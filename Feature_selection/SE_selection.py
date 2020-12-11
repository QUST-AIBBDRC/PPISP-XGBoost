import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.manifold import SpectralEmbedding 

def SE(data,n_components=m):
    embedding = SpectralEmbedding(n_components=n_components)
    X_transformed = embedding.fit_transform(data)
    return X_transformed
    
data=pd.read_csv(r' .csv')
shu=scale(data)
data_2=SE(shu,n_components=m)
data_csv = pd.DataFrame(data=data_2)
data_csv.to_csv('out_SE.csv')