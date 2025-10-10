from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import auth_controller, company_controller, product_controller


Base.metadata.create_all(bind=engine)
version = "v1"
app = FastAPI(title="Company & Product API",
              description="in which user create their company",
              version=version
              )

app.include_router(auth_controller.router,
                   prefix=f"/api/{version}/auth", tags=["Auth"])
app.include_router(company_controller.router,
                   prefix=f"/api/{version}/company", tags=["Company"])
app.include_router(product_controller.router,
                   prefix=f"/api/{version}/product", tags=["Product"])


@app.get("/")
def root():
    return {"message": "Welcome to Company API!"}


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import db.database_model as database_model
# from app.database import engine
# from routes import file_routes, post_routes, products_routes, user_route

# version = "v1"
# app = FastAPI(title="Fastapi ",
#               description="this is learning project.",
#               version=version,)


# database_model.Base.metadata.create_all(bind=engine)


# app.include_router(products_routes.router,
#                    prefix=f"/api/{version}/products", tags=['Products'])
# app.include_router(file_routes.router,
#                    prefix=f"/api/{version}/files", tags=['Files'])
# app.include_router(user_route.router,
#                    prefix=f"/api/{version}/users", tags=['Users'])
# app.include_router(post_routes.router,
#                    prefix=f"/api/{version}/posts", tags=["Posts"])

# @app.get("/")
# def greet():
#     return {"message": "Hello, World!"}
