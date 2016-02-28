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

    def dns(self):
        """Generate dns domain"""
        dns = '{0}.{1}.{2}.example.com'.format(
            self.repo,
            self.project,
            self.env
        )

        return dns
