# What is this?

This repository contains a template project for demonstrating Flask, Vue.js, Bulma and various Genomics APIs. It contains tagged versions to track progress while building the app. 

### Intro

Genomics APIs represent an evolving set of standards and protocols that assist developers in managing the plethora of data sources and in building more interoperable applications. Due to the expanding volume and diversity of genomics data, Application Programming Interfaces (APIs) are developed to provide secure and predictable access to a variety of applications and platforms.

# Gene Genie - API and Client

### Requirements
TBD

#### Build with `venv`:

```bash
    $ python3 -m venv venv
    $ source ./venv/bin/activate
    $ (venv) pip install -r ./requirements.txt
```
#### Run app locally:
```bash
    $ source ./venv/bin/activate
    $ (venv) export FLASK_APP=gene_genie.py 
    $ (venv) export FLASK_ENV=development 
    $ (venv) flask run -h localhost -p 8000
```