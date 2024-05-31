# CyberHUB

![App Logo](/static/assets/icon_full.png)

An Innovative Web App for Real-Time Data Protection and Breach Prevention

## Objective and Scope

### Objectives

1. Develop a robust hash identifier.
2. Implement an email breach checker utilizing external APIs for real-time analysis.
3. Create a password breach detection system.
4. Design a secure message encryption and decryption mechanism

### Scope

1. The project focuses on providing user-friendly interfaces for hash identification, email breach
checking, password breach analysis, and message encryption/decryption.
2. Emphasis on backend processing to ensure data integrity and security.

## Installation

Clone the repository:

```bash
git clone https://github.com/spaulll/college_project.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Flask application:

```bash
python app.py
```

 Access the application in your web browser at [http://localhost:5000/](http://localhost:5000/).

## Docker Guide

Build the Docker image:

```bash
docker build -t cyberhub .
```

Run the Docker container:

```bash
docker run -e HOST_IP=host.docker.internal -p 5000:5000 cyberhub
```

## API Keys Configuration
To use the email breach checker, you need to obtain an API key from [Have I Been Pwned](https://haveibeenpwned.com/API/Key) and set it up in a .env file.

- Create a .env file in the root directory of your project and add your API key:
```
API_KEYs = your_hibp_api_key_here
```
- For multiple API Keys separate using commas
```
API_KEYs = api_key1, api_key2, api_key3
```

## API Endpoints

- `/api/email-breach`: Checks if the provided email has been involved in any data breaches.
- `/api/password-breach`: Checks if the provided password has been breached.
- `/api/hash-id`: Identifies the type of hash provided.
- `/api/massageEncode`: Encodes the provided message securely.

## Screenshots

![home](/static/img/home.png)
![securemessage](/static/img/securemessage.png)
![hashid](/static/img/hashid.png)
![passwordleak](/static/img/passwordleak.png)
![emailleak](/static/img/emailleak.png)
![help](/static/img/help.png)
