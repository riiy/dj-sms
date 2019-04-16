from threading import local

from django.conf import settings
from django.utils.module_loading import import_string
from dj_sms.backends.base import BaseSMS, InvalidDjSmsBackendError

__all__ = [
    'BaseSMS',
]
__version__ = '0.1.0'
DEFAULT_DJSMS_ALIAS = 'weimi'


def _create_dj_sms(backend, **kwargs):
    try:
        try:
            conf = settings.DJSMS[backend]
        except KeyError:
            try:
                # Trying to import the given backend, in case it's a dotted path
                import_string(backend)
            except ImportError as e:
                raise InvalidDjSmsBackendError("Could not find backend '%s': %s" % (
                    backend, e))
            params = kwargs
        else:
            params = conf.copy()
            params.update(kwargs)
            backend = params.pop('BACKEND')
        backend_cls = import_string(backend)
    except ImportError as e:
        raise InvalidDjSmsBackendError(
            "Could not find backend '%s': %s" % (backend, e))
    return backend_cls(params)


class DjSmsHandler:
    """
    A DjSms Handler to manage access to DjSms instances.

    Ensure only one instance of each alias exists per thread.
    """

    def __init__(self):
        self._dj_sms = local()

    def __getitem__(self, alias):
        try:
            return self._dj_sms.dj_sms[alias]
        except AttributeError:
            self._dj_sms.dj_sms = {}
        except KeyError:
            pass

        if alias not in settings.DJSMS:
            raise InvalidDjSmsBackendError(
                "Could not find config for '%s' in settings.CACHES" % alias
            )

        liqu = _create_dj_sms(alias)
        self._dj_sms.dj_sms[alias] = liqu
        return liqu

    def all(self):
        return getattr(self._dj_sms, 'dj_sms', {}).values()


all_dj_sms = DjSmsHandler()


class DefaultDjSmsProxy:

    def __getattr__(self, name):
        return getattr(all_dj_sms[DEFAULT_DJSMS_ALIAS], name)

    def __setattr__(self, name, value):
        return setattr(all_dj_sms[DEFAULT_DJSMS_ALIAS], name, value)

    def __delattr__(self, name):
        return delattr(all_dj_sms[DEFAULT_DJSMS_ALIAS], name)

    def __contains__(self, key):
        return key in all_dj_sms[DEFAULT_DJSMS_ALIAS]

    def __eq__(self, other):
        return all_dj_sms[DEFAULT_DJSMS_ALIAS] == other


dj_sms = DefaultDjSmsProxy()
