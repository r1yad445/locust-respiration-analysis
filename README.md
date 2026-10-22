# Analysis of data on the effect of altitude on locust breathing rate

## Objective
To determine whether altitude has an affect on locust breathing rate, using sea level locusts and Tibetan plateau locusts. 
Null hypothesis = altitude has no affect on locust breathing rate.

## Methods
- Imported data using pandas
- Analysed shape of dataset and calculated summary statistics
- Use matplotlib to create a boxplot of the data
- Calculated the difference in mean breathing rates of each type of locust
- Used scipy to run a t-test to gain t statistic and p-value
- p-value was used to determine if  the difference in mean was statistcally significant (p < 0.05)


## Results
The p value was 1.12 *10^-5, so p < 0.05. This shows that the difference in mean breathing rates is statistically significant, meaning altitude does have an affect on locust breathing rate. So reject null hypothesis.