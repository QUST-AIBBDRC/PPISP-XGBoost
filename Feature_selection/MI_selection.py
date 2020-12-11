import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

def mutual_mutual(data,label,k=m):
    model_mutual= SelectKBest(mutual_info_classif, k=k)
    new_data=model_mutual.fit_transform(data, label)
    return new_data

data=pd.read_csv(r' .csv')
label=np.append(label)
data_2=mutual_mutual(shu,label,k=m)
data_csv = pd.DataFrame(data=data_2)
data_csv.to_csv('out_MI.csv')