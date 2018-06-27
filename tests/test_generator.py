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
        'project': 'foremast',
        'repo': 'test',
        'env': 'dev',
        'region': 'us-west-2',
    },
    'repo2': {
        'project': 'foremast',
        'repo': 'test',
        'env': 'stage',
        'region': 'us-east-1',
    },
    'repo3': {
        'project': 'project1',
        'repo': 'repo1',
        'env': 'env1',
        'region': 'us-west-1',
    },
    'repo4': {
        'project': 'foremast.test',
        'repo': 'unknown',
        'env': 'stage',
        'region': 'us-west-2',
    },
}

ERROR_PROJECTS = {
    'repo1': {
        'project': 'foremast',
        'repo': 'test',
    },
    'repo2': {
        'project': 'foremast',
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
        'project': 'foremast',
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
    app_name = 'Testforemast'
    g = Generator('foremast', 'Test')
    assert app_name.lower() == g.app_name()


def test_valid_camel_cases():
    """Validate case sensitivity for Git repository names."""
    repo_name = 'foremast/Test-config'
    g = Generator('foremast', 'Test-config')
    uri_dict = g.gitlab()
    assert repo_name == uri_dict['main']


def test_generate_dns():
    """Validate generated DNS values."""
    for project in PROJECTS:
        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
            PROJECTS[project]['region'],
        )

        dns = '{0}.{1}.{2}.example.com'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
            PROJECTS[project]['env'],
        )

        dns_withregion = '{0}.{1}.{2}.{3}.example.com'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
            PROJECTS[project]['region'],
            PROJECTS[project]['env'],

        )
        instance = '{0}{1}-xx.{2}.example.com'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
            PROJECTS[project]['env'],
        )
        assert dns == g.dns()['elb']
        assert dns_withregion == g.dns()['elb_region']
        assert dns_withregion == g.dns()['region']
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

        iam_group = PROJECTS[project]['project']
        iam_lambda_role = '{0}_role'.format(iam_base)
        iam_policy = '{0}_policy'.format(iam_base)
        iam_profile = '{0}_profile'.format(iam_base)
        iam_role = '{0}_role'.format(iam_base)
        iam_user = iam_base

        assert iam_group == g.iam()['group']
        assert iam_lambda_role == g.iam()['lambda_role']
        assert iam_policy == g.iam()['policy']
        assert iam_profile == g.iam()['profile']
        assert iam_role == g.iam()['role']
        assert iam_user == g.iam()['user']


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
            region=PROJECTS[project]['region']
        )

        bucket = '{1}-{0}'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
        )
        region_bucket = '{1}-{0}-{2}'.format(
            PROJECTS[project]['repo'],
            PROJECTS[project]['project'],
            PROJECTS[project]['region']
        )

        shared_bucket = 'common-{0}'.format(
            PROJECTS[project]['project'],
        )
        region_shared_bucket = 'common-{0}-{1}'.format(
            PROJECTS[project]['project'],
            PROJECTS[project]['region']
        )

        assert bucket == g.s3_app_bucket()
        assert region_bucket == g.s3_app_bucket(include_region=True)
        assert shared_bucket == g.shared_s3_app_bucket()
        assert region_shared_bucket == g.shared_s3_app_bucket(include_region=True)


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


@pytest.mark.parametrize('formats, expected', [
    (
        {
            'test': '{project}|{repo}'
        },
        'foremast|test',
    ),
    (
        {
            'test': '{project}|{repo}-{special}',
            'special': 'pretty',
        },
        'foremast|test-pretty',
    ),
])
def test_autoformat_attr(formats, expected):
    """Validate unknown attributes are formatted."""
    p = PROJECTS['repo1']

    g = Generator(
        p['project'],
        p['repo'],
        env=p['env'],
        region=p['region'],
        formats=formats,
    )

    assert g.test == expected


class CustomFormatting(str):
    """Custom string formatter."""

    def format(self, *args, **kwargs):
        """Override default format method."""
        custom = kwargs['repo'].replace(' ', '--').upper()
        return super(CustomFormatting, self).format(*args, custom=custom, **kwargs)


def test_format_method():
    """Objects with :meth:`format` should string format correctly."""
    formats = {
        'test': CustomFormatting('{region}-{custom}+{project}'),
    }

    g = Generator(
        'project',
        'has an apple',
        env='home',
        region='Uruguay',
        formats=formats,
    )

    assert g.test == 'uruguay-HAS--AN--APPLE+project'
