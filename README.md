# TESTAPI

Simply dummy project in Django & DRF. The aim is simply to mess around new features in Django or else, test out performance,
do some funky stuff to learn, essentially.

## Developer setup

Use virtualenvwrapper to create a Python 3 environment:

```
$ cd path/to/testapi
$ mkvirtualenv -p python3.6 testapi
(testapi)$ setvirtualenvproject $VIRTUAL_ENV $(pwd)
```

Install python dependencies:

```
$ pip install -r requirements.txt
```

To create a database for the local application, run this helper script to create the app user and database.

```
$ sudo -u postgres bin/setup-db
$ sudo -u postgres psql -c "ALTER ROLE testapi WITH PASSWORD '$SOME_PASSWORD'"
