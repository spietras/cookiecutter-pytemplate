"""

Notice we don't follow the same test structure as in unit tests.
That's because functional tests should test the code from "outside".
So we don't need to follow any hierarchy.

"""

import pytest
from {{cookiecutter.package_import_name}}.__main__ import cli
from typer.testing import CliRunner


class Test{{cookiecutter.package_name.replace("-", "")|title}}:

    # pytest fixture, passed to all methods by argument
    @pytest.fixture(autouse=True, scope="class")
    def runner(self):
        return CliRunner()

    def test_{{cookiecutter.package_import_name}}_returns_zero(self, runner):
        result = runner.invoke(cli)
        assert not result.exception
        assert result.exit_code == 0

    def test_{{cookiecutter.package_import_name}}_prints_something(self, runner):
        result = runner.invoke(cli)
        assert result.output

    def test_{{cookiecutter.package_import_name}}_prints_help(self, runner):
        result = runner.invoke(cli, ['--help'])
        assert "Usage" in result.output

    def test_{{cookiecutter.package_import_name}}_works_with_arg(self, runner):
        result = runner.invoke(cli, ['--x', 2])
        assert not result.exception
        assert result.exit_code == 0
