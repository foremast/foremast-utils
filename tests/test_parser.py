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

import pytest
from gogoutils.parser import Parser, ParserError


def test_parser_url():
    """Test parsing of url"""

    urls = [
        'http://github.com/foremast/test',
        'https://github.com/foremast/test',
        'http://github.com/foremast/test.git',
        'https://github.com/foremast/test.git',
        'https://username@testgithub.com/foremast/test.git',
        'git@github.com:foremast/test.git',
        'git://git@github.com/foremast/test.git',
        'file:///opt/git/foremast/test.git',
        'ssh://git@github.com/foremast/test.git',
        '/foremast/test.git',
        '/var/opt/gitlab/git-data/repositories/foremast/test.git',
        'foremast/Test.git',
        'http://GIT.example.com/foremast/tEst.git',
        'https://git.GIThub.com/foremast/teST.giT',
        'HTTPS://username@Testgithub.com/foremast/test.git',
    ]

    for url in urls:
        project, repo = Parser(url).parse_url()
        assert project == 'foremast'
        assert repo == 'test'


def test_parser_case_url():
    """Test parsing of url with case sensitive urls"""
    urls = [
        'http://github.com/foremast/Test-config',
        'https://github.com/foremast/Test-config',
        'http://github.com/foremast/Test-config.git',
        'https://github.com/foremast/Test-config.git',
        'https://username@testgithub.com/foremast/Test-config.git',
        'git@github.com:foremast/Test-config.git',
        'git://git@github.com/foremast/Test-config.git',
        'file:///opt/git/foremast/Test-config.git',
        'ssh://git@github.com/foremast/Test-config.git',
        '/foremast/Test-config.git',
        '/var/opt/gitlab/git-data/repositories/foremast/Test-config.git',
        'foremast/Test-config.git',
        'HTTPS://username@Testgithub.com/foremast/Test-config.git',
    ]

    for url in urls:
        project, repo = Parser(url, lower=False).parse_url()
        assert project == 'foremast'
        assert repo == 'Test-config'


def test_parser_invalid_url():
    """Test url is valid when parsed"""
    with pytest.raises(ParserError):
        project, repo = Parser('https://github.com').parse_url()


def test_empty_params():
    urls = [
        None,
        '',
    ]

    for url in urls:
        with pytest.raises(ParserError):
            g = Parser(url)
