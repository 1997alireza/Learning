import pyDes
import struct


def int_to_bytes(value, length):
    result = []

    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)

    result.reverse()

    return result


msg = int_to_bytes(0x0123456789ABCDEF, 8)
key = int_to_bytes(0x133457799BBCDFF1, 8)

des = pyDes.des(key)
m_des_hex = des.encrypt(msg)
print(m_des_hex.hex())

