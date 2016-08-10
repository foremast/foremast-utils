Gogo-utils
==========

gogo-utils is a utility library that generates a service name convention based on a repo url. The
library is mainly used to ensure that an application is able to easily know the path to a service
it may need.

.. code:: python

    from gogoutils import Parser, Generator

    url = 'https://github.com/gogoair/test.git'
    project, repo = Parser(url).parse_url()

    # a way to customize based on your conventions
    my_formats = {
        'jenkins_job_name': '{project}-{repo}-master',
        'app': 'app-{project}{repo}',
    }

    info = Generator(project, repo, 'dev', formats=my_formats)

    info.jenkins()
    > {'name': 'gogoair-test-master'}

    info.app_name()
    > app-gogoairtest


Classes
=======

Parser
--------
This class is needed to parse and gather details about a git repository.
A url is split up and the result is a project, repo.

Generator
---------
This class provides details about an application's details when using different technologies.
Its a simple and concise way to know how a specific app is referenced in jenkins, gitlab, s3,
iam, dns and among other services tools.

Formats
-------
This class provides a mechanism to alter the way Generator generates certain application references. It
is mainly referenced within Generator to provide that functionality.

In setting up the format the following variables are exposed:

``domain, env, project, repo, raw_project, raw_repo``


Contributions
=============

We encourage contributions, feedback and any bug fixes.

Running Tests
-------------

Running tests are very quick and easy when using tox. We validate against python 2.7, 3.4 and 3.5.

To run the tests simply execute

.. code:: sh

    # only needed once
    $ pip install -r requirements-dev.txt

    $ tox
