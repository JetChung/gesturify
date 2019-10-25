from sklearn import preprocessing
le = preprocessing.LabelEncoder()

# First Feature
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
# Second Feature
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

# Label or target varible
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']


weather_encoded=le.fit_transform(weather)
print(weather_encoded)
# converting string labels into numbers
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)