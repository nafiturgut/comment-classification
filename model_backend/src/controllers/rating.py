from fastapi import APIRouter
from ..services import RatingService, PreprocessorService
from ..validations import InputDataModel


class RatingController:
    router = APIRouter()

    # POST /rating/classify-texts
    @staticmethod
    @router.post('/classify-texts')
    async def classify_texts(comment: InputDataModel):
        processed_input = PreprocessorService.process_texts(list(comment.comment_text))
        return await RatingService.classify_texts(processed_input)
