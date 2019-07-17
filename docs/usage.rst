=====
Usage
=====

To use DJ Pony Django Docker Test Databases in a project, add it to your `INSTALLED_APPS`:

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
