import pyodbc

# Define the server, port, user, password, and database
server = "large-scale-data-management-mysql.database.windows.net"
port = 1433
user = "dbAdmin"
password = "Password~"
database = "MySQL Database"

# Build connection string
connString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}"

# Create connection
conn = pyodbc.connect(connString)

# Print a success message
print("Connected!")
