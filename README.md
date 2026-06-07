# Federated Learning for 6G Link-Quality Prediction

A Flask-based web application that predicts 6G beamforming link quality using machine learning models. The system allows users to upload datasets, evaluate model performance, and perform real-time link-quality predictions through an interactive web interface.

---

## 🚀 Features

- User Registration and Login System
- Dataset Upload and Visualization
- Machine Learning Model Comparison
- Real-Time 6G Link-Quality Prediction
- Beamforming Success/Failure Analysis
- MySQL Database Integration
- Password Hashing and Security
- Responsive Web Interface

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-WTF
- MySQL Connector

### Machine Learning
- Scikit-Learn
- Joblib
- Decision Tree
- Random Forest
- XGBoost
- CNN
- FNN
- MLP

### Database
- MySQL

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

---

## 📂 Project Structure

```text
Federated-Learning-For-6G/
│
├── app.py
├── dt.joblib
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── upload.html
│   ├── model.html
│   └── value_predict.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── dataset/
    └── dataset.csv
```

---

## 📊 Input Features

The prediction model uses the following network parameters:

| Feature | Description |
|----------|------------|
| Mobility | User mobility speed (m/s) |
| Number of Antennas | Total antennas available |
| SIFT Keypoints | Feature extraction points |
| Beamforming Gain | Signal gain (dB) |
| Latency | Network latency (ms) |
| Throughput | Data rate (Mbps) |
| Beam Training Time | Beam alignment duration |
| Environment Outdoor | 1 = Outdoor, 0 = Indoor |

---

## 📈 Model Performance

| Algorithm | Accuracy |
|------------|----------|
| Random Forest | 100.00% |
| XGBoost | 100.00% |
| Decision Tree | 100.00% |
| FNN | 99.20% |
| CNN | 89.00% |
| MLP | 83.60% |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Federated-Learning-For-6G.git
cd Federated-Learning-For-6G
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

```txt
Flask
Flask-WTF
Flask-Bcrypt
Werkzeug
pandas
numpy
mysql-connector-python
joblib
scikit-learn
```

---

## 🗄️ Database Setup

Create a MySQL database:

```sql
CREATE DATABASE cyberbullying;
```

Create users table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password TEXT
);
```

Update database credentials in `app.py`:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database="cyberbullying"
)
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🔍 Application Workflow

1. Register a new account.
2. Login to the system.
3. Upload a CSV dataset.
4. View dataset preview.
5. Compare machine learning models.
6. Enter network parameters.
7. Predict beamforming success or failure.

---

## 🎯 Prediction Output

### Success

```text
Success (Beamforming will work)
```

### Failure

```text
Failure (Beamforming will fail)
```

---

## 🔮 Future Enhancements

- TensorFlow Federated Integration
- Real-Time 6G Network Monitoring
- Federated Edge Learning
- Explainable AI Dashboard
- Cloud Deployment
- Automated Model Retraining

---

## ❗ Troubleshooting

### No module named 'sklearn'

Install Scikit-Learn:

```bash
pip install scikit-learn
```

### MySQL Connection Error

Verify:
- MySQL Server is running
- Database exists
- Correct username/password
- Port 3306 is available

---

## 📚 Research Domain

This project focuses on:

- 6G Wireless Networks
- Federated Learning
- Machine Learning for Communications
- Beamforming Optimization
- Intelligent Network Management

---

## 👨‍💻 Author

**Munna**

Federated Learning for 6G Link-Quality Prediction

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
