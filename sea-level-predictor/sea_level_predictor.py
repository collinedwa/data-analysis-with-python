import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([year for year in range(1880, 2051)])
    y = line.slope*x + line.intercept
    plt.plot(x, y, 'y')

    # Create second line of best fit
    df_2 = df.loc[df['Year'] >= 2000]
    line_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    x_2 = pd.Series([year for year in range(2000, 2051)])
    y_2 = line_2.slope*x_2 + line_2.intercept
    plt.plot(x_2, y_2, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()