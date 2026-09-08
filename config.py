MYSQL_HOST = os.environ.get("MYSQL_HOST", "gateway01.ap-southeast-1.prod.aws.tidbcloud.com") #sesuaikan host TIDB
MYSQL_USER = os.environ.get("MYSQL_USER", "3BysfHNMoeXfMG1.root") #sesuaikan user TIDB
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "C4SLr9NnGd6zmG1U")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "sys")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 4000))