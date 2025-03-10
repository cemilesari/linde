



from main.volton.models import *

def products_in_header(request):
    productstr = ProductsTr.objects.all().order_by("-created")[:20]
    return {'products_in_header': productstr}


def ind_in_header(request):
    productstr = Industries.objects.all().order_by("-created")[:20]
    return {'ind_in_header': productstr}