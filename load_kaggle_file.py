import pandas as pd
import kagglehub
file_path = kagglehub.dataset_download('shubhammeshram579/bank-customer-churn-prediction',force_download=True)
df=pd.read_csv(f"{file_path}/Churn_Modelling.csv")
