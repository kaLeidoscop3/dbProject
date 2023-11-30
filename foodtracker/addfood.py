import sqlite3

# Establish connection to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# List of breakfast items with nutritional information
breakfast_items = [
    ("Scrambled Eggs", 6, 1, 5, 78),
    ("Oatmeal", 6, 28, 2, 158),
    ("Greek Yogurt", 17, 6, 10, 170),
    ("Whole Wheat Toast", 7, 24, 3, 138),
    ("Banana", 1.3, 27, 0.4, 105),
    ("Peanut Butter", 7, 7, 16, 188),
    ("Cereal", 8, 24, 3, 120),
    ("Milk", 8, 12, 2.5, 103),
    ("Avocado", 2, 12, 15, 160),
    ("Cottage Cheese", 14, 3, 2, 81),
    ("Whole Grain Pancakes", 6, 33, 3, 198)
]

# Insert the breakfast items into the food table
for item in breakfast_items:
    cursor.execute('''
        INSERT INTO food (name, protein, carbohydrates, fat, calories)
        VALUES (?, ?, ?, ?, ?)
    ''', item)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Breakfast items added successfully to the database.")
