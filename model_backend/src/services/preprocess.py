from typing import Dict, List
from keras.preprocessing import sequence
from ..model import TokenizerModel


class PreprocessorService:
    @staticmethod
    def process_texts(texts: List) -> List:
        tokenized_input = TokenizerModel.TOKENIZER.texts_to_sequences(texts)
        padded_input = sequence.pad_sequences(tokenized_input, maxlen=100)
        return padded_input
