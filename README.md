# GSU Health Food Tracker

This is a Flask-based web application designed for tracking nutritional intake. Users can log their food consumption, view nutritional information, and track their daily intake of proteins, carbohydrates, fats, and calories.

## Getting Started

To set up and run the application, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kaLeidoscop3/dbProject.git
   cd your-repository
   ```

2. **Create and Activate a Virtual Environment:**

   For Windows (Powershell):

   ```bash
   deactivate
   Remove-Item -Recurse -Force .\env
   python -m venv env
   .\env\Scripts\Activate
   ```

3. **Install Required Packages:**

   ```bash
   pip install flask-sqlalchemy
   pip install python-dotenv
   pip install matplotlib
   pip install python-dotenv
   ```

4. **Run the Application:**

   ```bash
   flask run
   ```

5. **Access the Database:**

   To view the tables in the SQLite database:

   ```bash
   cd .\foodtracker\
   sqlite3 db.sqlite3
   .tables
   ```

6. **Accessing the Application:**

   Open your web browser and go to `http://localhost:5000` to access the application.

## Overview

- **Technology Stack:**
  - Flask - Python web framework
  - SQLite - Database
  - Matplotlib - Python plotting library

- **Features:**
  - Log food items with nutritional information.
  - View nutritional statistics and track daily intake.
  - Categorize food items into breakfast, lunch, dinner, dessert, candies, and drinks.
