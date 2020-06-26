import uuid

a = str(uuid.uuid1()).split("-")
b = ("".join(a))
print("random string using a UUID module is "+b[:9])