from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", highlights=[
        "State-of-the-art Equipment", "Professional Trainers", "Group Classes"
    ])

@app.route('/about')
def about():
    return render_template("about.html", 
        mission="Our mission is to help everyone achieve their fitness goals in a healthy and motivating environment.",
        team=["John Doe - Trainer", "Jane Smith - Nutritionist", "Mike Johnson - Manager"]
    )

@app.route('/membership')
def membership():
    return render_template("membership.html", plans=[
        {"name": "Basic Plan", "price": "$30/month"},
        {"name": "Standard Plan", "price": "$50/month"},
        {"name": "Premium Plan", "price": "$70/month"}
    ])

if __name__ == '__main__':
    app.run(debug=True)
