import pandas as pd
import numpy as np
file_path = 'bhopal_aqi_weather_final_clean.csv'
df = pd.read_csv(file_path)
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)
#interpolation 
df.interpolate(method = 'time', inplace=True)
df.reset_index(inplace= True)

df.to_csv('bhopal_cleaned_data.csv', index=False)
