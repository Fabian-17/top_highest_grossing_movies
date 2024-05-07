# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

movies_data = pd.read_csv("Top_1000_Highest_Grossing_Movies_Of_All_Time.csv")
movies_data

#shape of the dataset
print("Shape of the dataset is",movies_data.shape)

#information about the dataset
movies_data.info()

#checking for null values to comfirm that there are no NULL values in it.
movies_data.isna().sum()


movies_data

'''Dropping the Logline column because it's not needed in our analysis.'''
movies_data.drop('Logline', inplace=True, axis=1)

movies_data.info()

'''Converting Object to Numeric datatype'''
list_to_clean=[ 'Year of Realease', 'Gross', 'Worldwide LT Gross', 'Metascore', 'Votes']

for i in list_to_clean:
    movies_data[i]=movies_data[i].replace(r'[$|M|******|,|X]' , '', regex=True)
    movies_data[i] = pd.to_numeric(movies_data[i])

    movies_data

movies_data.describe()


top_10 = movies_data.head(10)


print(plt.style.available)


plt.style.use("fivethirtyeight")
plt.figure(figsize=(10,10))
plt.title("Top 10 Highest Grossing Movies Of All Time")
sns.barplot(data=top_10, y= "Movie Title", x="Worldwide LT Gross",hue="Year of Realease")
plt.show()



movies_data["Movie Rating"].value_counts()


plt.style.use("fivethirtyeight")
plt.figure(figsize=(12,12))
sns.countplot(data=movies_data,y="Movie Rating")
plt.show()


movies_data[movies_data["Movie Rating"]>=9]


movies_data[movies_data["Movie Rating"]<=4]


'''Creating a Histogram of Movie Rating, Metascore, Votes, and Duration.'''
fig, axes = plt.subplots(2, 2,figsize=(12,12))
plt.style.use("fivethirtyeight")
sns.histplot(data=movies_data, x='Movie Rating',ax=axes[0,0])
sns.histplot(data=movies_data, x='Metascore',ax=axes[0,1])
sns.histplot(data=movies_data, x='Votes',ax=axes[1,0])
sns.histplot(data=movies_data, x="Duration",ax=axes[1,1])
plt.show()



'''Creating a Histogram of Movie Rating, Metascore, Votes, and Duration with KDE'''
fig, axes = plt.subplots(2, 2,figsize=(12,12))
plt.style.use("fivethirtyeight")
sns.histplot(data=movies_data, x='Movie Rating',ax=axes[0,0],kde=True)
sns.histplot(data=movies_data, x='Metascore',ax=axes[0,1],kde=True)
sns.histplot(data=movies_data, x='Votes',ax=axes[1,0],kde=True)
sns.histplot(data=movies_data, x="Duration",ax=axes[1,1],kde=True)
plt.show()


movies_with_highest_rating = movies_data[["Movie Title","Movie Rating"]].sort_values(by=["Movie Rating"], ascending=False)
movies_with_highest_rating


top_10_highest_rated = movies_with_highest_rating.head(10)
top_10_highest_rated


print(plt.style.available)

plt.style.use('fivethirtyeight')
plt.figure(figsize=(12,12))
plt.xlim(8, 10)
plt.title("Top 10 Highest rated movies")
sns.barplot(data=top_10_highest_rated, x= "Movie Rating", y="Movie Title")
plt.show()