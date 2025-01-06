from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pymongo
import requests
# import os
# from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

def run_selenium_script():
    # service = Service(chromedriver_path)
    driver = webdriver.Chrome()
    driver.get("https://x.com/i/flow/login")
    sleep(3)

    # Login process
    username = driver.find_element(By.XPATH, "//input[@name='text']")
    username.send_keys("tester16_")
    sleep(2)
    next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
    next_button.click()
    sleep(5)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("Tester@1234")
    login_button = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
    login_button.click()
    sleep(10)

    # Scrape trending topics
    try:
        trending_section = driver.find_element(By.XPATH, "//div[@aria-label='Timeline: Trending now']")
        trending_items = trending_section.find_elements(By.XPATH, ".//div[@role='link']//span[contains(@class, 'r-poiln3')]")
    except:
        trending_items = []

    trend_names = [item.text for item in trending_items if item.text.strip() != '']
    driver.close()

    ip = requests.get('https://httpbin.org/ip').json()['origin']
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return trend_names, ip, date

@app.route('/run-script', methods=['GET'])
def run_script():
    trends, ip, date = run_selenium_script()
    unique_id = str(datetime.now().timestamp())

    # Connect to MongoDB and insert data
    try:
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = mongo_client["trending_db"]
        collection = db["trends"]
        collection.insert_one({
            "_id": unique_id,
            "trends": trends,
            "ip": ip,
            "date": date
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        mongo_client.close()

    return jsonify({"trends": trends, "ip": ip, "date": date})

if __name__ == '__main__':
    app.run(debug=True)

