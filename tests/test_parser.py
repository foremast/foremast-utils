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


def test_parser_case_url():
    """Test parsing of url with case sensitive urls"""
    urls = [
        'http://github.com/gogoair/Test-config',
        'https://github.com/gogoair/Test-config',
        'http://github.com/gogoair/Test-config.git',
        'https://github.com/gogoair/Test-config.git',
        'https://username@testgithub.com/gogoair/Test-config.git',
        'git@github.com:gogoair/Test-config.git',
        'git://git@github.com/gogoair/Test-config.git',
        'file:///opt/git/gogoair/Test-config.git',
        'ssh://git@github.com/gogoair/Test-config.git',
        '/gogoair/Test-config.git',
        '/var/opt/gitlab/git-data/repositories/gogoair/Test-config.git',
        'gogoair/Test-config.git',
        'HTTPS://username@Testgithub.com/gogoair/Test-config.git',
    ]

    for url in urls:
        project, repo = Parser(url, lower=False).parse_url()
        assert project == 'gogoair'
        assert repo == 'Test-config'


def test_empty_params():
    urls = [
        None,
        '',
    ]

    for url in urls:
        with pytest.raises(ParserError):
            g = Parser(url)
