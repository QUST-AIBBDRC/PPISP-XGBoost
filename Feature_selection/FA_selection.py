import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.decomposition import FactorAnalysis

def factorAnalysis(data,percentage = m):
    dataMat = np.array(data) 
    newData,meanVal=zeroMean(data)  #equalization
    covMat=covArray(newData)  #covariance matrix
    eigVals,eigVects=featureMatrix(covMat)
    n_components = percentage2n(eigVals,percentage)
    clf = FactorAnalysis(n_components=n_components)
    new_data = clf.fit_transform(dataMat)
    return new_data  # return the new data

data=pd.read_csv(r' .csv')
label=data_[:,1]
data_2=factorAnalysis(shu,percentage = m)
data_csv = pd.DataFrame(data=data_2)
data_csv.to_csv('out_FA.csv')















