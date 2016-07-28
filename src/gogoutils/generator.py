import logging
from gogoutils.formats import Formats


class GeneratorError(Exception):
    pass


class Generator(object):
    """Generates application details"""

    def __init__(self, project, repo, env='dev', formats={}):

        params = {
            'project': project,
            'repo': repo,
            'env': env,
        }

        for param, value in params.items():
            if not value:
                error = '"{0}" parameter may not be None or empty'.format(
                    param,
                )
                raise GeneratorError(error)

        self.format = Formats(formats)
        self.data = {
            'repo': params.get('repo').lower(),
            'project': params.get('project').lower(),
            'raw_project': params.get('project'),
            'raw_repo': params.get('repo'),
            'env': params.get('env').lower(),
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
        """Generate dns domain"""
        dns = self.format['dns_elb'].format(**self.data)
        return dns

    def dns_instance(self):
        """Generate dns instance"""
        instance = self.format['dns_instance'].format(**self.data)
        return instance

    def dns(self):
        """Combined dns details"""
        dns = {
            'elb': self.dns_elb(),
            'instance': self.dns_instance(),
        }

        return dns

    def iam(self):
        """Generate iam details"""
        iam_base_name = self.format['iam_base'].format(**self.data)

        iam = {'user': self.format['iam_user'].format(**self.data),
               'group': self.format['iam_group'].format(**self.data),
               'role': self.format['iam_role'].format(**self.data),
               'policy': self.format['iam_policy'].format(**self.data),
               'profile': self.format['iam_profile'].format(**self.data)}

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

        git = {'main': main_name,
               'qe': qe_name,
               'config': config_name}

        return git
