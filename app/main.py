from fastapi import FastAPI
from app.controllers import auth_controller, company_controller, product_controller, todo_controller
from app.middlewares.time_middleware import add_process_time_header

version = "v1"
app = FastAPI(title="Company & Product API",
              description="in which user create their company",
              version=version
              )

app.middleware("")(add_process_time_header)
app.include_router(auth_controller.router,
                   prefix=f"/api/{version}/auth", tags=["Auth"])
app.include_router(company_controller.router,
                   prefix=f"/api/{version}/company", tags=["Company"])
app.include_router(product_controller.router,
                   prefix=f"/api/{version}/product", tags=["Product"])
app.include_router(todo_controller.router,
                   prefix=f"/api/{version}/todo", tags=["Todo"])
