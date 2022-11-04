import hashlib


def custom_hash(message: str):
    '''
        Custom hash function, a combination of known hash functions
        input -> message: string
        returns -> digest: string
    '''
    message = str(hashlib.sha1(message.encode()).hexdigest())
    message = str(hashlib.sha256(message.encode()).hexdigest())
    return message


def sxor(s1: str, s2: str):
    '''
        Function that computes the XOR of two strings
        input -> s1: str, s2: str
        returns -> xor of s1 and s2: str
    '''
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def hmac(message: str, key: str, source: str, block_len: int):
    '''
        Function to carry out HMAC process
        input -> message: string, source: string, block_len: integer
        returns -> digest: string
    '''

    # zero padding to length = block_length (64 in our case)
    zero_padded_key = key.ljust(block_len, '0')

    it = ''
    ot = ''
    for i in range(block_len):
        it += str(0x5C)
        ot += str(0x36)

    # translating with ipad and opad sequence
    ipad = sxor(it, zero_padded_key)
    opad = sxor(ot, zero_padded_key)

    # concatenating the message with ipad and source
    message = message.rjust(block_len, '0')
    source = source.rjust(block_len, '0')
    message1 = ipad + message + source
    hash1 = custom_hash(message=message1)
    print(f'Intermediate digest: {hash1}')

    # concatenating message with opad and intermediate digest
    hash1 = hash1.rjust(block_len, '0')
    message2 = opad + hash1
    hash2 = custom_hash(message=message2)

    print(f'Final digest: {hash2}')
    return hash2
