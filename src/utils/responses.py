from datetime import datetime

def json_response(status: str, data: dict) -> dict:
    """Standardizes API responses."""
    return {
        "status": status,
        "payload": data,
        "timestamp": datetime.now().isoformat()
    }
