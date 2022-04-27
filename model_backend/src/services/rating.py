from typing import Dict, List

from ..logics import Ranking


class RatingService:
    @staticmethod
    async def classify_texts(text: List) -> Dict:
        return await Ranking.get_ranks(text)
