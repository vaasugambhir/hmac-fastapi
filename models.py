from pydantic import BaseModel


class HMACObject(BaseModel):
    key: str
    message: str
    source: str
    digest: str
