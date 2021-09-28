from fastapi import FastAPI
from users.routes import user
from estaciones.routes import estaciones
#from docs import tags_metadata

app = FastAPI(
  title="Zuccardi Rest API",
  description="Prueba de FastApi orientado a sistema Zuccardi",
  version="0.0.1",
  #openapi_tags=tags_metadata
)

app.include_router(user)
app.include_router(estaciones)