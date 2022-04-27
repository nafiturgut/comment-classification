from pydantic import BaseModel, Field
from typing import List


class InputDataModel(BaseModel):
    comment_text: List = Field(alias="commentText")
