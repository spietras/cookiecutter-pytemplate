<h1 align="center">{{cookiecutter.repo_name}}</h1>

<div align="center">

[![Running tests]({{cookiecutter.repo_url}}/actions/workflows/test.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/test.yml)
[![Deploying docs]({{cookiecutter.repo_url}}/actions/workflows/docs.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/docs.yml)

</div>

---

{{cookiecutter.short_description}}

It lets you easily accomplish the following things:

- [x] **nothing**

But at least it shows some opinionated best practices about python projects.

## Installing

Using ```pip```<sup>*</sup>:

```sh
pip install {{cookiecutter.repo_name}}
```

<sup><sup>* assuming the authors bothered to release the package on PyPI...</sup></sup>

## Usage as a library

**Very** useful example:

```python
from {{cookiecutter.repo_name}}.subpackage.module import identity

x = 1
assert x is identity(x)
```

## Usage as a command line tool

```sh
$ {{cookiecutter.repo_name}}
Hello World.
```