<h1 align="center">{{cookiecutter.package_name}}</h1>

<div align="center">

[![Running tests]({{cookiecutter.repo_url}}/actions/workflows/test.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/test.yml)
[![Deploying docs]({{cookiecutter.repo_url}}/actions/workflows/docs.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/docs.yml)

</div>

---

{{cookiecutter.short_description}}

It lets you easily accomplish the following things:

- [x] **nothing**

But at least it shows some opinionated best practices about python project structure.

## Installing

Using ```pip```{% if cookiecutter.automatic_releases != 'y' %}<sup>*</sup>{% endif %}:

```sh
pip install {{cookiecutter.package_name}}
```

{% if cookiecutter.automatic_releases != 'y' -%}
<sup><sup>* assuming the authors bothered to release the package on PyPI...</sup></sup>
{%- endif %}

## Usage{% if cookiecutter.executable == 'y' %} as a library{% endif %}

**Very** useful example:

```python
import {{cookiecutter.package_import_name}}
```

{%- if cookiecutter.executable == 'y' %}
## Usage as a command line tool

```sh
$ {{cookiecutter.package_name}}
1
```
{%- endif %}