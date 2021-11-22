# TESTAPI

Simple dummy project in Django & DRF. The aim is simply to mess around new features in Django or else, 
test out performance, etc.


## Developer setup

Here's a non-exhaustive list of server dependencies:
postgresql-10 postgresql-server-dev-10

Use virtualenvwrapper to create a Python 3 environment:

```
$ cd path/to/testapi
$ mkvirtualenv -p python3.6 testapi
(testapi)$ setvirtualenvproject
```

Install python dependencies:

```
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

To create a database for the local application, run this helper script to create the app user and database.

```
$ sudo -u postgres bin/setup-db
$ sudo -u postgres psql -c "ALTER ROLE testapi WITH PASSWORD '$SOME_PASSWORD'"
```

As for the configuration, you will need to setup some environment variables, those at the end of the uwsgi.ini.
With virtualenvwrapper the ~/.virtualenvs/testapi/bin/postactivate script is already there for such a use-case.

Run the migrations:

```
$ ./manage.py migrate
```

## Integration tests

Run:

```
$ pytest -svv --reuse-db
```

## Open questions and TODO:

- I do not appreciate giving CREATEDB privilege to the DB user, in a more proper setup (with containers for instance) this
might not mean much. I considered redefining the django_db_setup() fixture to only run migrations and create the DB only in
the bin/setup-db script but this not flexible (for instance if I would like to parallelize pytest).
- Should not necessitates having postgresql installed, should be DB agnostic (or see how to include container for DB)
- Configure journalctl disk usage / mem usage (like seriously... that shit gets crazy after a few months)

## Deployment

The usual setup would be nginx + uwsgi. The uwsgi configuration is at the root of the project, uwsgi.ini. Otherwise simply
create the virtualenv, copy and adjust the sample nginx configuration (server-config/nginx_sample). uWSGI can be configured
in a few ways, I would recommend creating a systemd service :

```
$ cp server-config/testapi.service /etc/systemd/system/testapi.service
$ systemctl enable testapi
$ systemctl start testapi
```
