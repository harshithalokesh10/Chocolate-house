Chocolate House Management System
This is a web application for managing a fictional chocolate house. It is built using Flask, SQLite, and a simple frontend with HTML, CSS, and Jinja templates. The application allows the management of:
Seasonal chocolate flavor offerings
Ingredient inventory
Customer flavor suggestions and allergy concerns
Table of Contents
Features:
Installation
Running the Application
Testing
SQL Queries and ORM Implementation
Docker Setup
Documentation and Code Comments
Project Features:
Display seasonal flavors available for chocolates.
Manage ingredient inventory with current stock.
Allow customers to submit flavor suggestions and report allergy concerns.
Simple and intuitive user interface.
Prerequisites:
Python 3.8+
Flask
SQLite
Docker (for Docker-based setup)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/harshithalokesh10/chocolate-house.git
cd chocolate-house

From here every command should be given in terminal:

Create a virtual environment:

bash
to create a local environment Copy code:
'python -m venv myenv'
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

Start the Flask application:
bash
Copy code:
'flask run'
and then copy code 'python app.py' to run application:
Access the application: Open your web browser and go to http://127.0.0.1:5000.

Testing
Here are the test cases to validate the application:

Test Steps
Seasonal Flavors Page

Navigate to the Seasonal Flavors page from the homepage:
Verify that the page displays a list of available seasonal flavors.
Test adding a new flavor through a POST request if using a form.
Ingredient Inventory Page

Go to the Ingredients page:
Verify the list of ingredients.
Test the "Add Ingredient" feature and validate the new ingredient appears on the list.

Customer Feedback Page:
Enter a flavor suggestion or allergy concern.
Check that the new feedback entry is stored and displayed correctly.
Error Testing

Test submitting empty forms to verify form validation errors.

