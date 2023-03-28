import pandas as pd
import numpy as np
import re
import csv

# Read data from csv to dataframe and add parameter that will read in the following as nans:  'undefined', ' ', 'none', '-' 

hotel_bookings = pd.read_csv("hotel_bookings.csv").replace(['([uU]ndefined)', '/^(\S) &', '/^([nN]one)$', '/^(-)$'], np.nan, regex=True)

#Update columns to the right dtype (reservation_status_date to datetime and is_canceled to bool)

hotel_bookings["reservation_status_date"] = pd.to_datetime(hotel_bookings["reservation_status_date"])
hotel_bookings["is_canceled"] = hotel_bookings["is_canceled"].astype('bool')

#In a new column named 'arrival_date', connect the year, month and day of month to one neat datetime.  Then drop the year month and day column

from datetime import datetime

cols = ["arrival_date_year", "arrival_date_month", "arrival_date_day_of_month"]

hotel_bookings['arrival_date'] = hotel_bookings[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis=1)

hotel_bookings['arrival_date'] = pd.to_datetime(hotel_bookings["reservation_status_date"])

hotel_bookings.drop(["arrival_date_year", "arrival_date_month", "arrival_date_day_of_month"], axis=1, inplace=True)

#In a new col named 'direct_booking' fill with 'yes' if agent  and company are NaN values, else fill with no. Do this using a lambda

hotel_bookings['direct_booking'] = hotel_bookings[["agent", "company"]].apply(lambda x: "yes" if (pd.isnull(x[0]) and pd.isnull(x[1]))  else 'no', axis=1)

# children - NaN means zero children.  Will switch value to 0
# meal - Nan means no meal booked.  Will switch to "SC"
# agent - NaN means not booked through an agent.  Will switch to 0.00
# company - Nan means not booked through a company.  Will switch to 0.00

hotel_bookings['children'].fillna(0, inplace=True)

hotel_bookings['meal'].fillna("SC", inplace=True)

hotel_bookings["agent"].fillna(0.00, inplace=True)

hotel_bookings["company"].fillna(0.00, inplace=True)

#Once checked that no column has more than 70% Nan, replacing NaN with value preceding

# def find_nan(column):
#     nan_percentage = hotel_bookings[column].isnull().sum() * 100 / len(hotel_bookings[column]) 
#     print( f"{column} : {nan_percentage}" )

# for column in ["country", "market_segment", "distribution_channel"]:
#     find_nan(column)

hotel_bookings.fillna(method = 'bfill', inplace=True)

print(hotel_bookings.head())