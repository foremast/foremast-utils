.. image:: https://travis-ci.org/gogoair/gogo-utils.svg?branch=master
    :target: https://travis-ci.org/gogoair/gogo-utils

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

.. csv-table::
   :header: "VARIABLE", "DESCRIPTION"

    domain,Domain
    env,Environment
    project,Git project/group name (lowercase)
    repo,Git repo name (lowercase)
    raw_project,Git project/group name
    raw_repo,Git repo name

These are the services you can customize the formats along with their default format:

.. csv-table::
   :header: "SERVICE", "DEFAULT", "DESCRIPTION"
   :widths: 15,35,60

    domain,example.com,Domain
    app,{repo}{project},Application Name
    dns_elb,{repo}.{project}.{env}.{domain},FQDN of DNS ELB
    dns_instance,{repo}{project}-xx.{env}.{domain}, FQDN of instances
    iam_base,{project}_{repo},IAM profile base
    iam_user,{project}_{repo},IAM username
    iam_group,{project},IAM group name
    iam_role,{project}_{repo}_role,IAM role name
    iam_policy,{project}_{repo}_policy,IAM policy name
    iam_profile,{project}_{repo}_profile,IAM profile name
    s3_bucket,archaius-{env},S3 archaius bucket name
    s3_bucket_path,{project}/{repo}{project},S3 path for app (within s3_bucket)
    s3_archaius_name,archaius-{env}/{project}/{repo}{project}/,S3 full path for archaius
    s3_app_bucket,{project}-{repo},Application specific S3 bucket name
    jenkins_job_name,{project}_{repo},Jenkins job name
    git_repo,{raw_project}/{raw_repo},Apps git repo
    git_repo_qe,{raw_project}/{raw_repo}-qa,QA's git repo
    git_repo_configs,{raw_project}/{raw_repo}-config,Config git repo


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
