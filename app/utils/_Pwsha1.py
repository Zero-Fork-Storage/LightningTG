import hashlib

def pwhash(arg) -> str:
    return hashlib.sha1(arg.encode()).hexdigest()