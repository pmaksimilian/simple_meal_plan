from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        sex = request.form.get("sex")
        weight = int(request.form.get("weight"))
        height = int(request.form.get("height"))
        age = int(request.form.get("age"))
        activity = float(request.form.get("activity"))
        goals = int(request.form.get("goals"))

        # gets data from form and calculate results using the Mufflin equation

        if sex == "male":
            resting_energy_expenditure = (10 * weight) + (6.25 * height) - (5 * age) + 5
            total_energy_expenditure = resting_energy_expenditure * activity
        else:
            resting_energy_expenditure = (10 * weight) + (6.25 * height) - (5 * age) - 161
            total_energy_expenditure = resting_energy_expenditure * activity

        calorie_intake = int(total_energy_expenditure)

        if goals == 2:
            calorie_intake -= 500
        elif goals == 3:
            calorie_intake -= 1000
        elif goals == 4:
            calorie_intake += 500
        elif goals == 5:
            calorie_intake += 1000

        breakfast = {
            "oatmeal": 40,
            "yogurt": 50,
            "almonds": 5,
            "whey": 15
        }
        brunch = {
            "eggs": 2,
            "wholemeal bread": 40
        }
        lunch = {
            "chicken breast": 120,
            "rice": 35
        }
        dinner = {
            "salmon": 90,
            "potato": 110
        }

        def mealplan_calculator(calories, meal):
            calorie_index = calories / 1000

            for food in meal:
                meal[food] *= calorie_index
                meal[food] = int(round(meal[food]))
            return meal

        breakfast = mealplan_calculator(calorie_intake, breakfast)
        brunch = mealplan_calculator(calorie_intake, brunch)
        lunch = mealplan_calculator(calorie_intake, lunch)
        dinner = mealplan_calculator(calorie_intake, dinner)

        def macro_calculator(calories):
            carbs = int((0.40 * calories) / 4)
            proteins = int((0.35 * calories) / 4)
            fats = int((0.25 * calories) / 9)
            macros = {
                "carbs": carbs,
                "proteins": proteins,
                "fats": fats
            }
            return macros

        macros = macro_calculator(calorie_intake)

        return render_template("index.html", calorie_intake=calorie_intake, macros=macros, weight=weight,
                               breakfast=breakfast, brunch=brunch, lunch=lunch, dinner=dinner)


if __name__ == '__main__':
    app.run(debug=True)
