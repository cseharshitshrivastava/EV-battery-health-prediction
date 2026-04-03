import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("battery.csv")

plt.scatter(data['cycle'], data['capacity'])
plt.xlabel("Cycle Count")
plt.ylabel("Battery Capacity")
plt.title("Battery Degradation")
plt.show()
