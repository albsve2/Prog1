import csv
import matplotlib.pyplot as plt
from Uppg2 import smooth_a, smooth_b

def load_csv(): 
    with open('CO2Emissions_filtered.csv', 'r') as f:
        reader = csv.reader(f)
        data = {rows[1].lower() : [float(element) for element in rows[3:]]for rows in reader}
    return data

a = load_csv()
fig, ax = plt.subplots() #figur och axel skapas
time = list(range(1960, 2015)) #lista time

list_land = ['dnk', 'fin', 'isl', 'nor', 'swe']
list_color = ['blue', 'orange', 'green', 'red', 'purple']

for i in range(len(list_land)):
    land = list_land[i] #index i
    color = list_color[i]

    ax.plot(time, a[land], linestyle = ':', color = color) #punkter
    ax.plot(time, smooth_a(a[land], 5), color = color, label = land) #heldragen, label = land -> legend
    ax.plot(time, smooth_b(a[land], 5), linestyle = '--', color = color) #sträckad

ax.set(xlabel='Year', ylabel='CO2 Emissions (kt)', title='Yearly Emissions of CO2 in the Nordic Countries')
ax.plot()
ax.legend()
plt.show()
print(load_csv())
