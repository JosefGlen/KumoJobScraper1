from django.core.management.base import BaseCommand
from jobs.models import Jobs
from Scraper.job_scraper_glassdoor import get_glassdoor_jobs_posted_today  # Import the function

class Command(BaseCommand):
    help = "Scrape jobs and store them in the database"

    def handle(self, *args, **kwargs):
        jobs = get_glassdoor_jobs_posted_today()
        for job in jobs:
            if not Jobs.objects.filter(url=job["url"]).exists():
                Jobs.objects.create(
                    title=job["title"],
                    company=job["company"],
                    location=job["location"],
                    salary=job["salary"],
                    url=job["url"],
                    description=job["description"]
                )
        self.stdout.write(self.style.SUCCESS("Successfully scraped and stored jobs"))