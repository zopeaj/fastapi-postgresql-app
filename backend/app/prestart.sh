#! /usr/bin/bash

# Let the DB start
python backend/app/app/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python backend/app/app/initial_data.py
