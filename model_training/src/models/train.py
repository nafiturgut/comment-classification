from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding


class Model:
    @staticmethod
    def generate_model(vocabulary_size: int):
        model = Sequential()
        model.add(Embedding(vocabulary_size + 1, 100, input_length=100))
        model.add(LSTM(50, return_sequences=True))
        model.add(LSTM(50))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(3, activation='softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
