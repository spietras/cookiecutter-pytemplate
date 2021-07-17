FROM continuumio/miniconda3:4.9.2-alpine

# add bash, because it's not available by default on alpine
# also install poetry
RUN apk add --no-cache bash \
    && conda install poetry \
    && conda clean -afy

# create new environment
# see: https://jcristharif.com/conda-docker-tips.html
# warning: for some reason conda can hang on "Executing transaction" for a couple of minutes
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml \
    && conda clean -afy \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

# "activate" environment for all commands (note: ENTRYPOINT is separate from SHELL)
SHELL ["conda", "run", "--no-capture-output", "-n", "{{cookiecutter.package_name}}", "/bin/bash", "-c"]

# add poetry files
COPY ./{{cookiecutter.package_import_name}}/pyproject.toml ./{{cookiecutter.package_import_name}}/poetry.lock /tmp/{{cookiecutter.package_import_name}}/
WORKDIR /tmp/{{cookiecutter.package_import_name}}

# install dependencies only (notice that no source code is present yet) and delete cache
RUN poetry install --no-root \
    && rm -rf ~/.cache/pypoetry

# add source and necessary files
COPY ./{{cookiecutter.package_import_name}}/src/ /tmp/{{cookiecutter.package_import_name}}/src/
COPY ./{{cookiecutter.package_import_name}}/LICENSE ./{{cookiecutter.package_import_name}}/README.md /tmp/{{cookiecutter.package_import_name}}/

# build wheel by poetry and install by pip (to force non-editable mode)
RUN poetry build -f wheel \
    && python -m pip install --no-cache-dir --find-links=dist {{cookiecutter.package_name}}

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "{{cookiecutter.package_name}}", "{{cookiecutter.package_name}}"]
