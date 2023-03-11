import requests
import os
from bs4 import BeautifulSoup

import sys
import pdb

from termcolor import colored

try:
    args = sys.argv[1]
except IndexError:
    args = None

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file_location = os.path.join(script_dir, "important.txt")
important_reports = []
with open(file_location, 'r') as f:
    lines = f.readlines()
    important_reports = [line.strip() for line in lines]

# Define the URL to scrape
url = 'https://www.marketwatch.com/economy-politics/calendar'

# Send a GET request to the URL
response = requests.get(url)

# Use Beautiful Soup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the economic calendar data
table = soup.find('table')

# Extract the table headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Extract the table rows
rows = []
for tr in table.find_all('tr')[1:]:
    row = {}
    for i, td in enumerate(tr.find_all('td')):
        row[headers[i]] = td.text.strip()
    rows.append(row)

# Print the table data
if not args:
    for i, row in enumerate(rows):
        if row["Report"] == "":
            print(row['Time (ET)'])
        else:
            if row['Report'] in important_reports or "Fed Chairman" in row['Report']:
                print(colored(f"{i}    ** {row['Time (ET)']} {row['Report']}", 'red'))
            else:
                print(f"{i}    {row['Time (ET)']} {row['Report']}")
else:
    report = rows[int(args)]["Report"]
    #pdb.set_trace()
    with open("definitions.txt", 'r') as f:
        show = False
        for i, line in enumerate(f.readlines()):
            #print(report)
            #print(line.lower())
            #print(report in line.lower())
            if report in line and "START" in line:
                show = True
            if report in line and "END" in line:
                show = False
            if show:
                print(line)

        #{'Time (ET)': '9:45 am', 'Report': 'S&P flash U.S. services PMI', 'Period': 'Feb.', 'Actual': '50.5', 'Median Forecast': '--', 'Previous': '46.8'}


