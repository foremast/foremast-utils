try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class Parser(object):
    """A Parser for urls"""

    def __init__(self, url):
        self.url = url

    def parse_url(self):
        """Parses a git/ssh/http(s) url"""

        url = urlparse(self.url).path

        # handle git
        url = url.split('.git')[0]

        if ':' in url:
            url = url.split(':')[1]

        # Ony capture last two list items
        project, repo = url.split('/')[-2:]

        return (project, repo)
