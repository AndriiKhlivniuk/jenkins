import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Browser, BrowserType
import requests

@pytest.fixture
def duck_start(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.duckduckgo.com')
    yield page

def test_duck_response(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    response = page.request.get('https://www.duckduckgo.com')
    expect(response).to_be_ok()

def test_bitcoin_wikipedia_title(duck_start):
    page = duck_start
    page.fill('#search_form_input_homepage', 'bitcoin price')
    #click search
    page.click('#search_button_homepage')
    assert page.title()== "bitcoin price at DuckDuckGo"

def test_bitcoin_wikipedia(duck_start):
    page = duck_start
    page.fill('#search_form_input_homepage', 'bitcoin wikipedia')
    #click search
    page.click('#search_button_homepage')
    page.click('//span[normalize-space()="Bitcoin - Wikipedia"]')
    main_title = page.locator("//span[@class='mw-page-title-main']").inner_text()
    assert main_title == "Etherium"


