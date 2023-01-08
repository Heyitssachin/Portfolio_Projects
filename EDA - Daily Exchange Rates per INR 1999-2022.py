#!/usr/bin/env python
# coding: utf-8

# # Daily Exchange Rates per INR 1999-2022

# ### Importing Libraries

# In[41]:


import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns


# ### Loading the Dataset

# In[52]:


df = pd.read_csv("C:\\Users\\lenovo\\Downloads\\UNZIP_FOR_NOTEBOOKS\\Euro exchange rates.csv",  parse_dates=["Period\\Unit:"])
df.head()


# ### Data Cleaning
# 
# #### Rename Columns and Change data types
# 

# In[53]:


names = str.maketrans('', '', '[]')
df.columns = df.columns.str.translate(names)
df.columns = df.columns.str.strip()
df.set_index('Period\\Unit:', inplace=True)
df.index.rename('DateSeries', inplace = True)
df.info()


# In[54]:


cols = list(df)
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df_cur.info()


# ### Removing NaN Values

# In[46]:


df.isnull().sum(axis = 0)


# In[55]:


n = df.index[df.isnull().all(1)]
print(n)
print('Number of NaN rows: {}'.format(len(n)))


# In[56]:


df= df.drop(n)
df.info()


# In[58]:


df.describe(include='all')


# #### Change the structure of dataframe:
# #### reset index and make 2 columns: one with all the currency types: Currency name and another with Value attribute.

# In[70]:


df1 = df.reset_index()
df2=df1.melt(id_vars=['DateSeries'], var_name='Currency name', value_name='Value')
df2.head(5)


# ### Example: USD/INR and INR/USD
# Create new dataframe 'dataINRUSD' containig only values of US dollar and Indian rupee INR get 5 sample rows;
# Plot the graph including both currencies in rates of INR.

# In[71]:


dataINRUSD = df2.loc[(df2['Currency name'] == 'Indian rupee') | (df2['Currency name'] == 'US dollar')]
dataINRUSD.sample(5)


# In[ ]:





# In[91]:


plt.figure(figsize= (8,5), dpi = 100)
plt.grid(which='major', linewidth = 2)
plt.minorticks_on()
sns.lineplot(x='DateSeries', y='Value', hue='Currency name', data = dataINRUSD)
plt.grid(which='minor', linewidth = 0.5)
plt.legend(bbox_to_anchor=(1.1, 1), loc=('upper left'))


# ### Graphs for 2020 - 2022

# In[96]:


dataSince2020 = dataINRUSD.loc[dataINRUSD['DateSeries'] >= ' 20200101']

fig = plt.figure(figsize=(10,8)) 
plt.grid(which='major', linewidth = 2)
plt.minorticks_on()
plt.grid(which='minor', linewidth = 0.5)
sns.lineplot(x='DateSeries', y='Value', hue='Currency name', data = dataSince2020)
plt.legend(bbox_to_anchor=(1.05, 1), loc=(1.02, 0.7) , borderaxespad=0.);


# ### All time high of USD - INR exchange

# In[127]:


dataUSD = dataINRUSD.loc[(dataINRUSD['Currency name'] == 'US dollar')]
dataUSD['Value'].nlargest()


# ### All time low of USD - INR exchange

# In[126]:


dataUSD = dataINRUSD.loc[(dataINRUSD['Currency name'] == 'US dollar')]
dataUSD['Value'].nsmallest()


# ### All time high of INR - USD exchange

# In[128]:


dataINR = dataINRUSD.loc[(dataINRUSD['Currency name'] == 'Indian rupee')]
dataINR['Value'].nlargest()


# ### All time low of INR - USD exchange

# In[129]:


dataINR = dataINRUSD.loc[(dataINRUSD['Currency name'] == 'Indian rupee')]
dataINR['Value'].nsmallest()


# ## Conclusion
# BY SEEING ABOVE PLOTS AND  ANALYSIS, WE CAN VIEW IT CLEARLY THAT HOW USD HAS BEEN STABLE THROUGH THE OUT THE YEARS IN COMPARISION OF INR.
# WHICH MAKES USD ONE OF THE STABLE CURRENCY IN THE WORLD.
