from shop.models import SiteDetail


def sitedetail(request):
    sitedetail, created = SiteDetail.objects.get_or_create()
    return {"sitedetail": sitedetail}
