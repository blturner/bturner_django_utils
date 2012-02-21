import datetime

from django.contrib.sites.models import Site


def current_date(request):
    return {
        'now': datetime.datetime.now()
    }


def site(request):
    return {
        'site': Site.objects.get_current()
    }
