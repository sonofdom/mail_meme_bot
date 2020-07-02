import os
import sys
import requests
from requests_html import *

url = "http://memedroid.com"

def url_to_text(url):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text

def parse_and_extract(url):

    html_text = url_to_text(url)
    r_html = HTML(html=html_text)
    links = []
    #finds all elements in class img-responsive
    img_line = r_html.find(".img-responsive")
    #removes logos of the page
    for x in range(0,3):
        img_line.remove(img_line[x])
    #print(img_line)
    #gets it to <img src ......>
    for x in range(len(img_line)):
        img_source = (img_line[x].html)
        #seperates the element and removes all parts apart from link
        link = img_source.split(" ")[1][5:-1:]
        #Special thanks to Luke + James for the previous line
        if link.startswith('https://'):
            links.append(link)
            #print(link)
    #print(links)
    return links

def add_to_file(links):
    with open("memeUrl.txt", "a") as f:
        for i in links:
            i = (i +"\n") 
            f.write(i)
            print("URL added")

def main():
    links = parse_and_extract(url)
    add_to_file(links)

if __name__ == "__main__":
    main()