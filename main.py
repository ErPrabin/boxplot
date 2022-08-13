import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_excel('Precipitation_bias_rating.xlsx')
# print(df.Bernoulli_Exponential)
sns.boxplot(x='Evaluation_Metrics', y='Bernoulli_Exponential', data=df)
sns.boxplot(x='Evaluation_Metrics', y='Bernoulli_Gamma', data=df)
# df = pd.DataFrame({'A': [5, 7, 7, 9, 12, 12],
#                    'B': [8, 8, 9, 13, 15, 17],
#                    'C': [1, 2, 2, 4, 5, 7]})
# df_melted = pd.melt(df)
# sns.boxplot(x='variable', y='value', data=df_melted)
plt.xlabel('Team')
plt.ylabel('Performance Rating')
plt.show()