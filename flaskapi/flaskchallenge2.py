#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

#accept posted json
@app.route('/post', methods=['POST'])
def post():
    if request.json:
        data=request.json
        if data['age'] == '34':
            return redirect('/correct')
    else:
        return "wrong"

#landing point
@app.route("/")
def start():
    return render_template("postmaker2.html")

@app.route("/ageme", methods=['POST'])
def ageme():
    if request.form.get('age'):
        age = request.form.get('age')
        if str(age) == '34':
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("start"))
    else:
        return redirect(url_for("start"))

@app.route('/correct')
def correct():
    return "Ding Ding Ding Correct!"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

