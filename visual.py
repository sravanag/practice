import pandas as pd
import numpy as np
from hello import create_dataframe
dict1={'Math': [89, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
df1=create_dataframe(dict1)
print(df1)
for col in df1.columns:
    print(df1[col].mean())
