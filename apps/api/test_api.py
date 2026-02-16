import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api_endpoints():
    print("Testing Secure Task Management Backend API...")
    print("="*50)
    
    # Test root endpoint
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"[SUCCESS] Root endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"[ERROR] Root endpoint failed: {e}")
    
    # Test API documentation
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print(f"[SUCCESS] API Documentation available: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] API Documentation failed: {e}")
    
    # Test OpenAPI JSON
    try:
        response = requests.get(f"{BASE_URL}/openapi.json")
        openapi = response.json()
        print(f"[SUCCESS] OpenAPI spec available: {response.status_code}")
        print(f"  API Title: {openapi['info']['title']}")
        print(f"  API Version: {openapi['info']['version']}")
    except Exception as e:
        print(f"[ERROR] OpenAPI spec failed: {e}")
    
    # Test /api/tasks endpoints (should return 401 since no auth token provided)
    try:
        response = requests.get(f"{BASE_URL}/api/tasks")
        print(f"[SUCCESS] Tasks endpoint accessible: {response.status_code}")
        if response.status_code == 401:
            print("  Note: 401 Unauthorized is expected without JWT token")
    except Exception as e:
        print(f"[ERROR] Tasks endpoint failed: {e}")
    
    print("="*50)
    print("API testing completed!")

if __name__ == "__main__":
    test_api_endpoints()