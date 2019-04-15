from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string


class InvalidLiquidityBackendError(ImproperlyConfigured):
    pass


class BaseSMS:
    def __init__(self, params):
        pass

    def send_sms(self, phone=None, msg=None, *args, **kwargs):
        """

        :param phone:
        :param tmpl:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def send_batch(self, phones=None, msg=None, *args, **kwargs):
        """

        :param phones:
        :param tmpl:
        :param args:
        :param kwargs:
        :return:
        """
        pass
