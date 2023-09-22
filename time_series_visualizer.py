import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.) 
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])

# Clean data
top = np.percentile(df['value'], 97.5)
bottom = np.percentile(df['value'], 2.5)

df = df[(df['value'] < top) & (df['value'] > bottom)]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(12, 6))
    fig = sns.lineplot(x='date', y='value', data=df, color='red')
    fig.set_xlabel('Date')
    fig.set_ylabel('Page Views')
    fig.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')



    fig = fig.figure
    # Save image and return fig (don't change this part)
    fig.savefig('img/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar['date'].apply(lambda month: month.month)
    df_bar['year'] = df_bar['date'].apply(lambda year: year.year)
    df_bar['day'] = df_bar['date'].apply(lambda day: day.day)
    
    month_map = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8:'August', 9:'September', 10:'October', 11:'November', 12: 'December'}
    df_bar['month'] = df_bar['month'].map(month_map)
    
    df_bar_group = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar_group = df_bar_group.reset_index()
    
    plt.figure(figsize=(10, 6))
    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Draw bar plot
    fig = sns.barplot(x="year", y ='value', hue="month", data=df_bar_group, hue_order=hue_order, )
    plt.legend(title='Months', loc=2)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    
    # Save image and return fig (don't change this part)
    fig = fig.figure
    fig.savefig('img/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(15, 6))
    plt.subplot(121)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    plt.subplot(122)
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=order)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig = fig.figure
    fig.savefig('img/box_plot.png')
    return fig
