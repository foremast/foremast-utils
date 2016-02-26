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
    ]

    for url in urls:
        p = Parser(url)
        project, repo = p.parse_url()
        assert project == 'gogoair'
        assert repo == 'test'
