import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #Create the regression
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x,y)

    # Create first line of best fit
    x_1 = pd.Series([i for i in range(1880, 2051)]) #Create year until 2050
    y_1 = res.intercept + res.slope*x_1

    #Create second line of best fit
    df_2 = df[df['Year'] > 1999]

    #Create linear regression from the year 2000
    x2 = df_2['Year']
    y2 = df_2['CSIRO Adjusted Sea Level']
    res_2 = linregress(x2,y2)

    #Create the second line of the best fit
    x_2 = pd.Series([i for i in range(2000, 2051)]) #Create the year until 2050
    y_2 = res_2.intercept + res_2.slope*x_2

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,10))
    plt.scatter(x,y)

    # Create first line of best fit
    plt.plot(x_1, y_1, 'red', label='First fitted Line')

    #Create second line of best fit 
    plt.plot(x_2,y_2, 'blue', label='Seconf fitted line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.show
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()