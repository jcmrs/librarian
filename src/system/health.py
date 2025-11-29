from src.utils.responses import json_response

def check_health() -> dict:
    """
    Performs a basic system health check.
    """
    return json_response(
        status="success",
        data={"message": "System is operational"}
    )
