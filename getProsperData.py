import requests
import pandas as pd

PROSPERDATASET_URL = "https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv" 

r = requests.get(PROSPERDATASET_URL)

if r.status_code == 200:
    data = pd.read_csv(PROSPERDATASET_URL)
    print (data.head())
    print ("-------------------------------")
    print (data.columns.values)
    print ("-------------------------------")
    print (data.info())

