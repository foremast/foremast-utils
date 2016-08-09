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

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class ParserError(Exception):
    pass


class Parser(object):
    """A Parser for urls"""

    def __init__(self, url, lower=True):

        if not url:
            error = 'url may not be "None" or empty'
            raise ParserError(error)
        self.url = url.lower() if lower else url

    def parse_url(self):
        """Parses a git/ssh/http(s) url"""

        url = urlparse(self.url).path

        # handle git
        url = url.split('.git')[0]

        if ':' in url:
            url = url.split(':')[1]

        # Ony capture last two list items
        project, repo = url.split('/')[-2:]

        return project, repo
