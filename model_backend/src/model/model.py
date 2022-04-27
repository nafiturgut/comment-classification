import keras
import os
from os.path import isfile, join


class TextModel:

    TEXT_MODEL = keras.models.load_model("./src/text_model")
