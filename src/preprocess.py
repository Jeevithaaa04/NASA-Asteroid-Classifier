import pandas as pd

df=pd.read_json(r"D:\Downloads\My code\NASA-Asteroid-Classifier\data\raw_data.json")

df["velocity"]=df["velocity"].astype(float)
df["miss_distance_au"]=df["miss_distance_au"].astype(float)

final_df=df.drop(columns=["id","name"])

final_df["is_hazardous"]=final_df["is_hazardous"].astype(int)

print(final_df.head())

final_df.to_csv(r"D:\Downloads\My code\NASA-Asteroid-Classifier\data\cleaned_data.csv",index=False)