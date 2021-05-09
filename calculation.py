import pandas as pd

col_list = ["order_amount", "total_items"]
test_data = pd.read_csv ('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', usecols=col_list)

#print (test_data.std(axis=0, skipna = True))

#print (test_data.mean(axis=0, skipna = True))
#print (test_data.median(axis=0, skipna = True))
#print (test_data.mode(axis=0))
value_sum = 0
for i in range(0,test_data["order_amount"].size):
    value_sum += test_data["order_amount"][i]/test_data["total_items"][i]

print(value_sum/test_data["order_amount"].size)