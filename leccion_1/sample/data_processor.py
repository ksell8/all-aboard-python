import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('ev_data.csv')
    print(df.head(1))