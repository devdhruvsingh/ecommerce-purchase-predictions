# E-Commerce Purchase Prediction

A machine learning powered web application that predicts whether an e-commerce visitor is likely to make a purchase based on their browsing and session behavior.

## 🌐 Live Website

**[E-Commerce Purchase Prediction](https://ecommerce-purchase-prediction.onrender.com)**

The website allows users to enter visitor information and receive:

* Purchase prediction
* Purchase probability

## ✨ Features

* Clean and interactive user interface
* E-commerce visitor behavior analysis
* Machine learning based purchase prediction
* Purchase probability estimation
* Input validation
* Responsive frontend
* Real-time prediction results

## 🖥️ Website

The frontend is built using:

* HTML
* CSS
* JavaScript

Users enter information such as:

* Administrative page visits
* Informational page visits
* Product-related page visits
* Time spent on pages
* Bounce rate
* Exit rate
* Page values
* Visitor type
* Traffic type
* Month
* Weekend activity
* Session engagement metrics

The submitted information is processed by the machine learning application and the prediction is displayed directly on the website.

## 🧠 Machine Learning

The application uses the **Online Shoppers Purchasing Intention Dataset** to predict whether a visitor will make a purchase.

Additional behavioral features were created, including:

* Total Pages
* Total Duration
* Average Time Per Page
* Product Engagement Ratio
* Product Time Ratio

## 📁 Project Structure

```text
ecommerce-pruchase-prediction/
│
├── data/
├── database/
├── models/
├── notebooks/
├── reports/
├── sql/
├── tableau/
│
├── src/
│   ├── api/
│   └── frontend/
│       ├── index.html
│       ├── style.css
│       └── script.js
│
├── tests/
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/devdhruvsingh/ecommerce-pruchase-prediction.git
```

Move into the project:

```bash
cd ecommerce-pruchase-prediction
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

The frontend can then be opened using **VS Code Live Server**.

## 🛠️ Technologies

* HTML5
* CSS3
* JavaScript
* Python
* Flask
* Pandas
* Scikit-learn
* SQL
* SQLite
* Tableau
* Git & GitHub
* Render

## 👨‍💻 Author

**Dhruv Singh**

GitHub: https://github.com/devdhruvsingh

## ⭐ Project

If you find this project interesting, consider giving the repository a star.
