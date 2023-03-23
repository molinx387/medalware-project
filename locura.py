import pandas as pd

df1 = pd.read_csv('detections.csv')
df2 = pd.read_csv('detections_sha.csv')

concatenated = pd.concat([df1, df2], axis=1, ignore_index=True)

concatenated.to_csv('detections_data.csv', index=False)