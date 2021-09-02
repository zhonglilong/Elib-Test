# -*- coding:utf-8 -*-
import base64
import hashlib
import hmac
import urllib.parse


def md5_key(value):
    """ 禅道md5加密 """
    m = hashlib.md5()
    b = value.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


def hmac_key(secret, string_to_sign):
    """ 钉钉加密 """
    hmac_code = hmac.new(
        secret.encode('utf-8'),
        string_to_sign.encode('utf-8'),
        digestmod=hashlib.sha256).digest()
    return urllib.parse.quote_plus(base64.b64encode(hmac_code))
