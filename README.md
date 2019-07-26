OpenShift CLI (oc) thin wrapper for Python3
===========================================

This *oc library* is a thin wrapper around the OpenShift CLI `oc`.

Usage
-----

```
>>> import oc
>>> oc.login('https://...openshift.com', 'mytoken')
>>> oc.set_project('myproject')
>>> oc.exec('mypod', 'curl -I http://localhost:8080')
>>> logs = oc.logs('mypod', since='1m')
```

Installation
------------

```
$ pip install oc
```

Documentation
-------------

```
$ pydoc oc.api
```
