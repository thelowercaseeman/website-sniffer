import requests

from selenium import webdriver

options = webdriver.EdgeOptions()

driver = webdriver.Edge(options=options)
driver.get("https://duckduckgo.com")