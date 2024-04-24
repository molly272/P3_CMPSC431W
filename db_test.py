#!/usr/bin/env python

import psycopg2 as db_connect  


host_name="localhost"
db_user="postgres"
db_password="molly"
db_name="postgres"

connection = db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name)

cursor = connection.cursor()

def fetch_query(connection, option):
    cursor = connection.cursor()
    try:
        if option == 1:
            print("INSERT INTO TableName (Column1, Column2, ...) VALUES (Value1, Value2, ...);")
            tablename = str(input("Enter TableName : "))
            cols = str(input("Enter (Column1, Column2, ...) : "))
            vals = str(input("Enter (Value1, Value2, ...) : "))
            query = f"INSERT INTO {tablename} {cols} VALUES {vals};"
            print(query)
            cursor.execute(query)
        elif option == 2:
            print("DELETE FROM TableName WHERE Condition;")
            tablename = str(input("Enter TableName : "))
            cond = str(input("Enter Condition : "))
            query = f"DELETE FROM {tablename} WHERE {cond};"
            print(query)
            cursor.execute(query)
        elif option == 3:
            print("UPDATE TableName SET Column1 = NewValue WHERE Condition;")
            tablename = str(input("Enter TableName : "))
            col1 = str(input("Enter Column1 : "))
            nv = str(input("Enter NewValue : "))
            cond = str(input("Enter Condition : "))
            query = f"UPDATE {tablename} SET {col1} = {nv} WHERE {cond};"
            print(query)
            cursor.execute(query)
        elif option == 4:
            print("SELECT * FROM TableName WHERE Condition;")
            tablename = str(input("Enter TableName : "))
            cond = str(input("Enter Condition : "))
            query = f"SELECT * FROM {tablename} WHERE {cond};"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        elif option == 5:
            print("SELECT AGG_FUN(Column) FROM TableName;")
            agg = str(input("Enter SUM, AVG, COUNT, MIN, or MAX : "))
            col = str(input("Enter Column : "))
            tablename = str(input("Enter TableName : "))
            query = f"SELECT {agg}({col}) FROM {tablename};"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        elif option == 6:
            print("SELECT * FROM TableName ORDER BY Column ASC/DESC;")
            tablename = str(input("Enter TableName : "))
            col = str(input("Enter Column : "))
            ad = str(input("Enter ASC or DESC : "))
            query = f"SELECT * FROM {tablename} ORDER BY {col} {ad};"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        elif option == 7:
            print("SELECT * FROM Table1 INNER JOIN Table2 ON Table1.Key = Table2.Key;")
            t1 = str(input("Enter Table1 : "))
            t2 = str(input("Enter Table2 : "))
            key = str(input("Enter Key : "))
            query = f"SELECT * FROM {t1} INNER JOIN {t2} ON {t1}.{key} = {t2}.{key};"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        elif option == 8:
            print("SELECT Column, COUNT(*) FROM TableName GROUP BY Column;")
            tablename = str(input("Enter TableName : "))
            col = str(input("Enter Column : "))
            query = f"SELECT {col}, COUNT(*) FROM {tablename} GROUP BY {col};"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        elif option == 9:
            print("SELECT * FROM TableName WHERE Column IN (SELECT Column FROM AnotherTable);")
            tablename = str(input("Enter TableName : "))
            col = str(input("Enter Column : "))
            another_table = str(input("Enter AnotherTable : "))
            query = f"SELECT * FROM {tablename} WHERE {col} IN (SELECT {col} FROM {another_table});"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
        connection.commit()
    except (Exception, db_connect.DatabaseError) as error:
        print(f"Error {error}")
        connection.rollback()


while True:
    print("\nSelect an option:")
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Update Data")
    print("4. Search Data")
    print("5. Aggregate Functions")
    print("6. Sorting")
    print("7. Joins")
    print("8. Grouping")
    print("9. Subqueries")
    print("0. Exit")
    option = int(input("Enter your choice : "))
    if option == 0:
        break
    fetch_query(connection, option)

print("Connection closed")

connection.close()
