import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
from scipy import stats
from sklearn.datasets import load_boston

boston = load_boston()

bostonDF = pd.DataFrame(boston.data, columns = boston.feature_names)

bostonDF['PRICE'] = boston.target
print('Boston data size:', bostonDF.shape)

# find out the relation between column properties 
#
#fig, axs = plt.subplots(figsize=(16,8), ncols = 4, nrows = 2) # show the various graph at once
#lm_feature = ['RM','ZN','INDUS','NOX', 'AGE', 'PTRATIO', 'LSTAT', 'RAD']
#for i, feature in enumerate(lm_feature):
#    row = int(i/4)
#    col = i%4
#    sns.regplot(x=feature, y='PRICE', data=bostonDF, ax= axs[row][col]) # show one feature and price relation with scatters  

