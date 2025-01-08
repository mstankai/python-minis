import pandas as pd
import os
from datasets import load_dataset, load_dataset_builder
import requests

def get_hf_dataset(path: str) -> pd.DataFrame:
    print("Downloading data...")
    df = pd.read_csv(path, index_col=0)  
    print(f"Data shape: {df.shape}")
    return df

def get_hf_dataset_readme(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        readme = response.text
        print("README fetched successfully")
        return readme

    print(f"Failed to fetch the README file. Status code: {response.status_code}")
    return ""

def save_dataset(df: pd.DataFrame, out_path: str):
    df.to_csv(out_path, index=False, encoding="utf-8")
    print(f"Dataset saved to {out_path}")

def save_readme(readme: str, out_path: str):
    with open(out_path, "w", encoding="utf-8") as file:
        file.write(readme)
    print(f"README saved to {out_path}")

def main():
    data_path = "hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv"
    df = get_hf_dataset(data_path)

    readme_url = "https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/raw/main/README.md"
    readme = get_hf_dataset_readme(readme_url)

    out_folder = "data"
    out_file = "spotify_tracks"
    os.makedirs(out_folder, exist_ok=True)
    outpath = os.path.join(out_folder, out_file)

    save_dataset(df, f"{outpath}.csv")
    save_readme(readme, f"{outpath}.txt")

if __name__ == "__main__":
    main()