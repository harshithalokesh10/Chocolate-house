import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS SeasonalFlavors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    available_until DATE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS IngredientInventory (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS CustomerFeedback (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    flavor_suggestion TEXT,
    allergy_concerns TEXT
)
''')

# Commit and close connection setup
conn.commit()
conn.close()
def add_seasonal_flavor(name, description, available_until):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO SeasonalFlavors (name, description, available_until) VALUES (?, ?, ?)',
                   (name, description, available_until))
    conn.commit()
    conn.close()

def view_seasonal_flavors():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM SeasonalFlavors')
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def add_ingredient(name, quantity, unit):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO IngredientInventory (name, quantity, unit) VALUES (?, ?, ?)',
                   (name, quantity, unit))
    conn.commit()
    conn.close()

def view_ingredients():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM IngredientInventory')
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

def add_customer_feedback(customer_name, flavor_suggestion, allergy_concerns):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO CustomerFeedback (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)',
                   (customer_name, flavor_suggestion, allergy_concerns))
    conn.commit()
    conn.close()

def view_customer_feedback():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM CustomerFeedback')
    feedback = cursor.fetchall()
    conn.close()
    return feedback
def main():
    while True:
        print("\nChocolate House Management System")
        print("1. Add Seasonal Flavor")
        print("2. View Seasonal Flavors")
        print("3. Add Ingredient to Inventory")
        print("4. View Ingredient Inventory")
        print("5. Add Customer Feedback")
        print("6. View Customer Feedback")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Flavor Name: ")
            description = input("Description: ")
            available_until = input("Available Until (YYYY-MM-DD): ")
            add_seasonal_flavor(name, description, available_until)
            print("Seasonal flavor added.")
        
        elif choice == "2":
            flavors = view_seasonal_flavors()
            print("\nSeasonal Flavors:")
            for flavor in flavors:
                print(f"ID: {flavor[0]}, Name: {flavor[1]}, Description: {flavor[2]}, Available Until: {flavor[3]}")
        
        elif choice == "3":
            name = input("Ingredient Name: ")
            quantity = int(input("Quantity: "))
            unit = input("Unit (e.g., kg, g, ml): ")
            add_ingredient(name, quantity, unit)
            print("Ingredient added to inventory.")
        
        elif choice == "4":
            ingredients = view_ingredients()
            print("\nIngredient Inventory:")
            for ingredient in ingredients:
                print(f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]} {ingredient[3]}")
        
        elif choice == "5":
            customer_name = input("Customer Name: ")
            flavor_suggestion = input("Flavor Suggestion: ")
            allergy_concerns = input("Allergy Concerns: ")
            add_customer_feedback(customer_name, flavor_suggestion, allergy_concerns)
            print("Customer feedback recorded.")
        
        elif choice == "6":
            feedback = view_customer_feedback()
            print("\nCustomer Feedback:")
            for fb in feedback:
                print(f"ID: {fb[0]}, Name: {fb[1]}, Suggestion: {fb[2]}, Allergy Concerns: {fb[3]}")
        
        elif choice == "7":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()