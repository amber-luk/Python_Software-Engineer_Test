import json
import logging
from flask import flash, jsonify, render_template

from app import app
from app.forms import InputNumbers


# define total route hardcoded 
@app.route("/total", methods=['GET', 'POST'])
def total():
    numbers_to_add=list(range(10000001))
    sum_of_numbers = sum(numbers_to_add)
    return jsonify({
        "total": sum_of_numbers
    })

# total route with user input
@app.route("/total2", methods=['GET', 'POST'])
def total2():
    form = InputNumbers()
    if form.validate_on_submit():
        numbers_to_add = form.numbers_to_add.data.split(",")

        sum_of_numbers = []
        for i in numbers_to_add:
            try:
                sum_of_numbers.append(int(i))
            except ValueError as e:
                logging.error(str(e))

        return jsonify({
            "total": sum(sum_of_numbers)
        })
    else:
        return render_template("InputNumbersForm.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)