import logging

import requests
from django.conf import settings
from .base import BaseSMS

logger = logging.getLogger(__name__)


class WeimiSMS(BaseSMS):
    API_URL = "http://api.weimi.cc/2/sms/send.html"

    def __init__(self, params):
        self.uid = params['uid']
        self.pas = params['pas']
        self.cid = params['cid']
        super(WeimiSMS, self).__init__(params)

    def send_sms(self, phone=None, msg=None, *args, **kwargs):
        cid = kwargs.get('cid', self.cid)

        resp = requests.post((self.API_URL),
                             data={
                                 "uid": self.uid,
                                 "pas": self.pas,
                                 "mob": phone,
                                 "cid": cid,
                                 "type": "json",
                                 "p1": msg,
                             }, timeout=3, verify=False)
        return resp

    def send_batch(self, phones=None, msg=None, *args, **kwargs):
        pass
