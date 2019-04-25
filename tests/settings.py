# -*- coding: utf-8
import os

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "cpzatsr_#3dk9ad*sb%2bp+6s5o0v%1b!i$*6@hw5&izixn5@r"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "dj_sms.apps.DjSmsConfig",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
DJSMS = {
    'default': {
        "BACKEND": "dj_sms.backends.aliyun.AliyunSMS",
        "AccessKeyID": os.environ.get("AccessKeyID", ""),
        "AccessKeySecret": os.environ.get("AccessKeySecret", ""),
        "SignName": "身份验证",
    },
    "weimi": {
        "BACKEND": "dj_sms.backends.weimi.WeimiSMS",
        "uid": "ipScrzAANE33",
        "pas": "jc5fv2nc",
        "cid": "nEFFQCJiIImA"
    }
}
