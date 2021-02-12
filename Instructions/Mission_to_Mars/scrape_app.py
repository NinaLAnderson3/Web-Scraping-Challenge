#import dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# def init_browser():
#     executable_path = {'executable_path':'C:/Users/ninam/Downloads/chromedriver_win32/chromedriver'}
#     browser = Browser("chrome",**executable_path, headless = False)

def scrape():
    mars = {}
    #Mars news website scraping
    browser = Browser('chrome')
    #path and code for news URL (most recent news title and paragraph)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')
    #this works/pulls into html site
    news_titles = soup.find('div',class_ = "content_title").text
    #this works & pulls into html site
    paragraph = soup.find('div', class_= "rollover_description_inner").text

#Code for image url scraping
    url2 = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"

    base_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space"
    browser.visit(url2)
    browser.find_link_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find('img',class_='fancybox-image').get('src')
    #this works and pulls into html site
    featured_url_link = f'{base_url}/{results}'

#Code for scraping data html_table
    mars_url = "https://space-facts.com/mars"
    data = pd.read_html(mars_url)
    mars_data = data[0]
    mars_facts = mars_data.rename(columns = {0:"Parameter",1:"Value"})
    mars_facts = mars_facts.to_html()

#Mars Hemispheres

    usg_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    usg_base = "https://astrogeology.usgs.gov"
    browser.visit(usg_url)
    soup2 = bs(browser.html, 'html.parser')

    urls = []
    for image in range(4):
        browser.find_by_css('a.product-item h3')[image].click()
        html = bs(browser.html,'html.parser')
        titleelement = html.find("h2",class_="title").get_text()
        hrefelement = html.find('a',text = "Sample").get('href')
        browser.back()
        hemi_dict = {"title":titleelement, "image_url":hrefelement}
        urls.append(hemi_dict)
    #print(urls)


    mars= {
    "news_title": news_titles,
    "paragraph": paragraph,
    "featured_image": featured_url_link,
    "fact_table" : mars_facts,
    "hemisphere_images": urls
    }


    browser.quit()
    return mars

    if __name__ == "__main__":
        scrape()
