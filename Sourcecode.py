#PROJECT SOURCE CODE FOR DEFORESTATION IN INDIA....!

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  # Imported The libraries for Data Analytics


def fun_label():  # Defining the fuction
    plt.title("Deforestation Graph of India")  # Title of Graph
    plt.ylabel("Area in Hecters")  # Label for Y-axis
    print(plt.show())  # Ploting the graph


# Program For Bar Graph
# It is used to read the excel file from the given location
var = pd.read_excel("E:/Raj programming/Data Analytics/STATE DATA.xlsx")
# Head is the function of Pandas used to print the first 5 lines of sheet
print("Printing the first 5 lines of Table :")
print(var.head())
# Tail is the function of Pandas used to print the last 5 lines of sheet
print("\nPrinting the Last 5 lines of Table :")
print(var.tail())
# Here Matplotlib is used to print the bar graph for Deforestation in [2001-05]
print(var.plot(x='State', y='(2001-05)', kind='bar', figsize=(10, 10)))
plt.xlabel("Deforestation in [2001-05]")  # Label for X-axis
fun_label()
# Here Matplotlib is used to print the bar graph for Deforestation in [2006-10]
print(var.plot(x='State', y='(2006-10)', kind='bar', figsize=(10, 10)))
plt.xlabel("Deforestation in [2006-10]")  # Label for X-axis
fun_label()
# Here Matplotlib is used to print the bar graph for Deforestation in [2011-15]
print(var.plot(x='State', y='(2011-15)', kind='bar', figsize=(10, 10)))
plt.xlabel("Deforestation in [2011-15]")  # Label for X-axis
fun_label()
# Here Matplotlib is used to print the bar graph for Deforestation in  [2016-21]
print(var.plot(x='State', y='(2016-21)', kind='bar', figsize=(10, 10)))
plt.xlabel("Deforestation in [2016-21]")  # Label for X-axis
fun_label()
# Here Matplotlib is used to print the bar graph for total Deforestation Untill 2021
print(var.plot(x='State', y='Total', kind='bar', figsize=(10, 10)))
plt.xlabel("Total Deforestation Untill 2021")  # Label for X-axis
fun_label()
