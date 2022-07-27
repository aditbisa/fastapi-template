#! /usr/bin/env sh

# Stop on error
set -e

# DB Migration
# alembic upgrade head

# Start Server
gunicorn app.main_wsgi:wsgi_app --reload
