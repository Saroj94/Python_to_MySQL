import csv
import mysql.connector

# Establish a connection to the MySQL database

cnx=mysql.connector.connect(
    host='localhost',
    user='root',
    password='mypassword',
    database='mydatabase'
)

# Create a cursor object
cursor = cnx.cursor()

# Read the CSV file and insert data into the MySQL database
with open('myoriginal_table.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    # Assuming the table 'addresses' already exists and has columns matching the CSV file
    insert_query = f"INSERT INTO database_table ({', '.join(header)}) VALUES ({', '.join(['%s'] * len(header))})"
    
    #iterate over each rows to insert
    for row in reader:
        #prepare the row values to handle empty rows
        prepared_row=[
            value if value not in ('', None) else None
            for value in row
        ]
        # Execute the insert query with the prepared values
        cursor.execute(insert_query, prepared_row)

# Commit the transaction
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
