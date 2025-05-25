import os
from kaggle.api.kaggle_api_extended import KaggleApi

os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')

api = KaggleApi()
api.authenticate()

# Download the datasets

# data_class.csv from the first dataset
api.dataset_download_files('jaswanthhbadvelu/canada-covid-19', path='covid_dataset/source_1', unzip=True) 

# covid_19_data_Canada.csv from the second dataset
api.dataset_download_files('mdmahmudferdous/novel-corona-virus-2019-datasetcanada', path='covid_dataset', unzip=True)

# Public_COVID-19_Canada.csv from the third dataset
api.dataset_download_files('zinx1991/covid19-in-canada', path='covid_dataset/source_2', unzip=True)