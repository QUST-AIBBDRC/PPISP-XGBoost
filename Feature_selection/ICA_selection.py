import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.decomposition import FastICA

def ICA(data,n_components):
    ica = FastICA(n_components=95)
    X_transformed = ica.fit_transform(data)
    np.savetxt("ICA_out.csv", X_transformed, delimiter=",")
    return None

data_train=pd.read_csv(r' .csv')
data_=np.array(data_train)
data=data_[:,2:]
label=data_[:,1]
shu=scale(data)
data_1=ICA(shu,n_components=m)












