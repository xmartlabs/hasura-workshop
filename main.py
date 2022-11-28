from typing import Union, Any
from hasura import HasuraActionRequest
from fastapi import Request
import jwt


from fastapi import FastAPI

app = FastAPI()


@app.post("/purchase")
def create_purchase(request: Request):
    return {'result': "Purchase Created"}

@app.get("/auth/validate")
def validate(request: Request):
    if not request.headers.get('Authorization'):
        user_id = '0'
        user_role = 'anonymous'
    else:
        payload = jwt.decode(request.headers['Authorization'][7:], algorithms='RS256', options={"verify_signature": False})
        user_id = payload['id']
        user_role = payload['role']
    return {
        "X-Hasura-User-Id": user_id,
        "X-Hasura-Role": user_role,
        "X-Hasura-Is-Owner": "true",
        "X-Hasura-Custom": "custom value"
    }

@app.post("/notify-new-pizza")
def sent_email(request: Request):
    return "Email sent"