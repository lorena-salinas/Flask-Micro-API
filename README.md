# Flask-Micro-API

A simple Flask REST API that serves car data from `cars.csv` as JSON,
tested with Python `requests`.

## Project structure
| File | Purpose |
|---|---|
| `flaskWebApp.py` | The Flask API (all routes) |
| `client.py` | Tests the API with Python `requests` (GET + POST) |
| `cars.csv` | Car dataset loaded with pandas |
| `requirements.txt` | Libraries to install |

## Endpoints
| Method | Route | What it does |
|---|---|---|
| GET | `/hello` | Welcome message in JSON |
| GET | `/api/health` | Health check: `{"status": "OK"}` |
| GET | `/data` | All cars |
| POST | `/data` | Adds a new car (needs `CarName` and `price`) |
| GET | `/data/<id>` | One car by its `car_ID` |
| GET | `/data/first10` | The first 10 cars |

Example POST body:
```json
{ "CarName": "tesla model 3", "price": 42990 }
```
