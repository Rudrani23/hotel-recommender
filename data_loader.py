import pandas as pd

# Column constants
STATE_COL = 'state'
CITY_COL = 'city'
HOTEL_COL = 'property_name'
STAR_COL = 'hotel_star_rating'
ADDRESS_COL = 'address'
REVIEW_COL = 'site_review_rating'

def load_data(filename='booking_com-travel_sample.csv'):
    df = pd.read_csv(filename)
    return df

def get_states(df):
    return sorted(df[STATE_COL].dropna().unique())

def get_cities(df, state):
    return sorted(df[df[STATE_COL] == state][CITY_COL].dropna().unique())

def get_hotels(df, state, city):
    return df[(df[STATE_COL] == state) & (df[CITY_COL] == city)][[
        HOTEL_COL, STAR_COL, ADDRESS_COL, REVIEW_COL
    ]]

