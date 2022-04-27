import json
import pickle


class TokenizerModel:

    TOKENIZER = pickle.load(open('tokenizer.pkl', 'rb'))

