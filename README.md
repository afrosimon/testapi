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

## Integration tests

Run:

```
$ pytest -svv --reuse-db
```

## Open questions and TODO:

- I do not appreciate giving CREATEDB privilege to the DB user, in a more proper setup (with containers for instance) this
might not mean much. I considered redefining the django_db_setup() fixture to only run migrations and create the DB only in
the bin/setup-db script but this not flexible (for instance if I would like to parallelize pytest).

## Deployment

The usual setup would be nginx + uwsgi. The uwsgi configuration is at the root of the project, uwsgi.ini. Otherwise simply
create the virtualenv, copy and adjust the sample nginx configuration as well as the systemd configuration.
