from setuptools import find_packages, setup

setup(
    name='gogo-utils',
    version='0.3.2',
    description='A utility library used by various internal tools.',
    long_description=open('README.md').read(),
    author='Sijis Aviles',
    author_email='saviles@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    keywords="gogo python",
    url='https://github.com/gogoair/gogo-utils',
    download_url='https://github.com/gogoair/gogo-utils',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
)
