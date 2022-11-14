# Requirements
1. Python 3.10.8
2. PostgreSQL 14.5

# Prerequisites
1. Create virtual enviroment:

    `python -m venv venv`
2. Install requirements:

    `pip install -r requirements.txt`
3. Create database named blog_db:
    `sudo -u postgres psql`

    `CREATE DATABASE blog_db;`
4. Run migrations:

    `export FLASK_APP=blog`
    
    `flask db upgrade`
