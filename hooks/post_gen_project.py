import os
import shutil

EXECUTABLE_PATHS = [
    "Dockerfile",
    ".github/workflows/docker-build.yml",
    ".github/workflows/docker-push.yml",
    "{{ cookiecutter.package_import_name }}/tests/functional",
    "{{ cookiecutter.package_import_name }}/src/{{ cookiecutter.package_import_name }}/__main__.py",
    "{{ cookiecutter.package_import_name }}/docs/docs/usage/cli.md",
]

AUTOMATIC_RELEASES_PATHS = [
    ".github/release-drafter.yml",
    ".github/workflows/draft.yml",
    ".github/workflows/pypi.yml",
    ".github/workflows/docker-push.yml",
]

JUPYTER_PATHS = ["notebooks"]

executable = "{{ cookiecutter.executable }}" == "y"
automatic_releases = "{{ cookiecutter.automatic_releases }}" == "y"
jupyter = "{{ cookiecutter.jupyter }}" == "y"


def remove(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


if not executable:
    for path in EXECUTABLE_PATHS:
        remove(path)

if not automatic_releases:
    for path in AUTOMATIC_RELEASES_PATHS:
        remove(path)

if not jupyter:
    for path in JUPYTER_PATHS:
        remove(path)
