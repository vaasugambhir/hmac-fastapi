import hashlib


def custom_hash(message: str):
    '''
        Custom hash function, a combination of known hash functions
        input -> message: string
        returns -> digest: string
    '''
    message = str(hashlib.md5(message.encode()).hexdigest())
    message = str(hashlib.sha512(message.encode()).hexdigest())
    message = str(hashlib.sha256(message.encode()).hexdigest())
    return message


def hmac(message: str, key: str, source: str, block_len: int):
    '''
        Function to carry out HMAC process
        input -> message: string, source: string, block_len: integer
        returns -> digest: string
    '''
    # translation values for input and output padding
    ipad_translator = str((x ^ 0x5C) for x in range(256))
    opad_translator = str((x ^ 0x36) for x in range(256))

    # zero padding to length = block_length (64 in our case)
    zero_padded_key = key.ljust(block_len, '0')

    # translating with ipad and opad sequence
    ipad = zero_padded_key.translate(opad_translator)
    opad = zero_padded_key.translate(ipad_translator)

    # concatenating the message with ipad and source
    message1 = ipad + message + source
    hash1 = custom_hash(message=message1)
    print(f'Intermediate digest: {hash1}')

    # concatenating message with opad and intermediate digest
    message2 = opad + hash1
    hash2 = custom_hash(message=message2)
    print(f'Final digest: {hash2}')
    return hash2
