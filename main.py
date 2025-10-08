from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database_model
from database import engine
from routes import file_routes, products_routes, user_route

version = "v1"
app = FastAPI(title="Fastapi ",
              description="this is learning project.",
              version=version,)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

database_model.Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(products_routes.router,
                   prefix=f"/api/{version}/products", tags=['Products'])
app.include_router(file_routes.router,
                   prefix=f"/api/{version}/files", tags=['Files'])
app.include_router(user_route.router,
                   prefix=f"/api/{version}/users", tags=['Users'])


@app.get("/")
def greet():
    return {"message": "Hello, World!"}
