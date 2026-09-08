import os

MYSQL_HOST = os.environ.get("MYSQL_HOST", "gateway01.ap-southeast-1.prod.aws.tidbcloud.com")
MYSQL_USER = os.environ.get("MYSQL_USER", "3BysfHNMoeXfMGT.root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "C4SLr9NnGd6zmG1U")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "invanteris_it")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 4000))
