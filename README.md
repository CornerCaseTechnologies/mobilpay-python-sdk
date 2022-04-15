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