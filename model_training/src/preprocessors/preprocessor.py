from typing import Dict, List
from keras.preprocessing import sequence
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
import pickle


class Preprocessor:
    tokenizer = Tokenizer()

    @staticmethod
    def preprocessor(reviews: Dict):

        Preprocessor.tokenizer.fit_on_texts(reviews['comment'])
        vocabulary_size = len(Preprocessor.tokenizer.word_counts)

        y_train = to_categorical(reviews['rating'], num_classes=3)
        x_tokenized = Preprocessor.tokenizer.texts_to_sequences(reviews['comment'])
        x_train = sequence.pad_sequences(x_tokenized, maxlen=100)

        return x_train, y_train, vocabulary_size

    @staticmethod
    def save_tokenizer():

        with open(r"tokenizer.pkl", "wb") as output_file:
            pickle.dump(Preprocessor.tokenizer, output_file)
