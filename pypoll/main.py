import os
import csv
import pandas as pd
import numpy as np

csvpath=os.path.join('Resources','election_data.csv')
poll_df = pd.read_csv(csvpath)
votes=poll_df.shape[0]
name= poll_df["Candidate"].unique()
result=poll_df["Candidate"].value_counts()
percent=np.round(((result.values/votes)*100),decimals=3)

final=f"Election Results\n-------------------------\nTotal Votes: {votes}\n-------------------------\n"
for i in range(len(name)):
    final=final+f"{name[i]}:  {percent[i]} % ({result[i]})\n"
final=final+f"-------------------------\nWinner: {name[0]}\n-------------------------"
print(final)
File= open("final.txt","w+")
File.write(final)
