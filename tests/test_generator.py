from gogoutils.generator import Generator


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


def test_generate_dns():

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

    for project in PROJECTS:

        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        app = '{0}{1}'.format(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
        )

        assert app == g.app_name()


def test_generate_archaius():

    options = {}

    for project in PROJECTS:

        g = Generator(
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
            PROJECTS[project]['env'],
        )

        options['s3'] = 'archaius-{0}/{1}/{2}{1}/'.format(
            PROJECTS[project]['env'],
            PROJECTS[project]['project'],
            PROJECTS[project]['repo'],
        )

        archaius = g.archaius()
        for option in archaius:
            assert options[option] == archaius[option]
