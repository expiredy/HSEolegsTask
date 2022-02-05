from pandas import DataFrame, read_csv 
import os

def get_loaded_data_from_csv(filename: str) -> DataFrame:
    return read_csv(filename)


def main():
    static_dataset_path = "./NTO_AI_butcamp_thing/football.csv"
    read_data_frame = get_loaded_data_from_csv(static_dataset_path)
    


if __name__ == '__main__':
    main()