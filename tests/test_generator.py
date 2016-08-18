#   gogo-utils - Utility generating application details
#
#   Copyright 2016 Gogo, LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Validate Generator class."""
import pytest
from gogoutils.generator import Generator, GeneratorError


PROJECTS = {
    'repo1': {
        'project': 'gogoair',
        'repo': 'test',
        'env': 'dev',
    },
    'repo2': {
        'project': 'gogoair',
        'repo': 'test',
        'env': 'stage',
    },
    'repo3': {
        'project': 'project1',
        'repo': 'repo1',
        'env': 'env1',
    },
    'repo4': {
        'project': 'gogoair.test',
        'repo': 'unknown',
        'env': 'stage',
    },
}

ERROR_PROJECTS = {
    'repo1': {
        'project': 'gogoair',
        'repo': 'test',
    },
    'repo2': {
        'project': 'gogoair',
        'env': 'stage',
    },
    'repo3': {
        'repo': 'repo1',
        'env': 'env1',
    },
    'repo4': {
        'env': 'unknown',
    },
}


def test_default_env():
    """Validate defaults."""
    project = {
        'project': 'gogoair',
        'repo': 'no_env',
    }

    g = Generator(
        project['project'],
        project['repo'],
    )

    dns_elb = '{0}.{1}.dev.example.com'.format(
        project['repo'],
        project['project'],
    )

    assert dns_elb == g.dns()['elb']


def test_empty_params():
    """Validate empty."""
    for project in ERROR_PROJECTS:
        args = []

        for key in ['project', 'repo', 'env']:

            try:
                value = ERROR_PROJECTS[project][key]
            except KeyError:
                value = None

            args.append(value)

        with pytest.raises(GeneratorError):
            Generator(*args)


def test_camel_cases():
    """Validate Application name is lowercase."""
    app_name = 'Testgogoair'
    g = Generator('gogoair', 'Test')
    assert app_name.lower() == g.app_name()


def test_valid_camel_cases():
    """Validate case sensitivity for Git repository names."""
    repo_name = 'gogoair/Test-config'
    g = Generator('gogoair', 'Test-config')
    uri_dict = g.gitlab()
    assert repo_name == uri_dict['main']


def test_generate_dns():
    """Validate generated DNS values."""
    for project in PROJECTS:
        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        dns = '{0}.{1}.{2}.example.com'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
            PROJECTS[project]['env'],
        )

        instance = '{0}{1}-xx.{2}.example.com'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
            PROJECTS[project]['env'],
        )
        assert dns == g.dns()['elb']
        assert instance == g.dns()['instance']


def test_generate_app():
    """Validate generated App values."""
    for project in PROJECTS:

        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        app = '{0}{1}'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
        )

        assert app == g.app_name()


def test_generate_archaius():
    """Validate generated Archiaus values."""
    options = {}

    for repo in PROJECTS.values():

        g = Generator(
            repo['project'],
            repo['repo'],
            repo['env'],
        )

        options['s3'] = 'archaius-{0}/{1}/{2}{1}/'.format(
            repo['env'],
            repo['project'],
            repo['repo'],
        )
        options['bucket'] = 'archaius-{0}'.format(repo['env'])
        options['path'] = '{0}/{1}{0}'.format(repo['project'], repo['repo'])

        archaius = g.archaius()
        for option in archaius:
            assert options[option] == archaius[option]


def test_generate_iam():
    """Validate generated IAM values."""
    for project in PROJECTS:
        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        iam_base = '{0}_{1}'.format(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
        )

        iam_user = iam_base
        iam_group = PROJECTS[project]['project']
        iam_role = '{0}_role'.format(iam_base)
        iam_policy = '{0}_policy'.format(iam_base)
        iam_profile = '{0}_profile'.format(iam_base)

        assert iam_user == g.iam()['user']
        assert iam_group == g.iam()['group']
        assert iam_role == g.iam()['role']
        assert iam_policy == g.iam()['policy']
        assert iam_profile == g.iam()['profile']


def test_generate_jenkins():
    """Validate generated Jenkins values."""
    for project in PROJECTS:
        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        job_name = '{0}_{1}'.format(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
        )

        assert job_name == g.jenkins()['name']


def test_generate_gitlab():
    """Validate generated GitLab values."""
    for project in PROJECTS:
        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        git = '{0}/{1}'.format(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
        )

        git_main = git
        git_qe = '{0}-qa'.format(git)
        git_config = '{0}-config'.format(git)

        assert git_main == g.gitlab()['main']
        assert git_qe == g.gitlab()['qe']
        assert git_config == g.gitlab()['config']


def test_generate_properties():
    """Validate deprecated property."""
    g = Generator('project', 'repo')
    assert g.app == 'repoproject'
    assert g.project == 'project'
    assert g.repo == 'repo'
    assert g.env == 'dev'


def test_s3_bucket_format():
    """Validates generated s3 bucket name"""
    for project in PROJECTS:

        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        bucket = '{1}-{0}'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
        )

        assert bucket == g.s3_app_bucket()


def test_apigateway_domain():
    """Validate apigateway domain generator"""
    for project in PROJECTS:

        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        domain = 'api.{0}.example.com'.format(
            PROJECTS[project]['env'],
        )
        assert domain == g.apigateway()['domain']
