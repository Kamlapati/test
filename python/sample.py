def string_2_hex(text):
    return "".join("{:02X}".format(ord(c)) for c in text)


def xor_2_equal_hex(t1, t2):
    xor_hex = (int(t1,16) ^ int(t2, 16))
    xor_hex = hex(xor_hex).rstrip("L").lstrip("0x") or "0"
    return xor_hex

def  repeating_key_xor(input_text, key):
    input_text_hex = string_2_hex(input_text)
    new_key=""
    for i in range(len(input_text)/len(key)):
        new_key= new_key + key
    diff  = len(input_text) -len(new_key)
    if diff:
        new_key = new_key + key[:diff]
    key_hex =  string_2_hex(new_key)
    xor_keyed = 0
    if len(key_hex) == len(input_text_hex):
        xor_keyed = xor_2_equal_hex(input_text_hex,key_hex)
    return xor_keyed
