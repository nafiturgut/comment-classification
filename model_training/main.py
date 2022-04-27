from src import models
from src import preprocessors
import pandas as pd


def main():
    reviews = pd.read_csv('.data/random_reviews.csv')
    x_train, y_train, vocabulary_size = preprocessors.Preprocessor.preprocessor(reviews)
    model = models.Model.generate_model(vocabulary_size)
    model.fit(x_train, y_train, batch_size=128, epochs=20, verbose=1)
    model.save("text_model")


if __name__ == 'main':
    main()
