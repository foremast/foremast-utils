gogo-utils
----------
```
/ A utility library used by various \
\ internal tools.                   /
 -----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Classes
-------

***Parser***
This class is needed to parse and gather details about a git repository.

```
from gogoutils.parser import Parser

url = 'git@github.com:gogoair/test.git'
project, repo = Parser(url).parse_url()

> print(project)
gogoair
> print(repo)
test
```

***Generator***
This class provides details about an application's details when using different technologies.
Its a simple and consise way to know how a specific app is referenced in jenkins, gitlab, asgard,
iam, dns and among other gogoair tools.

```
from gogoutils.generator import Generator
info = Generator(project, repo, 'dev')

info.jenkins()
> {'name': 'a_gogoair_test'}

info.app_name()
> gogoairtest
```

Run Tests
---------

Running tests are very quick and easy when using tox. We validate against python 2.7, 3.4 and 3.5.
To run the tests simply execute
```
# only needed once
$ pip install -r requirements-dev.txt

$ tox
```

Publishing (Artifactory)
------------------------
This is an internal library so it needs to be published to Artifactory.

In your `~/.pypirc` file, add the following:
```
[gogo]
repository = https://pypi.example.com
username = username
password = xxxyyyyzzzz
```

Update version number in `setup.py`.

Publish that version to pypi in Artifactory
```
$ python setup.py sdist upload -r gogo
```
