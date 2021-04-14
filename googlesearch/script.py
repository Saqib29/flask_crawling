from flask import Blueprint, render_template, request, flash, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


goog = Blueprint("script", __name__, template_folder="templates")

@goog.route("/search")
def search():
    return render_template("index.html")


@goog.route("/result", methods=['POST'])
def getResult():
    search = request.form['s']

    if len(search) == 0:
        flash("please type for search.")
        return render_template("index.html")

    chromedriver = "/home/saqib/work/selenium/chromedriver/chromedriver"
    driver = webdriver.Chrome(chromedriver)

    driver.set_page_load_timeout("10")
    driver.get("http://google.com")

    driver.find_element_by_name("q").send_keys(search)
    driver.execute_script("arguments[0].click();", driver.find_element_by_name("btnK"))

    driver.maximize_window()
    # driver.refresh()
    driver.execute_script("window.scrollTo(0,200);")


    
    results = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='g']")))


    time.sleep(4)
    # driver.quit()

    return render_template('index.html')