import datetime
import hashlib
import random


def orderIdGenerator():
    x = datetime.datetime.now()
    yy = x.strftime("%Y")
    mm = x.strftime("%m")
    dd = x.strftime("%d")
    hh = x.strftime("%H")
    mm = x.strftime("%M")
    ss = x.strftime("%S")

    id=yy+mm+dd+hh+mm+ss
    return id


def order_redeem_codeGenerator(name,ph_no,orderId,nonce):
    str_text = name + str(ph_no) + str(orderId) + str(nonce)
    str_text = str_text.encode('utf-8')
    hashed_text = hashlib.sha1(str_text)
    hashed_text = hashed_text.hexdigest()

    return hashed_text



def nonceGenerator():
    r1 = random.randint(0,1000)
    r2 = random.randint(r1,r1+1000)
    n = random.randint(r1,r2+1)

    return n