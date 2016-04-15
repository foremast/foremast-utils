class GeneratorError(Exception):
    pass


class Generator(object):
    """Generates application details"""

    def __init__(self, project, repo, env='dev'):

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

        self.raw_project = params.get('project')
        self.project = params.get('project').lower()
        self.raw_repo = params.get('repo')
        self.repo = params.get('repo').lower()
        self.env = params.get('env').lower()
        self.app = '{0}{1}'.format(self.repo, self.project)

    def app_name(self):
        """Generate application name"""
        return self.app

    def dns_elb(self):
        """Generate dns domain"""
        dns = '{0}.{1}.{2}.example.com'.format(self.repo, self.project,
                                               self.env)
        return dns

    def dns_instance(self):
        """Generate dns instance"""
        instance = '{0}{1}-xx.{2}.example.com'.format(self.repo, self.project,
                                                      self.env)
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
        iam_base_name = '{0}_{1}'.format(self.project, self.repo)

        iam = {'user': iam_base_name,
               'group': self.project,
               'role': '{0}_role'.format(iam_base_name),
               'policy': '{0}_policy'.format(iam_base_name),
               'profile': '{0}_profile'.format(iam_base_name)}

        return iam

    def archaius(self):
        """Generate archaius bucket path"""
        archaius_name = 'archaius-{0}/{1}/{2}{1}/'.format(self.env,
                                                               self.project,
                                                               self.repo)
        archaius = {'s3': archaius_name}

        return archaius

    def jenkins(self):
        """Generate jenkins job details"""
        job_name = '{0}_{1}'.format(self.project, self.repo)
        job = {'name': job_name}

        return job

    def gitlab(self):
        """Generate gitlab details"""

        main_name = '{0}/{1}'.format(self.raw_project, self.raw_repo)
        qe_name = '{0}-qa'.format(main_name)
        config_name = '{0}-config'.format(main_name)

        git = {'main': main_name,
               'qe': qe_name,
               'config': config_name}

        return git
