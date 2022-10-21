from fastapi import FastAPI
from constants import block_len
from utils import hmac
from models import HMACObject

app = FastAPI()


@app.get('/')
def hello_world():
    '''
        Test API call
    '''
    return {'status': 200, 'message': 'Hello world'}


@app.post('/get-digest')
def get_digest(obj: HMACObject):
    '''
        API to get digest
        request -> source: string, key: string, message: string
        response -> digest: string
    '''
    return {'digest': hmac(obj.message, obj.key, obj.source, block_len)}


@app.post('/verify-digest')
def verify_digest(obj: HMACObject):
    '''
        API to verify if digest is same
        request -> source: string, key: string, message: string, digest: str,
        response -> if the user is verified or not
    '''
    digest = hmac(obj.message, obj.key, obj.source, block_len)
    print(f'Client digest: {obj.digest}')
    print(f'Server digest: {digest}')
    if digest == obj.digest:
        return {'message': 'HMAC verification complete!'}
    else:
        return {'message': 'HMAC verification incomplete'}
