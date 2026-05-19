import requests
import json
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/search")
def get_description(search: str = ''):
    try:
        # Send GET request
        response = requests.get('https://my-json-server.typicode.com/typicode/demo/comments', timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)

        # Convert JSON to Python dict
        data_list =json.loads(response.text) # requests automatically parses JSON
        results = []
        for item in data_list:
            if isinstance(item, dict) and 'body' in item and item['body'] == search:
                results.append(item)
        return results
            
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError as e:
        print(f"JSON parsing error: {e}")
        return None
    