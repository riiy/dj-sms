from django.http import HttpResponse
from dj_sms import dj_sms


def index(request):
    res = dj_sms.send_sms('18500426633', '3456', 'bankorus')
    return HttpResponse(res)
