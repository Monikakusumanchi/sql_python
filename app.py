import mysql.connector

def create_table(connection):
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def insert_data(connection):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO employees (name, age) VALUES (%s, %s)
    """
    data = ("John Doe", 30)
    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()

def select_data(connection):
    cursor = connection.cursor()
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    result = cursor.fetchall()
    cursor.close()
    return result

def main():
    try:
        # Connect to MySQL Container
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Replace with the MySQL container name
            port="3306",
            user="root",
            password="myrootpassword",  # Replace with your MySQL root password
            database="mydatabase"      # Replace with your database name
        )
        


        create_table(connection)
        insert_data(connection)

        # Retrieve and print data from the table
        data = select_data(connection)
        for row in data:
            print(row)

        connection.close()

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

if __name__ == "__main__":
    main()
