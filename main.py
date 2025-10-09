from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db.database_model as database_model
from db.database import engine
from routes import file_routes, post_routes, products_routes, user_route

version = "v1"
app = FastAPI(title="Fastapi ",
              description="this is learning project.",
              version=version,)


database_model.Base.metadata.create_all(bind=engine)


app.include_router(products_routes.router,
                   prefix=f"/api/{version}/products", tags=['Products'])
app.include_router(file_routes.router,
                   prefix=f"/api/{version}/files", tags=['Files'])
app.include_router(user_route.router,
                   prefix=f"/api/{version}/users", tags=['Users'])
app.include_router(post_routes.router,
                   prefix=f"/api/{version}/posts", tags=["Posts"])

@app.get("/")
def greet():
    return {"message": "Hello, World!"}




   