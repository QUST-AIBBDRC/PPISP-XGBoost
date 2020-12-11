import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

def logistic_dimension(data,label,parameter=m):#parameter是可调整的参数
    logistic_=LogisticRegression(penalty="l1", C=parameter)
    model=SelectFromModel(logistic_)
    new_data=model.fit_transform(data, label)
    mask=model.get_support(indices=True)
    return new_data,mask

data_=pd.read_csv(r' .csv')
data=np.array(data_)
label=np.append(label)
shu=scale(data)
data_2,mask=logistic_dimension(shu,label,parameter=m)
data_csv = pd.DataFrame(data=data_2)
data_csv.to_csv('out_LR.csv')