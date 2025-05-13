# ELA Analysis Tool

This is a Flask-based web application for performing **Error Level Analysis (ELA)** on JPEG images. ELA is a technique used to detect potential manipulations in images by analyzing compression artifacts.

## Features
- Upload JPEG images for analysis.
- Specify the quality level for ELA.
- View the original image and the ELA result side by side.

## Demo
![Screenshot](static/demo.png) *(Add a screenshot of your app here)*

---

## Installation and Setup

Follow these steps to set up and run the application on your local machine:

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)

### 1. Clone the Repository

git clone https://github.com/dbugom/ELA-Analysis.git
cd ELA-Analysis

### 2. Create a virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows


### 3. Install Dependensies

pip install -r requirements.txt

### 4. Run the application
python app.py

The application will start on:

http://127.0.0.1:5000. Open this URL in your browser

Usage:

1-Open the Application in your browser.
2-Upload a JPEG image using form.
3-Specify the quality level (default is:95) (I recommend to go 75)
4-Click "Upload and Analyze" to generate the ELA result.
5-View the Original and ELA result images on the page.


