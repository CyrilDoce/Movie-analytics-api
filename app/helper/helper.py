import pandas as pd

data_file = "data/movie.csv"

def load_data():
    data = pd.read_csv(data_file)
    return data

def get_summary(data):
    df = data
    return {"title" : df["title"].to_list()}