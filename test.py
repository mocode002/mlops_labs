import requests

url = "http://127.0.0.1:8000/predict"
data = {
            "tenure_months": 6,
            "num_complaints": 3,
            "avg_session_minutes": 12.5,
            "plan_type": "basic",
            "region": "AF",
            "request_id": "req-001"
        }

response = requests.post(url, json=data)
print(response.json())

print('#####################################################')

# GET /health
health_resp = requests.get("http://127.0.0.1:8000/health")
print("Health response:", health_resp.json())