import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.decomposition import KernelPCA

def KPCA(data,percentage=m):
    dataMat = np.array(data)  
    newData,meanVal=zeroMean(data)  
    covMat=covArray(newData)  
    eigVals,eigVects=featureMatrix(covMat)
    n_components = percentage2n(eigVals,percentage)
    #n_component=n_components
    clf=KernelPCA(n_components=n_components,kernel='rbf',gamma=1/n)#rbf linear poly
    new_x=clf.fit_transform(dataMat)
    return new_x

data_train=pd.read_excel(r' .xlsx')
data_=np.array(data_train)
data=data_[:,2:]
data_2=KPCA(shu,percentage = m)
data_csv=pd.DataFrame(data=data_2)
data_csv.to_csv(' out_KPCA.csv')







