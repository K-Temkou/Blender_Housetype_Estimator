import os
from os import listdir

# renaming the files gathered from scraping the web in order to prepare for target assignment

for f in listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\glassfrontBuildingDataset\skyscraper glass front facade/"):

    os.rename(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\glassfrontBuildingDataset\skyscraper glass front facade/" + f,
              r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\glassfrontBuildingDataset\skyscraper glass front facade/glassfront" + f)

for f in listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\Dutch_grachtenHouseDataset\amsterdam_dutch_grachten_house_front_view/"):

    os.rename(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\Dutch_grachtenHouseDataset\amsterdam_dutch_grachten_house_front_view/" + f,
              r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\Dutch_grachtenHouseDataset\amsterdam_dutch_grachten_house_front_view/dutch_house" + f)

for f in listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\high_riseBuildingDatasettest\new_york_skyscrapers_flat_iron/"):

    os.rename(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\high_riseBuildingDatasettest\new_york_skyscrapers_flat_iron/" + f,
              r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\high_riseBuildingDatasettest\new_york_skyscrapers_flat_iron/highrise_building" + f)
