from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

import matplotlib.pyplot as plt
import numpy
import pandas as pd

service = Service(executable_path='/usr/bin/geckodriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

#URL = "/home/thesynthax/projects/python/bakchodi/index.html"
URL = "http://localhost:8000"
driver.get(URL)

total = 0;

tables = []
tableTags = driver.find_elements(By.TAG_NAME, "table")
tbodyTags = []
for i in range(len(tableTags)):
    tbodyTags.append(tableTags[i].find_element(By.XPATH, "*"))

trs = []
for tbodyTag in tbodyTags:
    children = tbodyTag.find_elements(By.XPATH, "*")
    for child in children:
        trs.append(child)

numbers = []
for tr in trs:
    children = tr.find_elements(By.XPATH, "*")
    numbers.append(children[1])

numbers_float = []
for i in range(1, len(numbers)):
    if "ABSENT" in numbers[i].text:
        numbers_float.append(0)
        total += 0
    else:
        numbers_float.append(float(numbers[i].text))
        total += float(numbers[i].text)

mean = total/len(numbers_float)
print("mean =", mean)

median = numpy.median(numbers_float)
print("median = ", median)

sorted = numpy.sort(numbers_float)

x = pd.DataFrame(sorted)
x.columns = ['marks']
count = x['marks'].value_counts()
print(count)
x.marks.value_counts()[x.marks.unique()].plot(kind="bar")
#plt.subplots(figsize=(10,7))
#plt.bar(sorted, height=50)
plt.show()
