# Project Setup and Running Guide

## 1. Ensure Dependencies Are Installed

Make sure you have Python installed on your system.

Install the dependencies using the `requirements.txt` file:

pip install -r requirements.txt

## 2. Ensure MongoDB Is Running
If you don't have MongoDB installed, you need to install and start it. Follow the instructions for your operating system to install MongoDB and start the MongoDB service.

## 3. Check ChromeDriver
Make sure chromedriver is in your project directory as shown in the structure.

## 4. Run the Flask Application
Navigate to the project directory in the terminal or command prompt.

## 5. Access the Web Application
Open your browser and go to http://127.0.0.1:5000/ or http://localhost:5000/.

You should see your HTML page with the button to run the script.

## 6. Trigger the Selenium Script
Click the button on the HTML page. This will trigger the Selenium script to run.

Once the script completes, it will display the results on the same page, showing the trending topics, the IP address used, and a JSON extract of the MongoDB record.