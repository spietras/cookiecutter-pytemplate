import os
import shutil

executable = "{{ cookiecutter.executable }}" == "y"
extensive_testing = "{{ cookiecutter.extensive_testing }}" == "y"
automatic_releases = "{{ cookiecutter.automatic_releases }}" == "y"
jupyter = "{{ cookiecutter.jupyter }}" == "y"


def remove(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


to_remove = []

if not executable:
    to_remove.extend(
        [
            "Dockerfile",
            ".dockerignore",
            ".github/workflows/test-docker.yml",
            ".github/workflows/registry.yml",
            "{{ cookiecutter.package_import_name }}/tests/functional",
            "{{ cookiecutter.package_import_name }}/src/{{ cookiecutter.package_import_name }}/__main__.py",
            "{{ cookiecutter.package_import_name }}/docs/docs/usage/cli.md",
        ]
    )

if executable and not extensive_testing:
    to_remove.extend(
        [
            ".github/workflows/test-multiplatform.yml",
        ]
    )

if not automatic_releases:
    to_remove.extend(
        [
            ".github/release-drafter.yml",
            ".github/workflows/draft.yml",
            ".github/workflows/pypi.yml",
            ".github/workflows/registry.yml",
        ]
    )

if not jupyter:
    to_remove.extend(
        [
            "notebooks",
        ]
    )

for path in set(to_remove):
    remove(path)
