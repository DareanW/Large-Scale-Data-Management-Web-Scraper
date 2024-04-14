#Connect to MongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dbUser:LSDM@cluster0.qlhs8tl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
mongoClient = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    mongoClient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Connect to MySQL
import pyodbc

# Define the server, port, user, password, and database
server = "teamproj-mysql.database.windows.net"
port = 1433
user = "DBUSER1"
password = "ABCd@123"
database = "TeamProjRedundancy"

# Build connection string
connString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}"

# Create connection
mySqlConn = pyodbc.connect(connString)

# Print a success message
print("Connected to MySQL!")



SQL_QUERY = """
SELECT  * FROM dbo.NewTable

"""
cursor = mySqlConn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r}")