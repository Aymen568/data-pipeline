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
file.write("Hello \n")(f'Since {earliest.iloc[0]["time"]} on {earliest.iloc[0]["date"].strftime("%m/%d/%Y")} there have been {number_earthquakes} recorded earthquakes. {chr(10)} The most recent earthquake was {latest.iloc[0]["mag"]} in magnitude and occured in/near {latest.iloc[0]["place"]} on {latest.iloc[0]["date"]} at {latest.iloc[0]["time"]}.{chr(10)} The strongest earthquakes since the start of this webscraper was {strongest.iloc[0]["mag"]} magnitude and occured in/near {strongest.iloc[0]["place"]} on {strongest.iloc[0]["date"]} at {strongest.iloc[0]["time"]}.')
file.close()
