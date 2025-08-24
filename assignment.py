import sqlite3
import csv
import pandas as pd

# Connect to SQLite3 database
conn = sqlite3.connect("assign.db")
cursor = conn.cursor()

# SQL Query to get totals for customers aged 18–35
query = """
SELECT c.customer_id AS Customer,
       c.age AS Age,
       i.item_name AS Item,
       SUM(COALESCE(o.quantity,0)) AS Quantity
FROM Customer c
JOIN Sales s ON c.customer_id = s.customer_id
JOIN Orders o ON s.sales_id = o.sales_id
JOIN Items i ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
GROUP BY c.customer_id, c.age, i.item_name
HAVING SUM(COALESCE(o.quantity,0)) > 0
ORDER BY c.customer_id, i.item_name;
"""

# execute query
cursor.execute(query)
rows = cursor.fetchall()

# Write to CSV with ';' as delimiter
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Customer", "Age", "Item", "Quantity"])  
    writer.writerows(rows)

# Closing the connection
conn.close()

# If you want to read csv file
df = pd.read_csv("output.csv", sep=";")


