# Mobilpay Python SDK

A python sdk provided in a zipped format which we have decided to host in our gitlab to be used to send/receive xml payment requests/responses because life wasn't already tough but here we are.

## Deploy Package:
* Create distribution: `python3 setup.py sdist bdist_wheel`
* Create `.pypirc` file and place it in `$HOME`
* Run to publish: `python3 -m twine upload --repository gitlab dist/* --verbose`

.pypirc contents:
```
[distutils]
index-servers =
    gitlab

[gitlab]
repository = https://gitlab.com/api/v4/projects/35271465/packages/pypi
username = <deploy/ci/access token user name>
password = <deploy/ci/access token password>
```

## Changelog track
### v1.0.0b1
Initial beta dump of the mobilpay

### v1.0.1b1
* PyCrypto is dead as mentioned on [project issue page](https://github.com/pycrypto/pycrypto/issues/173)
  * Uninstalled it and install PyCryptodome which is a fork of PyCrypto

Note:
```text
The function time.clock() has been removed, 
after having been deprecated since Python 3.3: 
use time.perf_counter() or time.process_time() instead, 
depending on your requirements, to have well-defined behavior. (Contributed by Matthias Bussonnier in bpo-36895.)

```
