#Importing all the python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Overveiwing Dataset 
df = pd.read_csv(r'mymoviedb.csv')             
print(df.head()) 
df.info()
print(df['Genre'].head())
print(df.duplicated().sum())
print(df.describe())

#Converting Realease date Datatype to Datetime
df['Release_Date'] = pd.to_datetime(df['Release_Date'],errors ='coerce')
print(df['Release_Date'].dtypes)
# Extract year and month from Release_Date
df['Year'] = df['Release_Date'].dt.year
df['Month'] = df['Release_Date'].dt.month
#Counting movie released per year
plt.figure(figsize=(10,6))
sns.histplot(x='Year', data=df, palette="viridis")
plt.title("Number of Movies Released per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()
#counting movie released permonth
plt.figure(figsize=(10,6))
sns.countplot(x='Month', data=df, palette="mako")
plt.title("Number of Movies Released per Month (across all years)")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()

#30-Days rolling trend of movie release
release_trend = df.groupby('Release_Date').size().rolling(30).mean()
plt.figure(figsize=(12,6))
release_trend.plot()
plt.title("30-Day Rolling Average of Movie Releases")
plt.xlabel("Date")
plt.ylabel("Avg. Releases")
plt.show()

#removing Poster_Url
cols = ['Poster_Url']
df.drop(cols ,axis =1,inplace = True)
print(df.head())

#Removing extra spaces and coundting the genre
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop = True )
print(df['Genre'].describe())

#Visualizing Genre Data
sns.set_style('whitegrid')
sns.catplot(y= 'Genre',data = df,kind = 'count',order =df['Genre'].value_counts().index,color ='#4287f5' )
plt.title('Genre columne Distribution')
plt.show()

#which movie got the higest popularity
print(df[df['Popularity'] == df['Popularity'].max()])