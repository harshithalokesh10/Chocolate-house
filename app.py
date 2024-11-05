from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connection to database
def get_db_connection():
    con = sqlite3.connect('chocolate_house.db')
    con.row_factory = sqlite3.Row  # Enables column access by name
    return con
# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Seasonal Flavors route
@app.route('/flavors', methods=['GET', 'POST'])
def flavors():
    con = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        available_until = request.form['available_until']
        con.execute('INSERT INTO SeasonalFlavors (name, description, available_until) VALUES (?, ?, ?)',
                     (name, description, available_until))
        con.commit()
        return redirect(url_for('flavors'))

    flavors = con.execute('SELECT * FROM SeasonalFlavors').fetchall()
    con.close()
    return render_template('flavors.html', flavors=flavors)

# Ingredient Inventory route
@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    con = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        con.execute('INSERT INTO IngredientInventory (name, quantity, unit) VALUES (?, ?, ?)',
                     (name, quantity, unit))
        con.commit()
        return redirect(url_for('ingredients'))

    ingredients = con.execute('SELECT * FROM IngredientInventory').fetchall()
    con.close()
    return render_template('ingredients.html', ingredients=ingredients)

# Customer Feedback route
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    con = get_db_connection()
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_suggestion = request.form['flavor_suggestion']
        allergy_concerns = request.form['allergy_concerns']
        con.execute('INSERT INTO CustomerFeedback (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)',
                     (customer_name, flavor_suggestion, allergy_concerns))
        con.commit()
        return redirect(url_for('feedback'))

    feedback = con.execute('SELECT * FROM CustomerFeedback').fetchall()
    con.close()
    return render_template('feedback.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)