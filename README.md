# 📧 Company Email Finder

This project is a **web scraper** that finds possible company email addresses based on **full name, domain, and company name**.  
It uses **Scrapy** and **Google Search** to extract emails from company websites.

---

## ⚡ Features
✅ Extracts emails using **domain names**  
✅ Uses **Google Search** to find company websites (if domain is missing)  
✅ Scrapes all **possible emails** from company web pages  
✅ Saves results in a **CSV file**  

---

## 🛠 Requirements

Before running the project, install the required dependencies:

```bash
pip install scrapy pandas googlesearch-python
```

 ## 📂 Setup Instructions
 ## 1️⃣ Prepare Your CSV File
 - Your CSV file must contain Full Name, Domain, and Company Name
 - Save it as input.csv in the project directory
 - Example Format:
   
| full_name   |  domain       | company_name   |
|:-|:-|:-|
| Usman Subhani   | example.com | Example Corp  |
| Alice Smith | another.com | Another Inc   |

## 2️⃣ Run the Scraper
Run the following command in your terminal:
```bash
scrapy crawl email_finder -o emails.csv

```
- It will scan websites and save emails in emails.csv
- If a domain is missing, it searches Google for the official website

## 📌 Output Format
The scraper will generate emails.csv with the following format:
| company_name   |  email |
|:-|:-|
| Example Corp   | usmansubhani595@gmail.com |
| Alice Smith | another.com | 

## 💡 Need Help?
If you face any issues, feel free to open an Issue on this repository! 😃

---
 

