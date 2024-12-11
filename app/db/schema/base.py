from datetime import datetime

class BaseReponse:
    def __init__(self, status_code: int, timestamp: datetime,data:object,message: str):
        self.status_code = status_code
        self.timestamp = timestamp
        self.data = data
        self.message = message