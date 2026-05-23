# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project layout

- `backend/` (this directory) — Django 6.0.5 project named `clickmart`. Python 3.13 venv lives at `.venv/`.
- `../frontend/` — sibling directory, currently empty placeholder.

The Django project module is `clickmart/` (settings, urls, wsgi, asgi). No Django apps have been created yet — `INSTALLED_APPS` contains only Django defaults and `urls.py` exposes only `admin/`. New work will typically begin with `python manage.py startapp <name>` and registering the app in `clickmart/settings.py`.

## Commands

Activate the venv first: `source .venv/bin/activate` (run from this `backend/` directory).

- Run dev server: `python manage.py runserver`
- Make / apply migrations: `python manage.py makemigrations` / `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Start a new app: `python manage.py startapp <name>` (then add to `INSTALLED_APPS`)
- Run all tests: `python manage.py test`
- Run a single test: `python manage.py test <app>.tests.<TestClass>.<test_method>`
- Django shell: `python manage.py shell`

## Database

`clickmart/settings.py` is configured for **PostgreSQL** (`clickmart_db` on `localhost:5432`, user `postgresql`, empty password) via `psycopg2-binary`. The Postgres database must exist locally before `migrate` will succeed.

The empty `db.sqlite3` file in this directory is a leftover from the initial `startproject` scaffold and is not used — the configured engine is Postgres, not SQLite.

## Dependencies

There is no `requirements.txt` / `pyproject.toml` / `Pipfile`. The current venv has: `django==6.0.5`, `psycopg2-binary==2.9.12`, `asgiref`, `sqlparse`. When adding dependencies, install into `.venv` and consider creating a `requirements.txt` (`pip freeze > requirements.txt`) so the environment is reproducible.

## Notes

- `SECRET_KEY` in `settings.py` is the auto-generated insecure dev key and `DEBUG = True` — both are dev-only defaults from `django-admin startproject`.
- `ALLOWED_HOSTS = []` — fine while `DEBUG = True`; must be populated before any non-dev use.
