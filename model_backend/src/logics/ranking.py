from typing import List
from ..model import TextModel
import numpy as np


class Ranking:
    @staticmethod
    async def get_ranks(text: List):
        result = {
            "rating": int(np.argmax(TextModel.TEXT_MODEL.predict(text)))
        }
        return result

