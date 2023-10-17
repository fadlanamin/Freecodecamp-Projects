import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.columns.values[0] = 'Page_Views' #Rename value to page views 
df.index = pd.to_datetime(df.index) #set index as date time

# Clean data
df = df[(df['Page_Views'] < df['Page_Views'].quantile(0.975)) & (df['Page_Views'] > df['Page_Views'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(14,5))
    plt.plot(df_line, 'purple')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    #Group the data by year, with value = average vies of each month
    df_bar['month'] = df_bar.index.copy() #Copy timeframe index to new column month, 
    df_bar['month'] = df_bar['month'].dt.month_name() #Convert date time to month, (can only be used in datetime data format)
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year #Convert date time to year

    #Create list of unique months in order, to be used in categorical for bar plot
    cat = df_bar.loc[df_bar['year'] == 2017, 'month'].unique().tolist()

    #Set unique month as category
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=cat)
    df_bar = df_bar.pivot_table(index='year', columns='month', values='Page_Views', aggfunc='mean')

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(9,9)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    #Used to order the month accordingly
    box_order = df_box.loc[df_box['year'] == 2017, 'month'].unique().tolist()

    # Draw box plots (using Seaborn)
    fig, ax= plt.subplots(nrows=1, ncols=2, figsize=(20,7))
    ax1 = sns.boxplot(data=df_box, x='year', y='Page_Views', ax=ax[0], fliersize=2, linewidth=1, width=0.5)
    ax1.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(data=df_box, x='month', y='Page_Views', ax=ax[1], fliersize=2, linewidth=1, width=0.5, order=box_order)
    ax2.set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
