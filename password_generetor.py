import random
import string
import yaml

def id_generator(cls, size=16, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):

    return ''.join(random.choice(chars) for _ in range(size))





def password_generator(cls,size=10):
    char=string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+"123456789"
    passwd="".join(random.choice(char) for _ in range(size))
    print(passwd)
    return
password_generator(12)
