# ELA Analysis

## Overview
ELA Analysis is a web application that performs Error Level Analysis (ELA) on images to detect potential manipulations. Users can upload JPEG images, and the application will generate an ELA result image that highlights areas of the image that may have been altered.

## Project Structure
```
ELA-Analysis
├── templates
│   └── index.html          # HTML structure for the web application
├── static
│   └── results             # Directory for storing ELA result images
├── uploads                 # Directory for temporarily storing uploaded images
├── app.py                  # Main application script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Requirements
To run this project, you need to have Python installed on your machine. Additionally, you will need to install the required Python packages listed in `requirements.txt`.

## Installation
1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd ELA-Analysis
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the form to upload a JPEG image and specify the quality for ELA analysis.

4. After uploading, the original image and the ELA result will be displayed on the page.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.