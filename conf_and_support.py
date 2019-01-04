import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/snehamitta/Desktop/ML/Assignment2/Groceries(1).csv')

#Q2.a) To find number of customers
print('There are', data['Customer'].max(), 'in the given dataset')

#Q2.b) To find the unique items
print ('There are', np.size(data['Item'].unique()), 'unique items in the dataset')

#Q2.c) Plotting a histogram with distinct item numbers
y = data.groupby('Customer').size()
print(y.describe())
y.to_csv("~/Desktop/out.csv", sep = ',',header=None, index = False)
y.plot.hist(bins = 30)
plt.grid(True)
plt.show()

# Convert the Sale Receipt data to the Item List format
ListItem = data.groupby(['Customer'])['Item'].apply(list).values.tolist()

# Convert the Item List format to the Item Indicator format
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(ListItem).transform(ListItem)
ItemIndicator = pd.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

frequent_itemsets = apriori(ItemIndicator, min_support = 0.0076, use_colnames = True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print('The number of itemsets found', len(frequent_itemsets))
print('The highest k value in my itemset is', max(frequent_itemsets['length']))

# Discover the association rules
assoc_rules = association_rules(frequent_itemsets, metric = "confidence", min_threshold = 0.01)
print ('The number of association rules are', len(assoc_rules))

import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))
plt.scatter(assoc_rules['confidence'], assoc_rules['support'], s = assoc_rules['lift'])
plt.grid(True)
plt.xlabel("Confidence")
plt.ylabel("Support")
plt.show()

# Find the frequent itemsets
frequent_itemsets = apriori(ItemIndicator, min_support = 0.0076, use_colnames = True)

# Discover the association rules
assoc_rules = association_rules(frequent_itemsets, metric = "confidence", min_threshold = 0.6)
print ('The number of association rules with confidence = 60 percent are', len(assoc_rules))
print (assoc_rules)



