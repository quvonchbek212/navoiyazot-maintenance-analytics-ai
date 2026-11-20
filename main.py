"""Navoiyazot Logistics: Breakdown Report & Predictive Maintenance Service."""
import logging
import uvicorn
from fastapi import FastAPI
from breakdown_report.router import router as breakdown_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

app = FastAPI(
    title="Navoiyazot Logistics · Breakdown Report API",
    description="Fleet failure analytics, reliability engineering metrics, and predictive maintenance risk scoring for Navoiyazot.",
    version="1.0.0"
)

app.include_router(breakdown_router)

@app.get("/healthz", tags=["Health"])
async def healthz():
    return {"status": "ok", "service": "breakdown-report"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=False)
