import requests 
import logging
from bs4 import BeautifulSoup
import json
import http 
from urllib.parse import urlparse, urljoin
import re

def external_urls(url):

  params=urlparse(url)
  domain_name = params.netloc
  scheme = params.netloc
  req = requests.get(url)
  soup = BeautifulSoup(req.text, "html.parser")
  # scrap page title
  title = soup.title.text
  print(title)
  external_urls = set()

  for a_tag in soup.findAll("a"):

      href = a_tag.attrs.get("href")

      if href == "" or href is None:
          # href empty tag
          continue
  
      # join the URL if it's relative (not absolute link)
      href = urljoin(url, href)
      parsed_href = urlparse(href)
      # remove URL GET parameters, URL fragments, etc.
      href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

      # already in the set
      if href in external_urls:
          continue

      # external link
      if domain_name in href:
          continue

      external_urls.add(href)

  for url in external_urls:
    print (url)

external_urls("https://webscraper.io")
