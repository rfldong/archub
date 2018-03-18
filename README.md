# archub
A github cli à la arcanist.
This is very much a work in progress. I'll be adding features as I, or my co-workers, require them.

## Installation
```
$ python setup.py bdist_wheel
$ pip install dist/archub-*
```

## Usage
```
$ archub -h todo
usage: archub todo [-h] [-o ORG] -r REPO [-t TITLE] [-a ASSIGN] description

Quickly create an issue ticket for the specified repository

positional arguments:
  description

optional arguments:
  -h, --help            show this help message and exit
  -o ORG, --org ORG
  -r REPO, --repo REPO
  -t TITLE, --title TITLE
  -a ASSIGN, --assign ASSIGN
```
