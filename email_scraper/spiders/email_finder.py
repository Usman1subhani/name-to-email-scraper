import scrapy
import re
import pandas as pd
from googlesearch import search
import os

class EmailFinderSpider(scrapy.Spider):
    name = "email_finder"
    custom_settings = {
        'DEPTH_LIMIT': 2  # Set depth limit to 2
    }

    def start_requests(self):
        # Check if input CSV exists
        if not os.path.exists("input.csv"):
            self.logger.error("input.csv file not found")
            return

        # Load input CSV
        df = pd.read_csv("input.csv")

        for _, row in df.iterrows():
            domain = row["domain"]
            company_name = row["company_name"]

            # If domain is missing, find it via Google search
            if pd.isna(domain) or domain.strip() == "":
                search_query = f"{company_name} official website"
                try:
                    domain = next(search(search_query, num_results=1))  # Get first result
                except StopIteration:
                    domain = None

            if domain:
                url = f"https://{domain}" if not domain.startswith("http") else domain
                yield scrapy.Request(url=url, callback=self.parse, meta={"company_name": company_name})

    def parse(self, response):
        company_name = response.meta["company_name"]
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))

        for email in emails:
            yield {
                "company_name": company_name,
                "email": email
            }

        # Follow links to explore deeper
        for next_page in response.css("a::attr(href)").getall():
            if next_page.startswith("/"):
                next_page = response.urljoin(next_page)
            elif not next_page.startswith(("http", "https")):
                continue  # Skip invalid URLs
            yield scrapy.Request(url=next_page, callback=self.parse, meta={"company_name": company_name})
