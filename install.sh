#!/usr/bin/env bash

set -eo pipefail

PROJECT_NAME=fastai-courses

echo
echo " --- Your versions --- "
conda --version
pip --version

rm -fr build/
rm -fr dist/
rm -fr .eggs/
find . -name '*.egg-info' -exec rm -fr {} +
find . -name '*.egg' -exec rm -f {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +

ROOT_PROJECT=$(dirname "$0")

conda env remove -yq -n ${PROJECT_NAME}
conda create -y --name ${PROJECT_NAME} --file ${ROOT_PROJECT}/conda.txt
source activate ${PROJECT_NAME}
pip install -U -r ${ROOT_PROJECT}/requirements.txt
pip install -e ${ROOT_PROJECT}/.
conda deactivate

echo
echo " --- The environment ${PROJECT_NAME} is set --- "