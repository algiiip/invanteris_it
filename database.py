import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com'),
        user=os.environ.get('MYSQL_USER', '3BysfHNMoeXfMGT.root'),
        password=os.environ.get('MYSQL_PASSWORD', 'C4SLr9NnGd6zmG1U'),
        database=os.environ.get('MYSQL_DATABASE', 'invanteris_it'),
        port=int(os.environ.get('MYSQL_PORT', 4000)),
        ssl_disabled=False
    )
