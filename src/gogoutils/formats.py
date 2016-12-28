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
"""Determine the generator format"""
try:
    from collections import ChainMap
except ImportError:
    from ConfigParser import _Chainmap as ChainMap

DEFAULT_FORMAT = {
    'apigateway_domain': 'api.{env}.{domain}',
    'app': '{repo}{project}',
    'dns_elb_region': '{repo}.{project}.{region}.{env}.{domain}',
    'dns_elb': '{repo}.{project}.{env}.{domain}',
    'dns_global': '{repo}.{project}.{env}.{domain}',
    'dns_instance': '{repo}{project}-xx.{env}.{domain}',
    'domain': 'example.com',
    'git_repo_configs': '{raw_project}/{raw_repo}-config',
    'git_repo_qe': '{raw_project}/{raw_repo}-qa',
    'git_repo': '{raw_project}/{raw_repo}',
    'iam_base': '{project}_{repo}',
    'iam_group': '{project}',
    'iam_lambda_role': '{project}_{repo}_lambda_role',
    'iam_policy': '{project}_{repo}_policy',
    'iam_profile': '{project}_{repo}_profile',
    'iam_role': '{project}_{repo}_role',
    'iam_user': '{project}_{repo}',
    'jenkins_job_name': '{project}_{repo}',
    's3_app_bucket': '{project}-{repo}',
    's3_archaius_name': 'archaius-{env}/{project}/{repo}{project}/',
    's3_bucket_path': '{project}/{repo}{project}',
    's3_bucket': 'archaius-{env}',
}


class Formats(object):
    def __init__(self, config={}):
        self.config = ChainMap(config, DEFAULT_FORMAT)

    def get_formats(self):
        return self.config

    def __getitem__(self, key):
        return self.config[key]
