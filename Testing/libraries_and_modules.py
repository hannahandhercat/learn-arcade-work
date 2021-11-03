"""
Example using OpenPyXL to create an Excel worksheet
"""

from openpyxl import Workbook
import random

# Create an Excel workbook
work_book = Workbook()

# Grab the active worksheet
work_sheet = work_book.active

# Data can be assigned directly to cells
work_sheet['A1'] = "This is a test"

# Rows can also be appended
for i in range(200):
    work_sheet.append(["Random Number:", random.randrange(1000)])

# Save the file
work_book.save("sample.xlsx")


"""
Example showing how to read in from a web page
"""

from bs4 import BeautifulSoup
import urllib.request

# Read in the web page
url_address = "http://simpson.edu"
page = urllib.request.urlopen(url_address)

# Parse the web page
soup = BeautifulSoup(page.read(), "html.parser")

# Get a list of level 1 headings in the page
headings = soup.findAll("h1")

# Loop through each row
for heading in headings:
    print(heading.text)


"""
We LOVE plotting graphs 
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

plt.plot(x, y1, label = "Series 1")
plt.plot(x, y2, label = "Series 2")

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()