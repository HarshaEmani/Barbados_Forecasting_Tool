import json
from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware


#uvicorn Website.Backend.app:app --reload --host 0.0.0.0 --port 8000


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load and parse JSON files
def load_forecast_data():
	# Get path relative to script location
	script_dir = Path(__file__).resolve().parent  # Points to Backend/
	data_dir = script_dir.parent.parent / "Forecasts" / "2024-07-31"  # Points to root/Forecasts/2024-07-31
	forecast_data = []

	print(data_dir)

	for file_path in data_dir.glob("*.json"):
		try:
			with open(file_path, "r") as f:
				file_data = json.load(f)

			# Extract metadata from filename
			filename = file_path.stem
			parts = filename.split("_")
			location = "_".join(parts[:-3])  # Extract location name
			result_type = parts[-3]  # val or test

			forecast_data.append({**file_data, "location": location, "result_type": result_type, "filename": filename})
		except Exception as e:
			print(f"Error loading {file_path}: {str(e)}")

	return forecast_data


forecast_data = load_forecast_data()

# print(forecast_data)


# Response model
class ForecastResult(BaseModel):
	location: str
	result_type: str
	results: dict
	# metrics: dict
	filename: str


# API endpoint
# @app.get("/forecasts", response_model=List[ForecastResult])
# async def get_forecasts(location: Optional[str] = Query(None, description="Filter by location name"), result_type: Optional[str] = Query(None, description="'test' or 'val' results", regex="^(test|val)$")):
# 	filtered_data = forecast_data
# 	print(filtered_data)
#
# 	if location:
# 		filtered_data = [d for d in filtered_data if d["location"].lower() == location.lower()]
#
# 	if result_type:
# 		filtered_data = [d for d in filtered_data if d["result_type"] == result_type]
#
# 	return filtered_data

@app.get("/forecasts")
async def get_forecasts():
	print("I'm Here")
	return JSONResponse(content=load_forecast_data())

@app.get("/")
async def root():
    return {"message": "Hello World"}
