# To import directly the functions inside your namespace:
#from project_template.make_dataset import download_data, rename_files
#from project_template.process_data import clean_data

# To import all the functions from a module:
from project_template import make_dataset
from project_template import process_data

if __name__ == '__main__':

    make_dataset.download_data()
    make_dataset.rename_files()
    process_data.clean_data()