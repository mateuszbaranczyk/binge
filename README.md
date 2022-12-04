# binge

## Installation for dev
Simply copy below comands one after one.

First of all install [poetry](https://python-poetry.org/docs/).

Download project:
```
git clone git@github.com:mateuszbaranczyk/binge.git
```
Create virtual env and install dependencies. In root:
```
poetry install
```
Activate env:
```
poetry shell
```
Run flask server. With `--debug` or not:
```
flask --app binge --debug run 
```
