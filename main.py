from fastapi import FastAPI
from users.routes import user
#from docs import tags_metadata

app = FastAPI(
  title="Zuccardi Rest API",
  description="",
  version="0.0.1",
  #openapi_tags=tags_metadata
)

app.include_router(user)