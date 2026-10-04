

🛡️ PhishGuard – Phishing Website Detector

AI/ML Based Web Application for Detecting Phishing Website


## 🚀 Live Demo
[🌐 Open PhishGuard](https://phishguard-phishing-website-detector.onrender.com)

📌 Project Overview

PhishGuard is an AI/ML-based web application designed to identify potentially phishing websites by analyzing URL characteristics and applying a trained machine learning model.

Phishing websites are designed to look like legitimate websites in order to trick users into providing sensitive information such as:

🔐 Passwords

💳 Banking information

📧 Email credentials

👤 Personal information

🔑 Login details


PhishGuard provides a simple web interface where users can enter a website URL and receive a classification indicating whether the URL appears to be legitimate or potentially phishing.


---

🎯 Objectives

The main objectives of this project are:

Detect potentially phishing URLs using Machine Learning.

Analyze different characteristics of website URLs.

Provide a simple and user-friendly web interface.

Display the prediction and confidence score.

Provide security warnings for suspicious URLs.

Maintain a detection history during the application session.

Deploy the application online so it can be accessed through a web browser.



---

✨ Features

🔍 URL Detection

Users can enter a website URL and analyze it using the trained ML model.

🤖 Machine Learning

The project uses a Random Forest Classifier trained on a phishing website dataset.

📊 Prediction

The system classifies URLs as:

✅ LEGITIMATE WEBSITE

🚨 PHISHING WEBSITE


📈 Confidence Score

The application displays the model's prediction confidence.

⚠️ Security Warning

Potentially suspicious URLs generate a warning asking users not to use the website.

🛡️ URL Risk Analysis

The application checks characteristics such as:

HTTPS usage

Suspicious words

@ symbol

IP address usage

Multiple hyphens

URL length

Domain characteristics


📜 Detection History

The dashboard displays recently analyzed URLs along with their results.

📊 Dashboard

The application displays:

Total scans

Phishing websites detected

Legitimate websites detected


🌐 Online Deployment

The application is deployed using Render and can be accessed online.


---

🧠 Machine Learning

Algorithm Used

Random Forest Classifier

PhishGuard uses the Random Forest Classification algorithm.

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make predictions.

It is suitable for this project because it can handle multiple numerical and categorical-style features and can model non-linear relationships between URL characteristics and phishing classification.


---

📚 Dataset

The project uses a phishing website dataset containing:

11,055 records

30 input features

1 target column


Target

The target column is:

Result

The dataset contains two classes:

1  → Legitimate
-1 → Phishing


---

🔎 Features Used

The model uses the following URL/security-related features:

1. having_IPhaving_IP_Address


2. URLURL_Length


3. Shortining_Service


4. having_At_Symbol


5. double_slash_redirecting


6. Prefix_Suffix


7. having_Sub_Domain


8. SSLfinal_State


9. Domain_registeration_length


10. Favicon


11. port


12. HTTPS_token


13. Request_URL


14. URL_of_Anchor


15. Links_in_tags


16. SFH


17. Submitting_to_email


18. Abnormal_URL


19. Redirect


20. on_mouseover


21. RightClick


22. popUpWidnow


23. Iframe


24. age_of_domain


25. DNSRecord


26. web_traffic


27. Page_Rank


28. Google_Index


29. Links_pointing_to_page


30. Statistical_report




---

📊 Model Performance

The Random Forest model achieved approximately:

97.42% Accuracy

on the project's test split.

> ⚠️ Note: This accuracy represents performance on the supplied dataset and test split. It should not be interpreted as a guarantee of real-world phishing detection accuracy.




---

🏗️ Project Architecture

User
                     │
                     ▼
              ┌──────────────┐
              │  Web Browser │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │    Flask     │
              │ Web Server   │
              └──────┬───────┘
                     │
                     ▼
             ┌─────────────────┐
             │ Feature         │
             │ Extraction      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Random Forest   │
             │ ML Model        │
             └────────┬────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Prediction   │
              └──────┬───────┘
                     │
              ┌──────┴──────┐
              ▼             ▼
        Legitimate       Phishing
              │             │
              └──────┬──────┘
                     ▼
              Display Result


---

📁 Project Structure

phishguard-phishing-website-detector/
│
├── dataset/
│   └── phishing dataset csv.csv
│
├── model/
│   └── phishing_model.pkl
│
├── src/
│   ├── feature_extraction.py
│   ├── load_dataset.py
│   ├── predict.py
│   ├── prepare_data.py
│   ├── project 1.py
│   └── train_model.py
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md


---

🛠️ Technologies Used

Programming Language

🐍 Python


Machine Learning

Scikit-learn

Random Forest Classifier

Pandas

NumPy

SciPy

Joblib


Web Development

Flask

HTML

CSS

JavaScript


Deployment

Render


Version Control

Git

GitHub



---

⚙️ How the System Works

Step 1 – User enters URL

The user enters a website URL into the PhishGuard interface.

Example:

https://example.com

Step 2 – URL preprocessing

The application processes the entered URL and extracts relevant characteristics.

Step 3 – Feature extraction

The URL is converted into features required by the machine learning model.

Step 4 – Machine Learning prediction

The extracted features are passed to the trained Random Forest model.

Step 5 – Risk analysis

Additional URL security indicators are checked.

Step 6 – Final result

The application displays:

LEGITIMATE WEBSITE

or

PHISHING WEBSITE

along with the confidence and security information.


---

💻 Run the Project Locally

1. Clone the repository

git clone https://github.com/uttham-dev/phishguard-phishing-website-detector.git

2. Open the project

cd phishguard-phishing-website-detector

3. Create a virtual environment

Windows

python -m venv venv

4. Activate the virtual environment

PowerShell

venv\Scripts\Activate.ps1

If PowerShell blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then:

venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

6. Run Flask

python app.py

7. Open the application

Go to:

http://127.0.0.1:5000


---

☁️ Deployment

The application is deployed using Render.

Deployment configuration

Build Command:

pip install -r requirements.txt

Start Command:

gunicorn app:app

Live Application

👉 https://phishguard-phishing-website-detector.onrender.com


---

🧪 Example Testing

Legitimate example

https://google.com

Expected:

LEGITIMATE WEBSITE

Safe suspicious-looking test URL

http://paypal-login-security-example.com

This is a non-existent test URL used only to demonstrate the application's warning interface.

Expected:

PHISHING WEBSITE


---

⚠️ Limitations

The current version has some limitations:

The model's performance depends on the training dataset.

Dataset accuracy does not guarantee real-world accuracy.

Some webpage/domain features are currently approximated during URL feature extraction.

The application should not be considered a replacement for professional cybersecurity tools.

A prediction should be treated as a security indication rather than absolute proof that a website is malicious.



---

🚀 Future Improvements

Future versions of PhishGuard can include:

🔎 Real-time domain and DNS analysis

🌐 Website content analysis

🔐 SSL certificate verification

🌍 WHOIS/domain-age analysis

📡 Real-time threat intelligence APIs

🧠 Advanced ML/DL models

📊 More detailed analytics

💾 Persistent database for scan history

👤 User authentication

📱 Mobile-friendly improvements

🔔 Security notifications

🛡️ Browser extension

📈 Advanced risk scoring



---

👨‍💻 Developer

Uttham

AI/ML Engineering Student
AJ Institute of Engineering & Technology

Interested in:

Artificial Intelligence

Machine Learning

Python

Web Development

Cybersecurity

Data Structures & Algorithms



---

📌 Project Information

Category	Details

Project Name	PhishGuard
Project Type	AI/ML Web Application
Domain	Cybersecurity
Language	Python
Framework	Flask
ML Algorithm	Random Forest
Dataset Size	11,055 records
Features	30
Accuracy	~97.42%
Deployment	Render
Version Control	GitHub



---

⭐ Support

If you find this project useful, consider giving the repository a ⭐ Star on GitHub.





---

🔗 Link

Live Demo:
https://phishguard-phishing-website-detector.onrender.com

