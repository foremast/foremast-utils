class Generator(object):
    """Generates application details"""

    def __init__(self, project, repo, env):
        self.project = project
        self.repo = repo
        self.env = env
        self.app = '{0}{1}'.format(project, repo)

    def app_name(self):
        """Generate application name"""
        return self.app

    def dns_elb(self):
        """Generate dns domain"""
        dns = '{0}.{1}.{2}.example.com'.format(
            self.repo,
            self.project,
            self.env
        )

        return dns

    def dns_instance(self):
        """Generate dns instance"""

        instance = '{0}{1}-xx.{2}.example.com'.format(
            self.repo,
            self.project,
            self.env,
        )

        return instance

    def dns(self):
        """Combined dns details"""
        dns = {
            'elb': self.dns_elb(),
            'instance': self.dns_instance(),
        }

        return dns

    def archaius(self):
        """Generate archaius bucket path"""
        archaius = {}

        archaius['s3'] = 'archaius-{0}/{1}/{2}{1}/'.format(
            self.env,
            self.project,
            self.repo,
        )

        return archaius
