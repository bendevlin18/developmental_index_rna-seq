#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from pandas import ExcelFile


# In[4]:


my_df = pd.read_excel('/Users/annayoungkin/Desktop/GroupData.xlsx', header=1)


# In[5]:


my_df


# In[6]:


#my_df.rename(columns = {'GSE127884_microglia.cdep.meta':'Sample Name'}, inplace = True)
#my_df.rename(columns = {'Unnamed: 1':'Genotype'}, inplace = True)
#my_df.rename(columns = {'Unnamed: 2':'Organism'}, inplace = True)
#my_df.rename(columns = {'Unnamed: 3':'Age'}, inplace = True)
#my_df.rename(columns = {'Unnamed: 4':'Sex'}, inplace = True)
#my_df.rename(columns = {'Unnamed: 5':'Area'}, inplace = True)
my_df = my_df.drop(columns=['plateplus', 'plate', 'lane', 'raw file', 'molecule', 'Unnamed: 11', 'Unnamed: 12'])
my_df = my_df.reset_index(drop=True)
print(my_df.head())


# In[7]:


my_df2 = my_df.T
my_df2.columns = my_df2.iloc[0]
my_df2 = my_df2.drop(my_df2.index[0])
my_df2


# In[70]:


gene_df = pd.read_csv('/Users/annayoungkin/Desktop/GSE127884_microglia.cdep.SeuratNorm (1).tsv', sep='\t')


# In[71]:


gene_df= gene_df.reindex(sorted(gene_df.columns), axis=1)
print(gene_df.head())


# In[72]:


#gene_df2 = gene_df.T
#gene_df2.columns = gene_df2.iloc[0]
#gene_df2 = gene_df2.drop(gene_df2.index[0])
#print(gene_df2.head())


# In[73]:


samples = gene_df.columns.values
samples2 = samples[0:-1]
print(len(samples2))


# In[74]:


total = my_df2.columns.values
total


# In[75]:


for i in total:
    if i not in samples2:
        my_df2 = my_df2.drop(columns=[i])
my_df2


# In[76]:


my_df3 = my_df2.reindex(sorted(my_df2.columns), axis=1)
my_df4 = my_df3.T
my_df4


# In[77]:


gene_df2 = gene_df.T
gene_df2.columns = gene_df2.iloc[-1]
gene_df2 = gene_df2.drop(gene_df2.index[-1])
gene_df2


# In[78]:


names = my_df4.columns.values
for i in names:
    add = my_df4[i]
    gene_df2 = gene_df2.join(add)


# In[79]:


print(gene_df2)


# In[80]:


#last = list(gene_df2.columns[-5:-1])
#total = last.append('tissue')
#last


# In[81]:


#gene_df2 = gene_df2.sort_values(by = ['age','sex','tissue','organism','genotype'], inplace=True)
#gene_df2


# In[82]:


gene_df2 = gene_df2.sort_values(by = 'age')


# In[83]:


gene_df2


# In[84]:


cols = gene_df2.columns.tolist()
cols = cols[-5:]+cols[:-5]
cols


# In[85]:


gene_df2 = gene_df2[cols]
gene_df2


# In[86]:


gene_df2['genotype'].value_counts()


# In[87]:


gene_df2['tissue'].value_counts()


# In[88]:


gene_df2['Xkr4']=gene_df2['Xkr4'].astype('float')


# In[89]:


gene_df2.groupby(['genotype'])['Xkr4'].mean()


# In[90]:


gene_df2['Vamp7'].astype('float')


# In[91]:


import developmental_index as dvp


# In[92]:


genes_df = gene_df2.T
genes_df


# In[93]:


genes_df.dropna(inplace = True)
genes_df


# In[94]:


import scipy.stats as stats


# In[95]:


columns = genes_df.columns.tolist()
columns


# In[96]:


new_df= genes_df.drop(genes_df.index[0:5])
new_df


# In[97]:


for i in columns:
    new_df[i]=new_df[i].astype('float')
new_df


# In[67]:


dir(dvp)


# In[69]:


new_df
dvp.scale_expression(new_df)


# In[ ]:





# In[64]:


new_df = dvp.drop_unexpressed_genes(new_df)


# In[62]:


dvp.identify_significant_genes(new_df, new_df, new_df)


# In[63]:


#dvp.remove_insignificant_rows(new_df)


# In[49]:


#dvp.extract_regulated_genes(new_df)


# In[52]:


sample_cols = new_df.columns
new_df = dvp.generate_index(new_df, sample_cols)


# In[53]:


dvp.scale_index(new_df)


# In[ ]:




