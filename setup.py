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

from setuptools import find_packages, setup

setup(
    name='gogo-utils',
    version='1.1',
    description='A utility library that generates service name convention details based on a repo url.',
    long_description=open('README.rst').read(),
    author='Sijis Aviles',
    author_email='saviles@gogoair.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    keywords="gogo python",
    url='https://github.com/gogoair/gogo-utils',
    download_url='https://github.com/gogoair/gogo-utils',
    platforms=['OS Independent'],
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
