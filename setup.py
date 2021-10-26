#!/usr/bin/env python
#   foremast-utils - Utility generating application details
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
"""foremast-utils installer"""

import setuptools

with open('requirements.txt', 'rt', encoding="ascii") as reqs_file:
    REQUIREMENTS = reqs_file.readlines()

with open('README.rst', encoding="ascii") as readme_file:
    readme_content = readme_file.read()

if __name__ == "__main__":
    setuptools.setup(
        name='foremast-utils',
        description='A utility library for Foremast that generates names based on a common naming convention.',
        long_description=readme_content,
        author='Foremast',
        author_email='joelvasallo+foremast@gmail.com',
        packages=setuptools.find_packages(where='src'),
        package_dir={'': 'src'},
        setup_requires=['setuptools_scm'],
        use_scm_version={'local_scheme': 'dirty-tag'},
        install_requires=REQUIREMENTS,
        include_package_data=True,
        keywords="naming python spinnaker foremast foremast-utils",
        url='https://github.com/foremast/foremast-utils',
        download_url='https://github.com/foremast/foremast-utils',
        platforms=['OS Independent'],
        license='Apache License (2.0)',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
        ], )
