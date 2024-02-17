from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routers import bill, price_consumption, tip

app = FastAPI(
    title="HackUDC 2024 - Backend",
    description="Backend for HackUDC 2024",
    docs_url='/docs',
    redoc_url='/redoc',
    version="0.1.0",
)
app.include_router(bill.router)
app.include_router(price_consumption.router)
app.include_router(tip.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
def root():
    return RedirectResponse(url='/docs')
