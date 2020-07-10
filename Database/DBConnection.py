from sshtunnel import SSHTunnelForwarder
import pymysql

# Database connection based on reference https://pynative.com/python-mysql-select-query-to-fetch-data/
# Switching to Local and AWS Instance
SSH_CONNECTION = True

# SSH Configuration
ssh_user = 'ubuntu'
ssh_password = ''
sql_remote_bind_address = '127.0.0.1'
ssh_port = 22

# MYSQL Configuration
if SSH_CONNECTION:
    sql_hostname = '54.72.85.207'
else:
    sql_hostname = 'localhost'
sql_username = 'root'
sql_password = 'Dublin@123'
sql_main_database = 'GroceryGo'
sql_port = 3306


# Creating Database Connection
def connection():
    if SSH_CONNECTION:
        ssh_server_connection = SSHTunnelForwarder(
            sql_hostname,
            ssh_username=ssh_user,
            ssh_pkey='/Users/chandana/Documents/Sem2/web/pycharm/OnlineGrocery/Database/Key/chandana.pem',
            remote_bind_address=(sql_remote_bind_address, sql_port)
        )
        ssh_server_connection.start()
        return True

    database_server_connection = pymysql.connect(
        host=sql_remote_bind_address,
        port=sql_port,
        user=sql_username,
        password=sql_password,
        db=sql_main_database
    )

    return database_server_connection


print(connection())