import pandas as pd
import requests
import statsmodels.api as sm
import numpy as np
import seaborn as sns
import opendatasets as od
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Pre-adding Kaggle credentials to surpass download permission
os.environ['KAGGLE_USERNAME'] = 'navneethk'
os.environ['KAGGLE_KEY'] = 'aa629e0ddace435ec07eb2d585fa5006'

def main():
    
    # Scrapping the net to find a dataset
        
    api = KaggleApi()
    api.authenticate()

    dataset_path = 'lonnieqin/englishspanish-translation-dataset'
    file_name = 'data.csv'
        
    api.dataset_download_file(dataset_path, file_name, path='./')

    # Accessing the downloaded dataset from repository
    csv_file = "C:/Users/navak/Documents/GitHub/Life-Lingo-Frames/html-css-code/data.csv"
        
    df = pd.read_csv(csv_file)
    # Check if the file exists
    if os.path.exists(csv_file):
        # Return the CSV file
        return df
    else:
        print(f"File not found: {csv_file}")
    
    # Create translation dictionary 

    # Drop any duplicates and reset the index
    df_unique = df.drop_duplicates().reset_index(drop=True)

    # Create a dictionary with English as keys and Spanish as values
    translation_dict = pd.Series(df_unique['spanish'].values, index=df_unique['english']).to_dict()

    json_data = json.dumps(words)
    return json_data
main()