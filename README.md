# Simple Meal Plan Calculator

A small Flask web application that calculates daily calorie needs and generates a simple meal plan based on user input.

The app uses the Mifflin-St Jeor equation to estimate calorie requirements, adjusts them by activity level and fitness goal, and displays estimated macronutrients (carbs, protein, fats).

This is a lightweight educational project with no database and no external services.

## Features

- Calculate daily calorie intake
- Adjust calories based on fitness goals
- Estimate macronutrient distribution
- Generate a simple meal plan
- Single-page form-based UI
- No external services or database required

## Tech Stack

- Python 3
- Flask
- HTML templates (Jinja2)
- Basic CSS (static files)

## How to run the app

1. Make sure Python 3 is installed

On Ubuntu / Pop!_OS you may need:
sudo apt install python3 python3-venv

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -U pip
pip install Flask>=2.3,<3.0 gunicorn

4. Run the application

python main.py

5. Open the app in your browser

http://127.0.0.1:5000
