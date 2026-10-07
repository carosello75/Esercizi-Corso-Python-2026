# lista[a:b]

messaggi = ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10"]

"""
print(messaggi[0:3])
print(messaggi[2:])
print(messaggi[:2])

print(messaggi[-2:])

print(messaggi[:])
"""

QUANTI_MESSAGGI = 7

messaggi_pre = messaggi[0:QUANTI_MESSAGGI]
messaggi_post = messaggi[QUANTI_MESSAGGI:]

print(messaggi_pre)
print(messaggi_post)
