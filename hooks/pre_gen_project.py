import re
import sys

REPO_NAME_EXIT_CODE = 1
PACKAGE_NAME_EXIT_CODE = 2
PACKAGE_IMPORT_NAME_EXIT_CODE = 3

REPO_NAME_REGEX = r"^[a-zA-Z0-9_.-]+$"
PACKAGE_NAME_REGEX = r"^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9])$"
PACKAGE_IMPORT_NAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

repo_name = "{{ cookiecutter.repo_name }}"
package_name = "{{ cookiecutter.package_name }}"
package_import_name = "{{ cookiecutter.package_import_name }}"


def regex_error(name, value, regex, exit_code):
    print("ERROR: %s is not a valid %s! REGEX: '%s'" % (value, name, regex))
    sys.exit(exit_code)


if not re.match(REPO_NAME_REGEX, repo_name):
    regex_error("repository name", repo_name, REPO_NAME_REGEX, REPO_NAME_EXIT_CODE)

if not re.match(PACKAGE_NAME_REGEX, package_name):
    regex_error(
        "package name", package_name, PACKAGE_NAME_REGEX, PACKAGE_NAME_EXIT_CODE
    )

if not re.match(PACKAGE_IMPORT_NAME_REGEX, package_import_name):
    regex_error(
        "package import name",
        package_import_name,
        PACKAGE_IMPORT_NAME_REGEX,
        PACKAGE_IMPORT_NAME_EXIT_CODE,
    )
