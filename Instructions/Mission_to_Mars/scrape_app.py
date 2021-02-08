#import dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd

def init_browser():
    executable_path = {'executable_path':'C:/Users/ninam/Downloads/chromedriver_win32/chromedriver'}
    browser = Browser("chrome",**executable_path, headless = False)

def scrape():
    browser = init_browser()
    #path and code for news URL (most recent news title and paragraph)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    soup = bs(response.text, 'lxml')
    titles = soup.find('div',class_ = "content_title").text
    paragraph = soup.find('div', class_= "rollover_description_inner").text

    url2 = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url2)

base_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space"
