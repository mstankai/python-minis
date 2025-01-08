import pandas as pd

def clean_data(df: pd.DataFrame):
    df.dropna(inplace=True, axis=0)
    df.drop_duplicates(inplace=True)



def main():
    input_path = "data/spotify_tracks"
    input_data = f"{input_path}.csv"
    input_readme = f"{input_path}.txt"

    df = pd.read_csv(input_data)
    print(df.head())


if __name__ == "__main__":
    main()