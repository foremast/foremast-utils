How to do releases
==================

Setup
-----

Add the following to ``~/.pypirc`` file

.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository = https://pypi.python.org/pypi
    username = username
    password = xxxyyyzzz

Upload Release
--------------

When releasing a new version, the following needs to occur

- Update version in ``setup.py``
- Ensure all test via ``tox`` pass

Once that is taken care of, execute the following:

.. code:: sh

    $ python setup.py bdist_wheel upload
