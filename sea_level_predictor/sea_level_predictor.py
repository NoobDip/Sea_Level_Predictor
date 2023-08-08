import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df = df.drop(['Lower Error Bound', 'Upper Error Bound', 'NOAA Adjusted Sea Level'], axis=1)
    df = df.sort_values(by="Year")
    
    # Create scatter plot
    df_scatter = df[['CSIRO Adjusted Sea Level', 'Year']]
    fig, ax = plt.subplots()
    ax.scatter(df_scatter['Year'], df_scatter['CSIRO Adjusted Sea Level'])
    ax.set_xlabel('Year')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0], [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Regression model for data before 2000
    df_extension = pd.DataFrame({'Year': list(range(2014, 2051)), 'CSIRO Adjusted Sea Level': 0})
    final_df = pd.concat([df_scatter, df_extension], ignore_index=True) 
    slope_1, intercept_1, r_value, p_value, std_err = linregress(df_scatter['Year'], df_scatter['CSIRO Adjusted Sea Level'])
    first_best_fit_line = (slope_1 * final_df['Year']) + intercept_1
    ax.plot(final_df['Year'], first_best_fit_line, c='r')

    # Regression model for data after 2000
    slope_2, intercept_2, r_value, p_value, std_err = linregress(df_scatter[df_scatter['Year']>=2000]['Year'], df_scatter[df_scatter['Year']>=2000]['CSIRO Adjusted Sea Level'])
    first_best_fit_line = (slope_2 * final_df[final_df['Year']>=2000]['Year']) + intercept_2
    ax.plot(final_df[final_df['Year']>=2000]['Year'], first_best_fit_line, c='g')

    # Save plot and return data
    plt.savefig('sea_level_plot.png')
    return [plt.gca(), slope_1, intercept_1, slope_2, intercept_2]
