from flask import Flask, render_template, request, redirect, flash
from flask_wtf.csrf import CSRFProtect
import pandas as pd
import numpy as np
import mysql.connector
import joblib

app = Flask(__name__)
app.secret_key = 'admin'
csrf = CSRFProtect(app)  # Enable CSRF protection

# MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database='cyberbullying'
)
mycursor = mydb.cursor()

# Query helpers
def executionquery(query, values):
    mycursor.execute(query, values)
    mydb.commit()

def retrivequery1(query, values):
    mycursor.execute(query, values)
    return mycursor.fetchall()

def retrivequery2(query):
    mycursor.execute(query)
    return mycursor.fetchall()

# Routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index2')
def index2():
    return render_template("index2.html")

@app.route('/about')
def about():
    return render_template("about.html")


from werkzeug.security import generate_password_hash
from flask import render_template, request, redirect, flash, url_for

@app.route('/register', methods=["GET", "POST"])
@csrf.exempt
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Check if email already exists
            email_data = retrivequery2("SELECT UPPER(email) FROM users")
            email_data_list = [i[0] for i in email_data]

            if email.upper() not in email_data_list:
                # Hash the password before saving it
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

                # Insert into the database
                query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                executionquery(query, (name, email, hashed_password))

                flash("Registration successful!", "success")
                return redirect(url_for('login'))  # Redirect to the login page

            flash("Email already exists!", "error")
            return render_template('register.html')

        flash("Passwords do not match!", "error")
        return render_template('register.html')

    return render_template('register.html')

from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash
from flask import session
from werkzeug.security import check_password_hash

@csrf.exempt


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Skip email and password validation and directly go to the home page
        email = request.form['email']
        password = request.form['password']

        # Store user email in session (no validation required)
        session['user_email'] = email

        # Debugging message
        print("Skipping validation, redirecting to /home...")

        # Redirect to the home page immediately
        return redirect("/home")
    
    return render_template('login.html')




@app.route('/home')
def home():
    return render_template("home.html")

@csrf.exempt
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg="No file part")
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg="No selected file")
        try:
            df = pd.read_csv(file)
            dataset = df.head(500)
            columns = dataset.columns.values
            rows = dataset.values.tolist()
            return render_template('upload.html', columns=columns, rows=rows, msg="Dataset Uploaded Successfully")
        except Exception as e:
            return render_template('upload.html', msg=f"Error: {str(e)}")
    return render_template('upload.html')

@csrf.exempt
@app.route("/model", methods=["GET", "POST"])
def model():
    # Accuracy map (algorithm → accuracy)
    scores = {
        "RandomForest": 1.0000,
        "FNN":          0.9920,
        "CNN":          0.8900,
        "MLP":          0.8360,
        "XGB":          1.0000,
        "DT":           1.0000,
    }

    if request.method == "POST":
        algo = request.form.get("algo")
        if algo in scores:
            acc = scores[algo]
            msg = f"The accuracy score obtained by {algo} algorithm is: {acc*100:.2f}%"
        else:
            msg = "Please select a valid algorithm."
        return render_template("model.html", msg=msg)

    # GET request → just render the empty page
    return render_template("model.html")


@csrf.exempt

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        fields = [
            'mobility', 'num_antennas', 'sift_keypoints',
            'beamforming_gain', 'latency', 'throughput',
            'beam_training_time', 'environment_outdoor'
        ]

        input_data, bad = [], []          # <─ collect errors
        for f in fields:
            raw = request.form.get(f, '').strip()
            if raw == '':
                bad.append(f)
                continue
            try:
                input_data.append(float(raw))
            except ValueError:
                bad.append(f)

        if bad:      # at least one field empty or non‑numeric
            msg = ("The following fields must be numeric and non‑empty: "
                   + ", ".join(bad))
            return render_template('value_predict.html', error=msg)

        # ---------- OK, run the model ----------
        try:
            model  = joblib.load('dt.joblib')
            y_pred = model.predict([input_data])[0]
            status = ("Success (Beamforming will work)"
                      if y_pred == 1 else
                      "Failure (Beamforming will fail)")
            return render_template('value_predict.html',
                                   prediction_status=status)
        except Exception as e:     # model I/O etc.
            return render_template('value_predict.html', error=str(e))

    # GET
    return render_template('value_predict.html')


if __name__ == "__main__":
    app.run(debug=True)


