# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import datetime
import time

for x in range (0,100):  
    # specify the url
    quote_page = 'https://www.timeanddate.com/worldclock/usa/cincinnati'

    # query the website and return the html to the variable page
    page = urlopen(quote_page)
      
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    
    #Find item you are looking for
    name_box = soup.find('span', {'id': 'ct'})
    
    name = name_box.text.strip() # strip() is used to remove starting and trailing spaces
    print(name)
    
    # open a csv file with append, so old data will not be erased
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, datetime.datetime.now()])
    time.sleep(3.7)
