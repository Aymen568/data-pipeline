import pandas as pd # import pandas library for data manipulation and analysis
from pathlib import Path # import path library to work with file paths




# Read in data
df_main = pd.read_csv('usgs_main.csv')

# Clean data
df_main["date_time"] = pd.to_datetime(df_main["time"]) # Convert time to a column called date_time
df_main.drop("time", axis = 1) # Drop the old time column

df_main = df_main.assign(   
    date = df_main["date_time"].dt.date, # Make new column with date in the format year-month-day
    time = df_main["date_time"].dt.strftime('%I:%M %p'), # Make new column with 12 hour format
    military_time = df_main["date_time"].dt.time # Make new colum with 24 hour format
    )

# Query the dataframe to isolate types of earthquakes, to write a sentence about
number_earthquakes = df_main.shape[0] # Return number of rows of dataframe
earliest = df_main[df_main["date_time"] == df_main["date_time"].min()]
latest = df_main[df_main["date_time"] == df_main["date_time"].max()]  # Return the row with the earliest earthquake since you started recording
strongest = df_main[df_main["mag"] == df_main["mag"].max()] # Return the row with the strongest earthquakes since you started recording


file = open("Analysis remarqs.txt","a")
# Paste the values into a sentence. If there are earthquakes that happened at the same earliest time or had the same magnitude, we are taking the first row
file.write(f'Since {earliest.iloc[0]["time"]} on {earliest.iloc[0]["date"].strftime("%m/%d/%Y")}, there have been {number_earthquakes} recorded earthquakes.\n'
           f'The most recent earthquake had a magnitude of {latest.iloc[0]["mag"]} and occurred in/near {latest.iloc[0]["place"]} on {latest.iloc[0]["date"].strftime("%m/%d/%Y")} at {latest.iloc[0]["time"]}.\n'
           f'The strongest earthquake since the start of this web scraper had a magnitude of {strongest.iloc[0]["mag"]} and occurred in/near {strongest.iloc[0]["place"]} on {strongest.iloc[0]["date"].strftime("%m/%d/%Y")} at {strongest.iloc[0]["time"]}.')
f.write("/n")
file.close()
