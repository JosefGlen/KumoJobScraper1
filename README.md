# The Kumo Job Scraper

## Project Details

The **Job Scraper** is a powerful web scraping tool designed to collect job listings from various online websites and streamline the job searching process. Built using **Python, BeautifulSoup, Selenium, and Django**, this website allows users to search for jobs, filter results, and save their favorite listings for later viewing.

## Key Features

- **Automated Job Search** – Scrapes job postings from multiple sites.
- **User Accounts** – Save jobs across logins.
- **Filters & Sorting** – Search by keyword, location, company, and more.
- **Dashboard** – View and manage saved job listings.
- **Fast & Efficient** – Optimized scraping techniques with risk management.

## Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Web Scraping:** BeautifulSoup, Selenium
- **Database:** PostgreSQL / SQLite

## Project Management Structure

- **Course:** CIS 1512 - Principles of Software Engineering
- **Team:** Team Kumo
- **Member Roles**
  - **Project Manager**
    - Marquise Vaughan
  - **Backend Developers**
    - Devon O'Connor
  - **Frontend Developers**
    - Joseph Glenn
    - William Clay

## Installation & Setup

```sh
# Clone the repository
git clone https://github.com/JosefGlen/KumoJobScraper1

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv/Scripts/activate

# TroubleShooting
# It may be neccessary to run first
Set-ExecutionPolicy Unrestricted -Scope Process

# Install dependencies
pip install -r requirements.txt

# Choose the Directory
cd KumoJobScraper

# Migrate Object Classes
py manage.py migrate

# Run the Django server
py manage.py runserver
