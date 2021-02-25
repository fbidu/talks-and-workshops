from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route("/age", methods=["POST"])
def age():
    birthday = request.form["birth"]

    print(f"Recebi a data de aniversário {birthday}")

    age = datetime.today() - datetime.strptime(birthday, "%Y-%m-%d")
    age = age.days // 365
    print(age)
    return f"Você tem {age} anos!"


if __name__ == "__main__":
    app.run(debug=True)