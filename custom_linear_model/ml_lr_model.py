from lr_model import custom_linear_Regression
import numpy as np
house_area = [100,150,200,225,250,300]
house_price =[10,12,15,20,25,27]
lr_reg = custom_linear_Regression()
lr_reg.fit_train(house_area, house_price)
print(f'lr_reg.sl = {lr_reg.sl}')
print(f'lr_reg.ic = {lr_reg.ic}')
predicted_price = lr_reg.predict_val(500)
print(f'Predicted price for 500 sq ft house = {predicted_price}')

