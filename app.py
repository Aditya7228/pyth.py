from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["operation"]

        if op == "add":
            result = num1 + num2

        elif op == "sub":
            result = num1 - num2

        elif op == "mul":
            result = num1 * num2

        elif op == "div":
            if num2 == 0:
                result = "Cannot divide by 0"
            else:
                result = num1 / num2

        elif op == "floor":
            if num2 == 0:
                result = "Cannot divide by 0"
            else:
                result = num1 // num2

        elif op == "exp":
            result = num1 ** num2

    return render_template("index.html", result=result)


import os
if __name__=="__main__":
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT",5000)))