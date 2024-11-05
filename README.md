Chocolate House Management System
This is a web application for managing a fictional chocolate house. It is built using Flask, SQLite, and a simple frontend with HTML, CSS, and Jinja templates. The application allows the management of:

Seasonal chocolate flavor offerings
Ingredient inventory
Customer flavor suggestions and allergy concerns
Table of Contents
Features
Installation
Running the Application
Testing
SQL Queries and ORM Implementation
Docker Setup
Documentation and Code Comments
Features
Display seasonal flavors available for chocolates.
Manage ingredient inventory with current stock.
Allow customers to submit flavor suggestions and report allergy concerns.
Simple and intuitive user interface.
Prerequisites
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
Create a virtual environment:

bash
Copy code
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
flask shell
>>> from app import init_db
>>> init_db()
>>> exit()
Running the Application
Start the Flask application:

bash
Copy code
flask run
Access the application: Open your web browser and go to http://127.0.0.1:5000.

Testing
Here are the test cases to validate the application:

Test Steps
Seasonal Flavors Page

Navigate to the Seasonal Flavors page from the homepage.
Verify that the page displays a list of available seasonal flavors.
Test adding a new flavor through a POST request if using a form (this may require adding functionality in the app if not available).
Ingredient Inventory Page

Go to the Ingredients page.
Verify the list of ingredients with their current stock levels.
Test the "Add Ingredient" feature and validate the new ingredient appears on the list.
Customer Feedback Page

Visit the Feedback page.
Enter a flavor suggestion or allergy concern.
Check that the new feedback entry is stored and displayed correctly.
Error Testing

Test submitting empty forms to verify form validation errors.
Access non-existent routes to ensure 404 pages are shown.
Example Unit Test Code
To automate tests, you can create a test_app.py file in the project directory and write tests using pytest:

python
Copy code
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_flavors_page(client):
    response = client.get('/flavors')
    assert response.status_code == 200
Run the tests with:

bash
Copy code
pytest
SQL Queries and ORM Implementation
Database Schema
The schema has three tables: flavors, ingredients, and feedback. Here’s an example SQL structure:

sql
Copy code
CREATE TABLE flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock INTEGER
);

CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_suggestion TEXT,
    allergy_concern TEXT
);
Example ORM (SQLAlchemy) Implementation
python
Copy code
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_suggestion = db.Column(db.String(255))
    allergy_concern = db.Column(db.String(255))
Docker Setup
Create a Dockerfile in the root of your project:

dockerfile
Copy code
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
Build the Docker image:

bash
Copy code
docker build -t chocolate-house .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 chocolate-house
Access the application:
Open your browser and go to http://localhost:5000.

Documentation and Code Comments
Each function and important code block in the app is documented with inline comments for readability. Example:

python
Copy code
# Route for the home page
@app.route('/')
def index():
    """Render the homepage with navigation links to other sections."""
    return render_template('index.html')
Refer to the codebase for further comments that explain the purpose and functionality of each section.
