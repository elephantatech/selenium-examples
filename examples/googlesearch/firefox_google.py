#!/usr/bin/env python3
"""This script will allow you to search on google
using firefox browser.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def search_apples():
    """This function will open google.com on firefox,
    then search for Apples"""
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    assert "Google" in driver.title 
    # if the window loaded title is Google then continue below
    query_element = driver.find_element_by_name('q')
    query_element.send_keys("Apples")
    query_element.submit()
    sleep(10)
    driver.close()

def search_google(search_term):
    """This function will open google.com on firefox,
    then search for anything on google"""
    with webdriver.Firefox() as driver:
        driver.get("https://www.google.com")
        assert "Google" in driver.title 
        # if the window loaded title is Google then continue below
        query_element = driver.find_element_by_name('q')
        query_element.send_keys(search_term)
        query_element.submit()
        sleep(10)
        

if __name__ == "__main__":
    search_google("Pineapples")