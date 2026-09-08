import os
import mysql.connector

def get_connection():
    user = os.environ.get('MYSQL_USER')
    host = os.environ.get('MYSQL_HOST')
    db = os.environ.get('MYSQL_DATABASE')
    pwd = os.environ.get('MYSQL_PASSWORD')
    
    # Debug log untuk melihat nilai variabel di Railway Deploy Logs
    print(f"DEBUG_CONN -> HOST: '{host}', USER: '{user}', DB: '{db}', PWD_LEN: {len(pwd) if pwd else 0}")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=pwd,
        database=db,
        port=int(os.environ.get('MYSQL_PORT', 4000)),
        ssl_disabled=False
    )
