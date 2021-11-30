import nltk 
#download NLTK prelearned models
nltk.download([
    "names",
    "stopwords",
    "brown",
    "wordnet",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
])
from nltk.corpus import wordnet
from nltk.corpus import stopwords

#import spacy
import spacy
from spacy import displacy
from spacy.tokens import Span
import pandas

#download and loading spacy's models
spacy.cli.download("en_core_web_sm") 
NLP = spacy.load('en_core_web_sm')

import re

#constants for 
COLUMN_OF_LABEL_KEY_NAME = "total_label"
COLUMN_OF_PERSON_LABEL_KEY_NAME = "personal_label"
COLUMN_OF_SPAN_KEY_NAME = "span"
COLUMN_OF_TITLE_KEY_NAME = "title"

NLTK_LANGUAGE_KEY = "english"

'''
all text preprocessing and dataset file parsing
args: path for the dataset, dataset's rows limit
response: DataFrame from pandas Library, which contains all read data  
'''
def get_parsed_data(path_for_file: str, total_row_limit: int) ->  pandas.DataFrame:
    read_csv_data = pandas.read_csv(path_for_file).head(total_row_limit)
    return read_csv_data

'''
preprocessing text before nltk and spacy analysis
args: message for preprocessing 
response: preprocessed message in string format
'''
def get_preprocessed_message_text(message_text: str) -> str:
    def get_cleared_from_stop_words_text(message_text: str) -> str:
        filtered_message_text = " ".join([word for word in message_text.split()
                                         if word not in stopwords.words(NLTK_LANGUAGE_KEY)])
        return
    
    def get_removed_emoji_text(message_text: str) -> str:
        emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                    u"\U00002702-\U000027B0"
                                    u"\U000024C2-\U0001F251"
                                    "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', message_text)

    def get_removed_url_text(message_text: str) -> str: 
        url_pattern  = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        return url_pattern.sub(r'', message_text)

    message_text = " ".join(message_text.lower().split()) # removing all useless spaces
    message_text = get_cleared_from_stop_words_text(message_text) # removing all stop words
    message_text = get_removed_emoji_text(message_text) # removing all emojis
    message_text = get_removed_url_text(message_text) # removing all urls

    return message_text

#TODO: add spacy's labels connection
def get_label_from_data(message_text: str) -> str:
    pass

'''
saving pandas DataFrame to csv file
args: new dataset file name, DataFrame for saving
responce: None (cause why we need to return something if this is jus a function for saving data in .csv file) 
''' 
def load_data_to_csv(new_dataset_file_name: str, current_parsed_dataset: pandas.DataFrame, file_path: str = "") -> None:
    current_parsed_dataset.to_csv(file_path + new_dataset_file_name)

#get labels 
def get_personal_label_by_message(message_text: str) -> str:
    pass

#get total labels
def get_total_labels_by_message(message_text: str) -> str:
    pass

#main loop for processing data in dataset and load new columns 
def processing_on_dataset(parsed_dataset: pandas.DataFrame) -> None:
    parsed_dataset[COLUMN_OF_LABEL_KEY_NAME],
    parsed_dataset[COLUMN_OF_PERSON_LABEL_KEY_NAME],
    parsed_dataset[COLUMN_OF_SPAN_KEY_NAME] = " ", " ", " "

    for index_of_row, data_row in parsed_dataset.iterrows():
        message_text = get_preprocessed_message_text(data_row[COLUMN_OF_TITLE_KEY_NAME])
        parsed_dataset[COLUMN_OF_LABEL_KEY_NAME][index_of_row] = get_total_labels_by_message(message_text)
        parsed_dataset[COLUMN_OF_PERSON_LABEL_KEY_NAME][index_of_row] = get_personal_label_by_message(message_text)
    print(parsed_dataset)


def main():
    parsed_data = get_parsed_data(path_for_file=input("Enter the path for dataset file: \n"), total_row_limit=20000)
    processing_on_dataset(parsed_data)
    load_data_to_csv("answer.csv", parsed_data)
    print(parsed_data)

if __name__ == '__main__':
    main()