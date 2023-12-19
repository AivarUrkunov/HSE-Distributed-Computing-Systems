#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlalchemy
import os
import sys
import psycopg2
from flask import Flask, request, redirect, render_template


app = Flask(__name__)

# connect to postgres db
def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="postgres",
        password="password",
        port=5432
        )
    conn.autocommit = True
    
    return conn

# creating table in postgres in postgres db if not exists
def create_db_if_not_exists(conn, table_name):
    cur = conn.cursor()
    q_create = f"CREATE TABLE IF NOT EXISTS {table_name} (id PRIMARY KEY, number integer);"
    cur.execute(q_create)

# checking the input number with the achievement rule
def check_number_in_db_achvmnt_rule(conn, number, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE number = {number}")
    result = cur.fetchone()

    return result

# checking the input number with the achievement rule
def insert_number_db(conn, number, table_name):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {table_postgres} (number) VALUES ({number})")


@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/success', methods=['GET', 'POST'])
def sucess():
    error = ''
    table_postgres = 'dcs_t3_num_data'
    number = int(request.form.get('number'))
    conn = connect_db()
    create_db_if_not_exists(conn, table_postgres)
    result = check_number(conn, int(number), table_postgres)
    if result is not None:
        error = f"ERROR: Number {number} has already been received"
        return render_template('index.html', answer=error)

    result = check_number_achvmnt_rule(conn, int(number) + 1)
    if result is not None:
        error = f"ERROR: Number {number} is less by one than one of received numbers"
        return render_template('index.html', answer=error)

    insert_number_db(conn, number, table_name)
    
    new_number = number + 1

    return render_template('index.html', answer=new_number)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)


# In[ ]:


Running on http://127.0.0.1:8001
 * Running on http://10.110.124.212:8001

