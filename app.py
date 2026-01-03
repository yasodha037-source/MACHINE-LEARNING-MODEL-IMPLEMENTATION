from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        msg = request.form["message"]

        data = vectorizer.transform([msg])
        prediction = model.predict(data)

        if prediction[0] == 1:
            result = "SPAM MESSAGE ❌"
        else:
            result = "NOT SPAM (HAM) ✅"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
