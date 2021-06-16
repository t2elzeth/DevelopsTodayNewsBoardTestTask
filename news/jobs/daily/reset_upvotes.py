from django_extensions.management.jobs import DailyJob

from news.models import Upvote


class Job(DailyJob):
    help = "Job that resets upvotes once a day"

    def execute(self):
        Upvote.objects.all().delete()
