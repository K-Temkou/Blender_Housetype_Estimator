import random
from bing_hashing_image_downloader import downloader

# creating the datasets with available images from the internet
# i am using the bing_hashing_image_downloader in order to collect them through a search item and prevent any doubled images that might occur

downloader.download("new york skyscrapers flat iron", limit=150, output_dir='high_riseBuildingDatasettest')
downloader.download("skyscraper glass front facade", limit=150, output_dir='glassfrontBuildingDataset')
downloader.download("amsterdam dutch grachten house front view", limit=155, output_dir='Dutch_grachtenHouseDataset')
