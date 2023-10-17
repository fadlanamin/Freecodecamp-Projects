import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100)**2)
df['overweight'] = np.where(df['weight'] / ((df['height'] / 100)**2) > 25, 1,
                            0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,
                   value_vars=[
                       'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                       'overweight'
                   ])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = pd.melt(df,
                   id_vars=['cardio'],
                   value_vars=[
                       'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                       'overweight'
                   ])
  df_cat = pd.melt(df,
                   id_vars=['cardio'],
                   value_vars=[
                       'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                       'overweight'
                   ]).value_counts().reset_index()
  df_cat = df_cat.rename(columns={'count': 'total'})
  df_cat = df_cat.sort_values(by=['variable'])

  # Draw the catplot with 'sns.catplot()'
  cat_plot = sns.catplot(data=df_cat,
                         x='variable',
                         y='total',
                         kind='bar',
                         col='cardio',
                         hue='value',
                         palette='Set1')
  cat_plot.set_axis_labels('variable', 'total')

  # Get the figure for the output
  fig = cat_plot.figure

  # Do not modify the next two lines
  fig.savefig('catplot.png')

  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['weight'] <= df['weight'].quantile(0.975)
                )  #5 weight is more than the 97.5th percentile
               | (df['weight'] >= df['weight'].quantile(0.025)
                  )  #4 weight is less than the 2.5th percentile
               | (df['height'] <= df['height'].quantile(0.975)
                  )  #3 height is more than the 97.5th percentile
               | (df['height'] >= df['height'].quantile(0.025)
                  )  #2 height is less than the 2.5th percentile
               |
               (df['ap_lo'] <= df['ap_hi']
                )]  #1 diastolic pressure is higher than systolic ap_lo > ap_hi
  
  # Calculate the correlation matrix
  corr = df_heat.corr().round(1)
  
  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr))

  # Set up the matplotlib figure
  fig, ax = plt.subplots()

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr,
              annot=True,
              square=True,
              center=0,
              annot_kws={'fontsize': 7},
              mask=mask)

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig