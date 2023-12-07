import os

import pandas as pd


class FashionImagesDataset:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        print(os.listdir(self.data_dir))
        self.dataframe = self.get_data_frame()
        self.checkifvalid()

    # a dir is valid if it is not empty and has a csv and a folder of images called images
    def checkifvalid(self):

        if not os.path.isdir(self.data_dir):
            raise ValueError("Invalid directory path")
        if not os.path.exists(self.data_dir):
            raise ValueError("Directory does not exist")
        if not os.listdir(self.data_dir):
            raise ValueError("Directory is empty")
        if not os.path.exists(os.path.join(self.data_dir, "images")):
            raise ValueError("Directory does not contain images folder")

        # check if csv exists
        if not os.path.exists(os.path.join(self.data_dir, "styles.csv")):
            raise ValueError("Directory does not contain csv file")

        # check if csv is empty
        if os.stat(os.path.join(self.data_dir, "styles.csv")).st_size == 0:
            raise ValueError("csv file is empty")


        return True

    def __len__(self):
        return len(os.listdir(os.path.join(self.data_dir, "images")))



    def get_data_frame(self):
        return pd.read_csv(self.data_dir+"/styles.csv",on_bad_lines='skip')

# return a tuple of all values in the row of the csv
    def get_item(self, idx):
        return self.dataframe.iloc[idx]

    def get_image_path(self, idx):
        return os.path.join(self.data_dir, "images", str(self.get_item(idx)["id"])+".jpg")

if __name__ == "__main__":
    dataset = FashionImagesDataset("../../AI model/resources/myntradataset")

    print(dataset.get_item(0))

    print(dataset.get_image_path(0))