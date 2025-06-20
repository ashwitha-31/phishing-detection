from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

# Dummy training data
X = np.array([[0], [1]])
y = np.array([0, 1])  # 0 = Safe, 1 = Phishing

# Train the model directly
model = RandomForestClassifier()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        # Very basic logic for demonstration
        feature = [[1 if "http" in url else 0]]
        prediction = model.predict(feature)[0]
        result = "Phishing Website 🚨" if prediction == 1 else "Safe Website ✅"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
