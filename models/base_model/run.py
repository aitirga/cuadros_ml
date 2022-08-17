from models.base_model.step_1_diggest_data import diggest_data
from models.base_model.step_2_preprocessing import preprocessing
from models.base_model.step_3_training import training
from scripts.webapp import CustomWebapp

if __name__ == '__main__':
    # Code to diggest data
    diggest_data.run()

    # Code to preprocess data
    preprocessing.run()

    # Code to train model
    training.run()

    webapp = CustomWebapp()
    webapp.run()







