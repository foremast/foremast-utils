from gogoutils.parser import Parser


def test_parser_url():
    """Test parsing of url"""

    urls = [
        'http://github.com/gogoair/test',
        'https://github.com/gogoair/test',
        'http://github.com/gogoair/test.git',
        'https://github.com/gogoair/test.git',
        'https://username@testgithub.com/gogoair/test.git',
        'git@github.com:gogoair/test.git',
        'git://git@github.com/gogoair/test.git',
        'file:///opt/git/gogoair/test.git',
        'ssh://git@github.com/gogoair/test.git',
        '/gogoair/test.git',
        '/var/opt/gitlab/git-data/repositories/gogoair/test.git',
        'gogoair/Test.git',
        'http://GIT.example.com/gogoair/tEst.git',
        'https://git.GIThub.com/gogoair/teST.giT',
        'HTTPS://username@Testgithub.com/gogoair/test.git',
    ]

    for url in urls:
        project, repo = Parser(url).parse_url()
        assert project == 'gogoair'
        assert repo == 'test'
