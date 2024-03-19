from django.conf import settings
from shop.models import SiteDetail


def sitedetail(request):
    sitedetail, created = SiteDetail.objects.get_or_create()
    sitedetail.google_client_id = settings.GOOGLE_CLIENT_ID
    return {"sitedetail": sitedetail}
