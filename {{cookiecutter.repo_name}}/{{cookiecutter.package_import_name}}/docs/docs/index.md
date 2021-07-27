# {{cookiecutter.package_name}}

{{cookiecutter.short_description}}

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
