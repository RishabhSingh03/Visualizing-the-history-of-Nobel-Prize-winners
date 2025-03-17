import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nobel_laureates_data.csv')
data.head()
data.info()
data.isnull().sum()
data.describe(include='all')
data.drop(columns=['died','diedCountry','diedCity']) 
data = data.dropna(subset=['gender','bornCountry'])
data['motivation']=data['motivation'].fillna('Not specified')
data['bornCountry']=data['bornCountry'].fillna('Not specified')
data['organizationName']=data['organizationName'].fillna('Not specified')
data['organizationCountry']=data['organizationCountry'].fillna('Not specified')
data['organizationCity']=data['organizationCity'].fillna('Not specified')
data['category']= data['category'].str.title()
data['gender']=data['gender'].str.capitalize()
data['year']=pd.to_datetime(data['year'],format='%Y').dt.year
data = data.drop_duplicates()

data['year']=pd.todatetime(data['year'])
yearly_awards = data.groupby(data['year'].dt.year).size()
plt.figure(figsize=(10,6))
plt.plot(yearly_awards.index, yearly_awards.values)
plt.title("Number of Nobel Laureates Over Time")
plt.xlabel("year")
plt.show()

category_type = data['category'].value_counts()
category_type.plot(kind='bar', figsize=(8,5), color='blue')
plt.title("Category of Nobel Laureates")
plt.xlabel("Category")
plt.ylabel("Number of Laureates")
plt.show()

gender_type = data['gender'].value_counts()
gender_type.plot(kind='pie', autopct= '%1.1f%%',figsize=(6,6),colors=['blue','purple'])
plt.title("Gender Distribution of Nobel Laureates")
plt.ylabel("")
plt.show()



