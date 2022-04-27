from fastapi import FastAPI
from . import routers

app = FastAPI(
    debug=True,
    title="comment-classification",
    description=(
        "API for comment classification "
    ),
    version="0.61.0",
    docs_url="/docs"
)

for router in routers.__all__:
    app.include_router(**getattr(routers, router).__dict__)


@app.get("/")
def index():
    return f"{app.title} v{app.version}"


@app.get("/health")
async def health():
    return {"message": "healthy"}
