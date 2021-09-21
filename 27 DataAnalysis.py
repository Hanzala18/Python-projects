import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import funktionen as f

#url="http://www.pfeffer.at/r/allbus2018.dat"
#f.speichern("allbus.dat", f.geturl(url))
allbus=pd.read_csv("allbus.dat", sep="\t")
#print (allbus.head())
#print (allbus.shape)
#print (allbus.info())
##di01a = Nettoeinkommen
#print (allbus['di01a'].describe())
allbus=allbus[allbus['di01a']>0]
#print (allbus['di01a'].describe())
#print (allbus['di01a'].median())
#allbus['di01a'].plot(kind='box', vert=False)
#plt.hist(allbus['di01a'],bins=50)
m = allbus[allbus["sex"]==1]
print (m['di01a'].median())
w = allbus[allbus["sex"]==2]
print (w['di01a'].median())
sns.distplot(m['di01a'])
sns.distplot(w['di01a'])
plt.show()