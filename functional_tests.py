from selenium import webdriver

browser = webdriver.Firefox()
# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'Django' in browser.title
