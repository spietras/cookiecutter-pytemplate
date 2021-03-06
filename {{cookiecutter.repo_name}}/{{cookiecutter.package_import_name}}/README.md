<h1 align="center">{{cookiecutter.package_name}}</h1>

<div align="center">

{{cookiecutter.short_description}}

{% if cookiecutter.executable != 'y' -%}
[![Tests]({{cookiecutter.repo_url}}/actions/workflows/test-multiplatform.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/test-multiplatform.yml)
{% endif -%}
{% if cookiecutter.executable == 'y' and cookiecutter.extensive_testing != 'y' -%}
[![Tests]({{cookiecutter.repo_url}}/actions/workflows/test-docker.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/test-docker.yml)
{% endif -%}
{% if cookiecutter.executable == 'y' and cookiecutter.extensive_testing == 'y' -%}
[![Multiplatform tests]({{cookiecutter.repo_url}}/actions/workflows/test-multiplatform.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/test-multiplatform.yml)
[![Docker tests]({{cookiecutter.repo_url}}/actions/workflows/test-docker.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/test-docker.yml)
{% endif -%}
[![Docs]({{cookiecutter.repo_url}}/actions/workflows/docs.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/docs.yml)

</div>

---

It lets you easily accomplish the following things:

- [x] **nothing**

But at least it shows some opinionated best practices about python project structure.

## Installing

Using `pip`{% if cookiecutter.automatic_releases != 'y' %}<sup>\*</sup>{% endif %}:

```sh
pip install {{cookiecutter.package_name}}
```

{% if cookiecutter.automatic_releases != 'y' -%}
<sup><sup>\* assuming the authors bothered to release the package on PyPI...</sup></sup>
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
