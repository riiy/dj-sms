=============================
Django SMS Package
=============================

.. image:: https://badge.fury.io/py/dj-sms.svg
    :target: https://badge.fury.io/py/dj-sms

.. image:: https://travis-ci.org/riiy/dj-sms.svg?branch=master
    :target: https://travis-ci.org/riiy/dj-sms

.. image:: https://codecov.io/gh/riiy/dj-sms/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/riiy/dj-sms

send sms message(发送短信的django package)

Documentation
-------------

The full documentation is at https://dj-sms.readthedocs.io.

Quickstart
----------

Install Django SMS Package::

    pip install dj-sms

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
