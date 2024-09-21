import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = pd.Series(np.divide(df['weight'], np.square(df['height'] / 100)) > 25)
df['overweight'] = df['overweight'].astype(int)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# 4
def draw_cat_plot():
    df_cat_0 = df[df['cardio'] == 0]
    df_cat_1 = df[df['cardio'] == 1]
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True, gridspec_kw={'wspace': 0.05})
    sns.countplot(x='variable', hue='value', stat='count', data=pd.melt(df_cat_0[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']]), ax=ax[0], legend=False)
    sns.countplot(x='variable', hue='value', stat='count', data=pd.melt(df_cat_1[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']]), ax=ax[1], legend=True)
    ax[0].set_title('cardio = 0')
    ax[1].set_title('cardio = 1')
    ax[0].set_ylabel('total')
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    df['bmi'] = np.divide(df['weight'], np.square(df['height'] / 100))
    
    df.drop(df[(df['ap_lo'] > df['ap_hi'])].index, inplace=True)
    df.drop(df[(df['height'] < df['height'].quantile(0.025))].index, inplace=True)
    df.drop(df[(df['height'] > df['height'].quantile(0.975))].index, inplace=True)
    df.drop(df[(df['weight'] < df['weight'].quantile(0.025))].index, inplace=True)
    df.drop(df[(df['weight'] > df['weight'].quantile(0.975))].index, inplace=True)


    corr = df.corr()
    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize=(12, 8))
    
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': 0.45})
    ax.set_title('Correlation Matrix')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # 16
    fig.savefig('heatmap.png')
    return fig

