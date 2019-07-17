=============================
DJ Pony Django Docker Test Databases
=============================

.. image:: https://badge.fury.io/py/dj-pony-docker-test-dbs.svg
    :target: https://badge.fury.io/py/dj-pony-docker-test-dbs

.. image:: https://travis-ci.org/techdragon/dj-pony-docker-test-dbs.svg?branch=master
    :target: https://travis-ci.org/techdragon/dj-pony-docker-test-dbs

.. image:: https://codecov.io/gh/techdragon/dj-pony-docker-test-dbs/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/techdragon/dj-pony-docker-test-dbs

Initialize and run clean test databases for postgres/mysql testing with Django Libraries.

Documentation
-------------

The full documentation is at https://dj-pony-docker-test-dbs.readthedocs.io.

Quickstart
----------

Install DJ Pony Django Docker Test Databases::

    pip install dj-pony-docker-test-dbs

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_pony_docker_test_dbs.apps.DjPonyDockerTestDbsConfig',
        ...
    )

Add DJ Pony Django Docker Test Databases's URL patterns:

.. code-block:: python

    from dj_pony_docker_test_dbs import urls as dj_pony_docker_test_dbs_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_pony_docker_test_dbs_urls)),
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
