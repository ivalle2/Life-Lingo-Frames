import pandas as pd
import requests
import statsmodels.api as sm
import numpy as np
import seaborn as sns
import opendatasets as od
import os
import json
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
    
    gift_file_path = "C:/Users/navak/Documents/GitHub/Life-Lingo-Frames/html-css-code/GIFT lingo_questions.txt"
    write_gift_questions(translation_dict, gift_file_path)


def write_gift_questions(translation_dict, filename='GIFT lingo_questions.txt'):
    # Clear the existing content in the file at the start of each run
    open(filename, 'w').close()

    # Extract keys and values for question generation
    english_words = list(translation_dict.keys())
    spanish_words = list(translation_dict.values())

    # Open the file for appending each question
    with open(filename, 'a', encoding='utf-8') as file:
        # Writing multiple-choice questions
        for i in range(3):  # Generating three MCQs
            correct_answer = english_words[i]
            spanish_word = translation_dict[correct_answer]
            incorrect_answers = [translation_dict[word] for word in english_words if word != correct_answer][:3]

            question_text = (
                f"::Which of the following is the correct translation for '{spanish_word}'?::\n"
                "{\n"
                f"={correct_answer} #Correct! \n"
            )
            for wrong in incorrect_answers:
                question_text += f"~{wrong} #Wrong. \n"
            question_text += "}\n\n"
            file.write(question_text)

        # Writing true/false questions
        for i in range(3, 6):  # Generating three TF questions
            correct_answer = english_words[i]
            spanish_word = translation_dict[correct_answer]
            question_text = (
                f"::True/False: '{spanish_word}' means '{correct_answer}'.::\n"
                "{T} #Correct! \n\n"
            )
            file.write(question_text)

        # Writing one matching question
        matching_question_text = (
            "::Match the following words::\n"
            "{\n"
        )
        for i in range(6, 9):  # Assuming at least 9 words in the dictionary
            english = english_words[i]
            spanish = translation_dict[english]
            matching_question_text += f"={english} -> {spanish}\n"
        matching_question_text += "}\n"
        file.write(matching_question_text)

main()


