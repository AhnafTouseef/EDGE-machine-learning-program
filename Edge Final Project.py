
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error


dt=DecisionTreeRegressor(max_depth=20, min_samples_split=10, random_state=5)


# Import dataframes
wt=pd.read_excel('Research dataset.xlsx', sheet_name='wt')
rf=pd.read_excel('Research dataset.xlsx', sheet_name='rf')
tmp=pd.read_excel('Research dataset.xlsx', sheet_name='tmp')


# Water table dataset for each upazilla/station
abhaynagar_2_wt = wt[wt.wid=='JES12']
# Rainfall dataset for each upazilla
abhaynagar_rf = rf[rf.upazila=='Abhaynagar'].drop(columns=['upazila','rid'], axis=1)



# Merge water table and rainfall dataframes --> remove upazilla and wid columns --> drop na values --> save to new dataframe 
df = abhaynagar_2_wt.merge(abhaynagar_rf, on='date', how='left').drop(columns=['upazila','wid'], axis=1).dropna().merge(tmp, on='date', how='left')

# Create target column by shifting the wtable column by 1
df=df.iloc[:,[0,3,2,1]]
df['target']=df.shift(-1)['wtable']
df.dropna(inplace=True)

# Create time cycle columns and features
# 1.Extract year
df['year'] = df['date'].dt.year

# 2. Extract Month and Encode Cyclically
df['month'] = df['date'].dt.month
df['sin_month'] = np.sin(2 * np.pi * df['month'] / 12)
df['cos_month'] = np.cos(2 * np.pi * df['month'] / 12)

# 3. Extract Day of Month and Encode Cyclically
df['day'] = df['date'].dt.day  
df['sin_day'] = np.sin(2 * np.pi * df['day'] / 31) 
df['cos_day'] = np.cos(2 * np.pi * df['day'] / 31)

# Drop the original 'month' and 'day' columns 
df = df.drop(columns=['month', 'day'])


# Train and test split
train_filter = (df.date.dt.year<2019)&(df.date.dt.year>1990) # Train selection filter
test_filter = (df.date.dt.year>2019) # Test selection filter

x_train= df[train_filter].drop(columns=['target','year'], axis=1).set_index('date')
y_train= df[train_filter].target

x_test= df[test_filter].drop(columns=['target','year'], axis=1).set_index('date')
y_test= df[test_filter].target

# Fit the model
machine=dt.fit(x_train, y_train)
prediction = machine.predict(x_test)

# Plot scores
plt.bar(['MSE','MAE%','R2 score','Score'],
        [mean_squared_error(y_test, prediction), mean_absolute_percentage_error(y_test, prediction), 
         r2_score(y_test, prediction), machine.score(x_train, y_train)], color=['r','lime','purple','b'])

plt.show()






