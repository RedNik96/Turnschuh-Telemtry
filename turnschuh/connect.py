from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA


def create_signature(message):
    key = RSA.import_key(open('/home/rednik/Development/test-hash-hex/privkey.pem').read())
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)
    print(f'type of the signature: {type(signature)}')
    return signature


def verify_signature(message, signature):
    signature = bytes.fromhex(signature)
    print(f'Signature from hex {signature}')
    key = RSA.import_key(open('/home/rednik/Development/test-hash-hex/pubkey.pem').read())
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        print("The signature is valid.")
    except (ValueError, TypeError):
        print("The signature is not valid.")


if __name__ == '__main__':
    content = b"{'content': 'valides JSON'}"
    print(f'content: {content}')

    signature = create_signature(content)
    print(f'signature: {signature}')
    print(f'signature as hex: {signature.hex()}')

    verify_signature(content, signature.hex())