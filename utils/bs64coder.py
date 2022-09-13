import base64
def strEncoder(str):
	return base64.b64encode(str.encode('utf-8')).decode('utf-8')

def strDecoder(str):
    return base64.b64decode(str.encode('utf-8')).decode('utf-8')

if __name__ == '__main__':
    str = "test"
    a = strEncoder(str)
    print(a)
    print(strDecoder(a))