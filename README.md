# cookiecutter-pytemplate

`cookiecutter` template for `python` projects.

Example of a project: [spietras/pytemplate](https://github.com/spietras/pytemplate).

## Usage

Install [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) and run:

```sh
cookiecutter https://github.com/spietras/cookiecutter-pytemplate
```

Answer some basic questions and the repository will be created in current directory.

## Features

Just look at the example. The features include:

- `conda` as environment manager
- `poetry` as package manager
- standard package directory structure
- tests with `pytest`
- docs with `mkdocs` with `material` theme
- provided code for package resource retrieval
- `Dockerfile` for building Docker image of the package
- example of `jupyter` usage
- provided `Github Actions` for testing on different platforms, deploying docs on `Github Pages`, testing Docker build and making automatic releases
- `README` badges for actions status

## Notes

- Connect to Github with SSH if you want to use Actions. You need that to be able to change anything inside `.github` directory.
- You should pick a sensible name for your project, preferably all lowercase letter, using dashes and underscores should be the last resort
