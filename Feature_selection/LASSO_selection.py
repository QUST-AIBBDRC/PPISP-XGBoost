import scipy.io as sio
import numpy as np
import pandas as pd

from sklearn.linear_model import LassoCV

def lassodimension(data,label,alpha=np.array([0.01])):#alpha代表想要传递的alpha的一组值,用在循环中,来找出一个尽可能好的alpha的值
    lassocv=LassoCV(cv=5, alphas=alpha,max_iter=2000).fit(data, label)
#    lasso = Lasso(alpha=lassocv.alpha_, random_state=0)#生成Lasso对象
    x_lasso = lassocv.fit(data,label)#代入alpha进行降维
    mask = x_lasso.coef_ != 0 #mask是一个numpy数组,数组中的元素都是bool值,并且数组的维度和data的维度是相同的
    new_data = data[:,mask]  #将data中相应维度中与mask中为True对应的元素挑选出来
    return new_data,mask #返回降维之后的数组,并将使用lasso训练数据之后得到的最大值一起返回

data=pd.read_excel(r' .xlsx')
label=data_[:,1]
shu=scale(data)
data_2,index=lassodimension(shu,label)
data_csv = pd.DataFrame(data=data_2)
data_csv.to_csv('Rout_lasso.csv')

