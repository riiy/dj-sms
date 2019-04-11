=====
Usage
=====

To use Django SMS Package in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_sms.apps.DjSmsConfig',
        ...
    )

Add Django SMS Package's URL patterns:

.. code-block:: python

    from dj_sms import urls as dj_sms_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_sms_urls)),
        ...
    ]
