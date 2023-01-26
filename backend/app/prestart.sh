#! /usr/bin/bash

# Let the DB start
python app/backend_pre_start.py

# Run First migration
alembic revision --autogenerate -m "First migration"

# Run upgrade head
alembic upgrade head

# Create initial data in DB
python app/initial_data.py
