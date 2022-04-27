from .router import Router
from ..controllers.rating import RatingController

rate_route = Router(router=RatingController.router, prefix='/rating')

__all__ = [
    "rate_route"
]
