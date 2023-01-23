import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df =pd.read_csv('Final Assignment Liquor sales 2016 2019 USA.csv')
print(df.info())
print(df.head())
print("Missing values:", df.isnull().sum())
new_df= df.drop(['date',
       'address', 'city', 'store_location', 'county_number',
       'county', 'category', 'category_name', 'vendor_number', 'vendor_name',
       'item_number', 'pack', 'bottle_volume_ml',
       'state_bottle_cost', 'state_bottle_retail', 'volume_sold_liters', 'volume_sold_gallons'], axis = 1)
# print(new_df)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(new_df)
print("Missing values after dropping columns:", new_df.isnull().sum())

### most popular item based on zip code ###
a = df.groupby(['zip_code', 'item_description']).agg({'bottles_sold': 'sum'}).sort_values(by='bottles_sold', ascending=False)
print("The most popular item between 2016 -2019 based on Zipcode is:")
print(a.head(1))

### percentage of sales ###
sum_of_sales = df['sale_dollars'].sum()
df["%_of_sales"] =(df['sale_dollars'] / sum_of_sales) * 100
grouping_by_store= df.groupby(['store_number'])
print(grouping_by_store.agg({'%_of_sales': 'sum'}).sort_values(by='%_of_sales', ascending=False))

# Visualization of data
# x= []
# for item in df['zip_code']:
#     x.append(item)
# y =[]
# for item in df['bottles_sold']:
#     y.append(item)
# print(y)
# plt.title("Bottles sold based on Zip Code", color ='black')
# plt.xlabel("Zip_code")
# plt.ylabel("Bottles_sold")
# plt.plot(x,y, color= 'black', marker='o', markeredgecolor='blue', markerfacecolor = 'blue',markeredgewidth=0.5, markersize=7, ls='none')
# # plt.ylim(top =1600)
# plt.show()


# x_axis =[]
# for item in df["%_of_sales"]:
#     x_axis.append(item)
# y_axis = []
# for item in df['store_number']:
#     y_axis.append(item)
# plt.style.use('ggplot')
# plt.barh(y_axis, x_axis)
# plt.title('Percentage of sales per store')
# plt.xlabel('Percentage of sales')
# plt.ylabel('Store number')
# plt.xlim(0, 20)
# plt.ylim(2400, 9100)
# sns.despine(bottom=True, left=False)
# plt.show()