import pandas as pd
import numpy as np
from hello import create_dataframe
dict1={'Math': [80, 89, 70], 'Physics': [92, 94, 72], 'Chemistry': [90, 87, 70]}
df1=create_dataframe(dict1)
print(df1)
for col in df1.columns:
    print(df1[col].mean())
    print(max(df1[col]))
    print(min(df1[col]))
    print(df1.columns)