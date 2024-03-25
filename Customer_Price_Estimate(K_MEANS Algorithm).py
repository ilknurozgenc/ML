#GEREKLİ KÜTÜHANELERİ YÜKLEMEK
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

#DATASET OKUTMA İŞLEMİ
data=pd.read_csv("Customer_Price_Estimate.csv")  #Konu ile ilgili indirilmiş bir dataset.

#VERİ OKUMA VE GÖRÜNTÜLEME
data.head()
data.tail()

plt.scatter(data["UnitPrice"],data["Quantity"])
plt.xlabel("birim fiyat")
plt.ylabel("miktar")
plt.show()

scaler=MinMaxScaler()

scaler.fit(data[["UnitPrice"]])              #bir standartlaştırma işlemi yapıp küçükten büyüğe doğru sıralıyıcaz UnitPrice değerlerini.
data["UnitPrice"]=scaler.transform(data[["UnitPrice"]])

data.head()

scaler.fit(data[["Quantity"]])
data["Quantity"]=scaler.transform(data[["Quantity"]])

data.head()

data.tail()

dirsek=range(1,11)

liste=[]

#MAKİNE ÖĞRENMESİ K-MEANS ALGORİTMASINI KULLANMAK
from sklearn.cluster import KMeans

for k in dirsek:
    km=KMeans(n_clusters=k)
    km.fit(data[["UnitPrice","Quantity"]])
    liste.append(km.inertia_)

plt.xlabel("k")
plt.ylabel("dirsek")
plt.plot(dirsek,liste)
plt.show()

kson=KMeans(n_clusters=5)
y_pred=kson.fit_predict(data[["UnitPrice","Quantity"]])
y_pred    #eldeki verileri redic ediyoruz, yani kategorilere ayırdık.

data["cluster"]=y_pred    #cluster dediğimiz stunu tabloya ekler.

data.head()

kson.cluster_centers_       #değerlerin orta noktalarını elde ettik.

#KÜMELEME İÇİN CLUSTER SINIFI OLUŞTURMAK.
data1=data[data.cluster==0]
data2=data[data.cluster==1]
data3=data[data.cluster==2]
data4=data[data.cluster==3]
data5=data[data.cluster==4]

#K-MEANS İLE İŞLENEN VERİLER İÇİN SON ADIM

#OLUŞTURULAN SONUÖLARIN TABLO VEYA GRAFİK ÜZERİNDEN RENKLENDİRİLMESİ.

plt.xlabel("birim fiyat")
plt.ylabel("miktar")
plt.scatter(data1["UnitPrice"],data1["Quantity"],color="red")
plt.scatter(data2["UnitPrice"],data2["Quantity"],color="blue")
plt.scatter(data3["UnitPrice"],data3["Quantity"],color="green")
plt.scatter(data4["UnitPrice"],data4["Quantity"],color="teal")
plt.scatter(data5["UnitPrice"],data5["Quantity"],color="pink")

#CLUSTE LAR İÇİN ORTA NOKTALARINI ALMAK.
plt.scatter(kson.cluster_centers_[:,0],kson.cluster_centers_[:,0],color="black",marker="x",label="centroid")
plt.legend()
plt.show()
