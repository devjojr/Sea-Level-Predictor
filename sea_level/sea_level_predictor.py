import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x_axis = df['Year']
    y_axis = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, axes = plt.subplots()
    plt.scatter(x_axis, y_axis)

    # Create first line of best fit
    res = linregress(x_axis, y_axis)
    print(res)

    sea_level_x = pd.Series([_ for _ in range(1880, 2051)])
    sea_level_y = (res.slope * sea_level_x) + res.intercept
    plt.plot(sea_level_x, sea_level_y, 'r')

    # Create second line of best fit
    df_bf = df.loc[df['Year'] >= 2000]
    x_axis_bf = df_bf['Year']
    y_axis_bf = df_bf['CSIRO Adjusted Sea Level']
    res_bf = linregress(x_axis_bf, y_axis_bf)
    sea_level_x_bf = pd.Series([_ for _ in range(2000, 2051)])
    sea_level_y_bf = (res_bf.slope * sea_level_x_bf) + res_bf.intercept
    plt.plot(sea_level_x_bf, sea_level_y_bf, 'green')

    # Add labels and title
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
