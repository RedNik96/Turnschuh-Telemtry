import hashlib
import json
import os

import hexdump
import requests

from datetime import datetime
from uuid import uuid4

from django.conf import settings

APPLICATION_ID = "6fe1ca16-c578-474e-a17d-e1f7970faa8f"
CERTIFICATE_VERSION_ID = "8f2c0d76-97e0-4393-be84-6e1079fdd5da"
# TODO: private-key nicht veröffentlichen
PRIVATE_KEY_PATH = os.path.join(settings.MEDIA_ROOT, 'turnschuh', 'privkey.pem')

def get_authorize_url():
    url = "https://agrirouter-qa.cfapps.eu10.hana.ondemand.com/application/{application_id}/authorize?response_type=onboard&state={state}".format_map({
        'application_id': APPLICATION_ID,
        'state': uuid4()
    })
    return url

def onboard(regcode):
    body_dict = {
        "id": "urn:turnschuh:1",
        "applicationId": APPLICATION_ID,
        "certificationVersionId": CERTIFICATE_VERSION_ID,
        "gatewayId": "3",
        "certificateType": "PEM",
        "UTCTimestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "timeZone": "+02:00"
    }

    json_body = json.dumps(body_dict)
    # json_body = json_body.encode()
    print('json_body: {}'.format(json_body))

    headers = {
        'Content-Type': 'application/json',
        'X-Agrirouter-ApplicationId': APPLICATION_ID,
        'Authorization': f'Bearer {regcode}',
        'X-Agrirouter-Signature': _create_onboard_signature(json_body)
    }

    # url = "https://agrirouter-registration-service-hubqa-eu10.cfapps.eu10.hana.ondemand.com/api/v1.0/registration/onboard/request"
    url = "https://agrirouter-registration-service-hubqa-eu10.cfapps.eu10.hana.ondemand.com/api/v1.0/registration/onboard/verify"

    print('--- pre-request ---')
    print(json_body)
    print(headers)

    req = requests.post(url, data=json_body, headers=headers)

    print('------------ req ----------------')
    print(req.status_code)
    print(req.text)


def _create_onboard_signature(body):
    from Cryptodome.Signature import pkcs1_15
    from Cryptodome.Hash import SHA256
    from Cryptodome.PublicKey import RSA

    key = RSA.import_key(open(PRIVATE_KEY_PATH).read())
    h = SHA256.new(body.encode())
    signature = pkcs1_15.new(key).sign(h)

    return signature.hex()


    """return ''

    import rsa
    content_bytes = open(PRIVATE_KEY_PATH).read().encode()
    print('type <-> bytes')
    print(type(content_bytes))
    key = rsa.PrivateKey.load_pkcs1(content_bytes, format='DER')
    signature = rsa.sign(body, key, 'SHA-256')
    print(signature)
    return signature


    from hashlib import sha256
    h = sha256(key=open(PRIVATE_KEY_PATH, 'rb').read(), digest_size=16)
    # hash = hashlib.new('sha256', body)
    signature = h.update(body).hexdigst()
    print(signature)
    return signature


    import jws
    signed = jws.sign({'alg': 'RS256'}, body, open(PRIVATE_KEY_PATH, 'rb').read())
    print(signed)
    return signed


    from jose import jws
    signed = jws.sign(body, open(PRIVATE_KEY_PATH, 'rb').read(), algorithm='RS256')
    print(signed)
    return signed



    print(type(body))"""

    from Cryptodome.Signature import pkcs1_15  # pip install pycryptodomex
    from Cryptodome.Hash import SHA256
    from Cryptodome.PublicKey import RSA
    from base64 import decodebytes, encodebytes

    private_key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgIZRq508OkigRwdzO4B85LFqbdVx3JX8VOd3VpiyQfQxYehZiq8E6CxhCwftfJGIIxEMmbs2kcrAhqwEQEggibqWGMsEU1UDwUMA61LipZ008zyUceo8Pwev2FrKqxCPuBg3OQc4iM8RaF27RlrFZ0BnpExbKilrUVfN1lUELqtrDuJEv/B7zVaom78scMFsCp4rs1AQfx82d7w9sghfVHBobg06cBaaRbMZGSVyDNIPFaNsZ60goJb7zL2kCpGLCR9YnaTZ4M2XJG/2iwNYjmg5gDSyYrmanXEgzjYgoslzw6oXK0J9k7rb6DpvhyDcmusysWtRT/xDrKaJMYIJZAgMBAAECggEAF25qdw0jRJTO77BAJPZnIzjSBlLxRY7zTlISG5fuB/OAWbb9rREIXHuwoF4dsAGVJcbAM7C9fx14F+kbpfQZhB5QMredCLUexDtwsXscjU9MHkSKX+UwJ2RfKHqQSMwcHNF+diqrZNZR2kP5B4qnJ2b7z57nNBp0KYNtNUyygKgTiYugyX86imy/FSifQAbmuQX53grrusFIjFQ5ifv0ydTg6S0EFvko6h2pUpd5cTezsbF1up/i+Md4Ss44IPTqTbxsetdfsViONS0zjtWmAeXqwhuznsNsoS+fzkb9J71H+qFwExcCiX+4Hr2kIUoT3v7WEpyTVqpHKeEVle+p7QKBgQDNp6FGr2xgEtS+b6Q/44hWWfU1d47lNSEFfIYvMBTh66Vvlvh/pKM3WE4RUD/95ViFkrg68Pp9SwmgOb7TyBaytToAnWRYYzLUTHlU+rHUqkrEDnKykrICTQX4sIDw0i8wTlcS2N3xHCcJ3CeXz7dOD8ip6WhmkRbRG57byiBx3QKBgQDHVPzA+otu7ybN6dLWXvQDPwMF2/jTTD+p4A138GmIYQbYzkNMYWrwm3TM6cn3uL6EZb2HNFD6rwWuSlIh1Ytg16alFkXNdxElAvKocSQh7WHhGxKsF1K/Pzpk82UFTXblOlOunxV7MjjvGgZOW8ClrrBiPnffYFGgV8mhULDQrQKBgQCN7njhvcP/8j8dRxOGfFPltKQEyIS4L5ignrZE7twap3U/tGPARDHYynrmfAoOAjC7zuyS0SkvO5BjIjdPFjKEF4r2TampTp0P48+BFJuSeAytjoMeNxvfdqT+Y2I50fV7UzXI7h8Ofi17IpO4tER//Wixy0KgNtYWbweODMujiQKBgCGLfuGnCFIJ8xjSEcY7worNTt/sjepZOZmH+BxIHCp0UaeoxpCTEGEfeD+H1JJYx88WJBgdyMb3L1iOb1X8TvFkOUos/mA+emclINsR90eyYDd2y+SkJCvFIzmb8FM9HxYig7SuVvodkJFEau1C6Z+4TzypUJkJ55K5U1hPcQIdAoGBAJFB4oBpYQgqm+LyfxccVhJ2/gcD83MowkFDCMi43xRRE6c51qe5eG/r/bSGEMyincsEcdv5EA8bn2e18sGrazY3umdRkXfL60fhHJRlITPsEzuR4EYGcbLkVlgKxj3b53RNjrPWxMbs/H8kBv1R8OEfw0TLaXAmsWZxjKGoBxBA
-----END PRIVATE KEY-----"""

    raw_string = body

    # private_key = RSA.importKey(decodebytes(private_key.encode()))
    private_key = RSA.importKey(private_key)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(SHA256.new(raw_string.encode()))
    print('-- signature --')
    print(signature)
    signature = encodebytes(signature).decode().replace("\n", "")
    print(signature)
    signature = hexdump.dump(signature.encode())
    print(signature)
    return signature