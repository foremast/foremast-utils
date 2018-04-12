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

import logging
from gogoutils.formats import Formats


class GeneratorError(Exception):
    pass


class Generator(object):
    """Generates application details"""

    def __init__(self, project, repo, env='dev', region='us-east-1', formats={}):

        params = {
            'project': project,
            'repo': repo,
            'env': env,
            'region': region,
        }

        for param, value in params.items():
            if not value:
                error = '"{0}" parameter may not be None or empty'.format(param)
                raise GeneratorError(error)

        self.format = Formats(formats)
        self.data = {
            'repo': params.get('repo').lower(),
            'project': params.get('project').lower(),
            'raw_project': params.get('project'),
            'raw_repo': params.get('repo'),
            'env': params.get('env').lower(),
            'region': params.get('region').lower(),
        }
        self.data.update(self.format.get_formats())

    @property
    def app(self):
        """Return the generated app name."""
        logging.warning('Deprecated: Use Generator.app_name() instead')
        return self.app_name()

    @property
    def project(self):
        """Return the project property"""
        return self.data['project']

    @property
    def repo(self):
        """Return the repo property"""
        return self.data['repo']

    @property
    def env(self):
        """Return the env property"""
        return self.data['env']

    def app_name(self):
        """Generate application name"""
        app = self.format['app'].format(**self.data)
        return app

    def dns_elb(self):
        """Generate elb dns domain"""
        dns = self.format['dns_elb'].format(**self.data)
        return dns

    def dns_elb_region(self):
        """Generate dns domain with region"""
        dns = self.format['dns_elb_region'].format(**self.data)
        return dns

    def dns_global(self):
        """Generate dns global domain with no region"""
        dns = self.format['dns_global'].format(**self.data)
        return dns

    def dns_region(self):
        """Generate region specific DNS"""
        dns = self.format['dns_region'].format(**self.data)
        return dns

    def dns_instance(self):
        """Generate dns instance"""
        instance = self.format['dns_instance'].format(**self.data)
        return instance

    def dns(self):
        """Combined dns details"""
        dns = {
            'elb': self.dns_elb(),
            'elb_region': self.dns_elb_region(),
            'global': self.dns_global(),
            'region': self.dns_region(),
            'instance': self.dns_instance(),
        }

        return dns

    def s3_app_bucket(self, include_region=False):
        """Generates s3 application bucket name.

        Args:
            include_region (bool): Include region in the name generation.
        """
        if include_region:
            s3_app_bucket = self.format['s3_app_region_bucket'].format(**self.data)
        else:
            s3_app_bucket = self.format['s3_app_bucket'].format(**self.data)
        return s3_app_bucket

    def shared_s3_app_bucket(self, include_region=False):
        """Generates shared s3 application bucket name.

        Args:
            include_region (bool): Include region in the name generation.
        """
        if include_region:
            shared_s3_app_bucket = self.format['shared_s3_app_region_bucket'].format(**self.data)
        else:
            shared_s3_app_bucket = self.format['shared_s3_app_bucket'].format(**self.data)
        return shared_s3_app_bucket

    def iam(self):
        """Generate iam details"""
        iam_base_name = self.format['iam_base'].format(**self.data)

        iam = {
            'group': self.format['iam_group'].format(**self.data),
            'lambda_role': self.format['iam_lambda_role'].format(**self.data),
            'policy': self.format['iam_policy'].format(**self.data),
            'profile': self.format['iam_profile'].format(**self.data),
            'role': self.format['iam_role'].format(**self.data),
            'user': self.format['iam_user'].format(**self.data),
        }

        return iam

    def archaius(self):
        """Generate archaius bucket path"""
        bucket = self.format['s3_bucket'].format(**self.data)
        path = self.format['s3_bucket_path'].format(**self.data)
        archaius_name = self.format['s3_archaius_name'].format(**self.data)
        archaius = {'s3': archaius_name, 'bucket': bucket, 'path': path}

        return archaius

    def jenkins(self):
        """Generate jenkins job details"""
        job_name = self.format['jenkins_job_name'].format(**self.data)
        job = {'name': job_name}

        return job

    def gitlab(self):
        """Generate gitlab details"""

        main_name = self.format['git_repo'].format(**self.data)
        qe_name = self.format['git_repo_qe'].format(**self.data)
        config_name = self.format['git_repo_configs'].format(**self.data)

        git = {
            'config': config_name,
            'main': main_name,
            'qe': qe_name,
        }

        return git

    def apigateway(self):
        """Generate apigateway details"""
        domain = self.format['apigateway_domain'].format(**self.data)

        return {
            'domain': domain,
        }
