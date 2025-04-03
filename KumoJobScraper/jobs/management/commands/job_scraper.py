from django.core.management.base import BaseCommand
from jobs.models import Jobs
from concurrent.futures import ThreadPoolExecutor
from Scraper.job_scraper_glassdoor import jobs_posted_today  # Import the function

glassdoor = {
    "name":"glassdoor",
    "url": "https://www.glassdoor.com/Job/michigan-us-jobs-SRCH_IL.0,11_IS527.htm?fromAge=1&sortBy=date_desc",
    "job_card": "JobCard_jobCardContainer__arQlW",
    "job_title": "JobCard_jobTitle__GLyJ1",
    "job_employer": "EmployerProfile_profileContainer__63w3R",
    "job_location": "JobCard_location__Ds1fM",
    "job_pay": "JobCard_salaryEstimate__QpbTW",
    "job_url": "JobCard_jobTitle__GLyJ1",
    "show_more": "ShowMoreCTA_showMore__EtZpZ",
    "job_description": "JobDetails_jobDescription__uW_fK",
}

linkedin = {
    "name":"linkedin",
    "url": "https://www.linkedin.com/jobs/search?keywords=&location=Michigan&geoId=103051080&f_TPR=r86400&position=1&pageNum=0",
    "job_card": "base-card",
    "job_title": "base-search-card__title",
    "job_employer": "base-search-card__subtitle",
    "job_location": "job-search-card__location",
    "job_pay": None,
    "job_url": "base-card__full-link",
    "show_more": "show-more-less-html__button",
    "job_description": "show-more-less-html__markup",
}

websites = {"linkedin":linkedin, "glassdoor":glassdoor}

class Command(BaseCommand):
    help = "Scrape jobs and store them in the database"

    def add_arguments(self, parser):
        parser.add_argument("sources", nargs="+", type=str, help="List of job sites to scrape (glassdoor, linkedin)")

    def scrape_jobs(self, source):
        """Scrape jobs for a given source and store them in the database."""
        if source not in websites:
            self.stdout.write(self.style.ERROR(f"Invalid source: {source}"))
            return
        
        config = websites[source]
        try:
            jobs = jobs_posted_today(config)  # Handles both sources
            for job in jobs:
                if not Jobs.objects.filter(url=job["url"]).exists():
                    Jobs.objects.create(
                        website=source,
                        title=job["title"],
                        company=job["company"],
                        location=job["location"],
                        salary=job.get("salary", "Unknown"),  # Default salary to "Unknown"
                        url=job["url"],
                        description=job["description"],
                    )
            self.stdout.write(self.style.SUCCESS(f"Successfully scraped and stored jobs from {source}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error scraping {source}: {e}"))

    def handle(self, *args, **options):
        sources = options["sources"]
        
        with ThreadPoolExecutor() as executor:
            executor.map(self.scrape_jobs, sources)