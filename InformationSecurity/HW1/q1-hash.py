import hashlib

msg = b'If you want to keep a secret, you must also hide it from yourself'
m_sha256_hex = hashlib.sha256(msg).digest()
m_md5_hex = hashlib.md5(msg).digest()

remove_index = 0
edited_msg = msg[:remove_index] + msg[remove_index+1: len(msg)]

me_sha256_hex = hashlib.sha256(edited_msg).digest()
me_md5_hex = hashlib.md5(edited_msg).digest()

print('sha256\'s outputs:\n', m_sha256_hex.hex(), '\n', me_sha256_hex.hex(), '\n\n')
print('md5\'s outputs:\n', m_md5_hex.hex(), '\n', me_md5_hex.hex(), '\n\n')

# check changes on hash's output
sha256_diff = sum([bin(x ^ y).count('1') for x, y in zip(m_sha256_hex, me_sha256_hex)])
md5_diff = sum([bin(x ^ y).count('1') for x, y in zip(m_md5_hex, me_md5_hex)])

print('difference:')
print('    sha256: ', sha256_diff)
print('    md5   : ', md5_diff)

