import pandas as pd

df = pd.read_csv('data.csv') #loading the dataset into a pandas dataframe
print(df) #prints entire dataset into a table format

print("Dataset shape:", df.shape) #shows the number of rows and columns in this dataset respectively
print("Dataset columns:", df.columns) #shows the names of the columns in this dataset
print(df.describe()) #shows the statistical summary of this dataset
df.info()
print("Mean breaths per minute of each type of locust: ", df.mean()) 

import matplotlib.pyplot as plt #needed to plot a graph of this dataset
df.boxplot()

plt.title("Comparison of Locust Breathing Rates under hypoxic conditions")
plt.ylabel("Breaths per minute")

sl_mean = df["Sea Level Locust BPM"].mean()
tp_mean = df["Tibetan Plateau Locust BPM"].mean()

print("Sea-level mean:", sl_mean)
print("Plateau mean:", tp_mean)
print("Difference in means:", sl_mean - tp_mean)

from scipy.stats import ttest_ind #needed to perform a t-test to determine if the difference in means is statistically significaant

t_stat, p_value = ttest_ind(
    df["Sea Level Locust BPM"],
    df["Tibetan Plateau Locust BPM"]
)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("The difference is statistically significant so reject null hypothesis as altitude has an effect on locust breathing rates.")
else:
    print("The difference is not statistically significant so we cannot reject the null hypothesis.")

plt.savefig("locust_breathing_rate_boxplot.png") #saves the boxplot as a png file
plt.show() #creates a boxplot of the dataset to visualise the difference in breathing rates




                 



