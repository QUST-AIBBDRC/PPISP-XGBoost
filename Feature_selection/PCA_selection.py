import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.decomposition import PCA

def pca(data,percentage = m):  
    dataMat = np.array(data) 
    newData,meanVal=zeroMean(data)  #equalization
    covMat=covArray(newData)  #covariance matrix
    eigVals,eigVects=featureMatrix(covMat)
    n_components = percentage2n(eigVals,percentage)
    clf=PCA(n_components=n_components)  
    new_x = clf.fit_transform(dataMat)
    return new_x
    
    
data_train=pd.read_excel(r' .xlsx')
data_=np.array(data_train)
data=data_[:,2:]
shu=scale(data)
data_2=pca(shu,percentage = m)
shu=data_2
data_csv=pd.DataFrame(data=shu)
data_csv.to_csv(' out_PCA.csv')




