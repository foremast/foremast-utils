"""Determine the generator format"""
try:
    from collections import ChainMap
except ImportError:
    from ConfigParser import _Chainmap as ChainMap

DEFAULT_FORMAT = {
    'domain': 'example.com',
    'app': '{repo}{project}',
    'dns_elb': '{repo}.{project}.{env}.{domain}',
    'dns_instance': '{repo}{project}-xx.{env}.{domain}',
    'iam_base': '{project}_{repo}',
    'iam_user': '{project}_{repo}',
    'iam_group': '{project}',
    'iam_role': '{project}_{repo}_role',
    'iam_policy': '{project}_{repo}_policy',
    'iam_profile': '{project}_{repo}_profile',
    's3_bucket': 'archaius-{env}',
    's3_bucket_path': '{project}/{repo}{project}',
    's3_archaius_name': 'archaius-{env}/{project}/{repo}{project}/',
    'jenkins_job_name': '{project}_{repo}',
    'git_repo': '{raw_project}/{raw_repo}',
    'git_repo_qe': '{raw_project}/{raw_repo}-qa',
    'git_repo_configs': '{raw_project}/{raw_repo}-config',
}


class Formats(object):

    def __init__(self, config={}):
        self.config = ChainMap(config, DEFAULT_FORMAT)

    def get_formats(self):
        return self.config

    def __getitem__(self, key):
        return self.config[key]
