"""Main function for running the API."""
import uvicorn
from src import create_application

app = create_application()

if __name__ == "__main__":
    # Run the FastAPI application on a Uvicorn server
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

