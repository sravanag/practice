import pandas as pd
def create_dataframe(dict1):
    df=pd.DataFrame(dict1)
    return df

dict1={"sub":["English","hindi","telugu","urdu","odia","chemistry"],
             "marks":[91,78,67,58,98,76]
       }
df=create_dataframe(dict1)
print(df[df['marks']>=70])
