import pandas as pd
import matplotlib.pyplot as plt

def set_common_plot_settings(title):
    plt.title(title)
    plt.ylabel("Area in Hectares")
    plt.show()

def plot_deforestation(var, column_name, title):
    plt.figure(figsize=(10, 10))
    var.plot(x='State', y=column_name, kind='bar')
    plt.xlabel(column_name)
    set_common_plot_settings(title)

def main():
    var = pd.read_excel("E:/Raj programming/Data Analytics/STATE DATA.xlsx")

    print("Printing the first 5 lines of Table:")
    print(var.head())

    print("\nPrinting the Last 5 lines of Table:")
    print(var.tail())

    plot_deforestation(var, '(2001-05)', "Deforestation in [2001-05]")
    plot_deforestation(var, '(2006-10)', "Deforestation in [2006-10]")
    plot_deforestation(var, '(2011-15)', "Deforestation in [2011-15]")
    plot_deforestation(var, '(2016-21)', "Deforestation in [2016-21]")
    plot_deforestation(var, 'Total', "Total Deforestation Until 2021")

if __name__ == "__main__":
    main()
