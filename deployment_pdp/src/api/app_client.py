"""
    FastAPI module

    References:
        https://realpython.com/fastapi-python-web-apis/
        https://chatgpt.com/share/67ac75aa-c828-8005-867d-6a54c09396ab

    Future Questions:
        https://stackoverflow.com/questions/77476105/can-pydantic-model-dump-return-exact-type
"""


# from typing import Optional

from fastapi import APIRouter, FastAPI, HTTPException, Request
from pydantic import BaseModel
# from gateway_api.routes import router as gateway_router

# from ml_client import call_ml_model
# from ml_postprocessing import process_model_output

app = FastAPI()
router = APIRouter()
app.include_router(router)


class YelpReview(BaseModel):
    data: str
    # description: Optional[str] = None  # Need to use Optional for default values or pydantic will throw an error


@app.post("/predict")
def handle_request(review: YelpReview):
    try:
        # data = review.model_dump()
        # # Step 1: Call the ML model
        # model_output = call_ml_model(data)
        # # Step 2: Process the output
        # final_result = process_model_output(model_output)
        # # Step 3: Return the result to the frontend
        # return {"result": final_result}
        return {"result": 5}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
