import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE', 'invanteris_it'),
        port=int(os.getenv('MYSQL_PORT', 4000)),
        ssl_disabled=False
    )
