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


def test_default_env():

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


def test_generate_iam():

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

        assert iam_user == g.iam()['user']
        assert iam_group == g.iam()['group']
        assert iam_role == g.iam()['role']
        assert iam_policy == g.iam()['policy']


def test_generate_jenkins():

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
