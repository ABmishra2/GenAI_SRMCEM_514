import numpy as np
class custom_linear_Regression(object):
    def __init__(self):
        pass 
    '''def __new__(cls , *args, **kwargs):
        obj = super().__new__(cls)
        print(f'{obj=}')
        return obj'''
    
    def fit_train(self, X, y):
        X = np.array(X)
        y = np.array(y)
        f_exp = X - np.average(X)
        s_exp = y - np.average(y)
        nt = np.sum(f_exp  * s_exp)
        demt = np.sum(f_exp ** 2)

        self.sl = nt / demt
        self.ic = np.average(y) - self.sl * np.average(X)


    def predict_val(self,X):
        return self.sl * X + self.ic


        

ref = custom_linear_Regression()

print(f'{ref=}')



