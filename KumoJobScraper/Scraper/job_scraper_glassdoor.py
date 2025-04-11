from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def jobs_posted_today(website):
    """Scrape job listings from Glassdoor in Michigan"""

    # Set up the webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(website["url"])
    time.sleep(3)  # Wait for the page to load
    
    # Optional if we would like to limit our search for specific jobs
    # # Locate the search box and enter the query (e.g., "Software Engineer")
    # job_search_box = driver.find_element(By.ID, "searchBar-jobTitle")
    # location_search_box = driver.find_element(By.ID, "searchBar-location")
    
    # job_search_box.clear()
    # job_search_box.send_keys("Software Engineer")  # Job title to search
    # location_search_box.clear()
    # location_search_box.send_keys("Michigan")  # Location
    # location_search_box.send_keys(Keys.RETURN)  # Hit the Enter key to start the search
    
    time.sleep(5)  # Wait for the results to load

    if website["name"] == "linkedin":
        try:
            #Nukes Linkedins stupid login in request, resets styling so that I can actually scroll
            driver.execute_script("""
                let modal = document.querySelector('.top-level-modal-container');
                if (modal) {
                    modal.remove();
                }

                // Reset body styles that prevent scrolling
                document.body.style.overflow = 'auto';
                document.body.style.position = 'static';
            """)
            print("Modal forcibly removed.")
        except Exception as e:
            print(f"Failed to remove modal: {e}")

    # Extract job listings
    job_listings = []

    # Commented Out For testing purposes - Grabs every Job that meets those criteria
    # Keep clicking "Load More" until all the jobs for today are loaded
    if website["name"] == "glassdoor":
        while True:
            try:
                # Scroll to the bottom of the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # Wait a bit for content to load

                # Find and click the "Load More" button if it exists
                load_more_button = driver.find_element(By.XPATH, "//button[@data-test='load-more']")
                load_more_button.click()
                time.sleep(5)  # Wait for more jobs to load after clicking
            except Exception as e:
                print("No more jobs to load or error clicking 'Load More':", e)
                break

    # Loop to extract the job details from each result on the page
    job_elements = driver.find_elements(By.CLASS_NAME, website["job_card"])
    
    for job in job_elements:
        try:
            try:
                title = job.find_element(By.CLASS_NAME, website["job_title"]).text.strip()
            except Exception:
                title = "Unknown"
            try:
                company = job.find_element(By.CLASS_NAME, website["job_employer"]).text.strip()
            except Exception:
                company = "Unknown"
            try:
                location = job.find_element(By.CLASS_NAME, website["job_location"]).text.strip()
            except Exception:
                location = "Michigan"
            try:
                salary = job.find_element(By.CLASS_NAME, website["job_pay"]).text.strip()
            except Exception:
                salary = "Unknown"
            try:
                url = job.find_element(By.CLASS_NAME, website["job_url"]).get_attribute("href")
            except Exception:
                url = website["url"]

            job.click()
            time.sleep(3)  # Wait for the job detail page to load

            driver.find_element(By.CLASS_NAME, website["show_more"]).click()

            # Wait for the job description to load on the new page
            try:
                description_element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, website["job_description"]))
                )
                description = description_element.get_attribute("outerHTML")
            except Exception as e:
                description = "<p>No description available<p>"
            
            job_listings.append({
                "title": title,
                "company": company,
                "location": location,
                "salary" : salary,
                "description" : description,
                "url": url
            })
        except Exception as e:
            print(f"Error extracting a job listing")
            continue
    
    # Close the browser after scraping
    driver.quit()

    return job_listings