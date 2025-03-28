from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 


# Set up the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL = "https://www.glassdoor.com/Job/michigan-us-jobs-SRCH_IL.0,11_IS527.htm?fromAge=1&sortBy=date_desc"

def get_glassdoor_jobs_in_michigan():
    """Scrape job listings from Glassdoor in Michigan"""

    driver.get(URL)
    time.sleep(3)  # Wait for the page to load
    
    # # Locate the search box and enter the query (e.g., "Software Engineer")
    # job_search_box = driver.find_element(By.ID, "sc.keyword")
    # location_search_box = driver.find_element(By.ID, "sc.location")
    
    # job_search_box.clear()
    # job_search_box.send_keys("Software Engineer")  # Job title to search
    # location_search_box.clear()
    # location_search_box.send_keys("Michigan")  # Location
    
    # location_search_box.send_keys(Keys.RETURN)  # Hit the Enter key to start the search
    time.sleep(5)  # Wait for the results to load

    # Extract job listings
    job_listings = []

    # Keep clicking "Load More" until all the jobs for today are loaded
    while True:
        try:
            # Wait for the "Load More" button to be clickable
            load_more_button = driver.find_element(By.XPATH, "//button[@data-test='load-more']")
            load_more_button.click()  # Click the "Load More" button
            time.sleep(5)  # Wait for more jobs to load
        except Exception as e:
            print("No more jobs to load or error clicking 'Load More':")
            break

    # Loop to extract the job details from each result on the page
    job_elements = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer__arQlW")
    
    for job in job_elements:
        try:
            title = job.find_element(By.CLASS_NAME, "JobCard_jobTitle__GLyJ1").text.strip()
            company = job.find_element(By.CLASS_NAME, "EmployerProfile_profileContainer__63w3R").text.strip()
            location = job.find_element(By.CLASS_NAME, "JobCard_location__Ds1fM").text.strip()
            url = job.find_element(By.CLASS_NAME, "JobCard_jobTitle__GLyJ1").get_attribute("href")
            
            job_listings.append({
                "title": title,
                "company": company,
                "location": location,
                "url": url
            })
        except Exception as e:
            print(f"Error extracting a job listing: {e}")
            continue

    return job_listings

# Fetch job listings and display
jobs = get_glassdoor_jobs_in_michigan()
if jobs:
    for job in jobs:
        print(f"\nJob: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"URL: {job['url']}")
        print("=" * 50)

# Close the browser after scraping
driver.quit()