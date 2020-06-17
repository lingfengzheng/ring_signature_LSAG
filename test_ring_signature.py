from linkable_ring_signature import ring_signature, verify_ring_signature

from ecdsa.util import randrange
from ecdsa.curves import *

number_participants = 4

x = [ randrange(SECP256k1.order) for i in range(number_participants)]
y = list(map(lambda xi: SECP256k1.generator * xi, x))
x_pi = x[0]

message = "Every move we made was a kiss"
message2 = "Every move we made was a kisss"
i = 0
signature = ring_signature(x_pi, 0, message, y)
signature2 = ring_signature(x_pi, 0, message, y)
# for j in y:
# 	print("valor de y: "+str(j))
# 	print("\n")
# for j in x:
#  	print("valor de x: "+str(j))

# print("\n")
# for i in signature:
# 	print("Signature: "+str(i))

# for i in signature2:
# 	print("Signature2: "+str(i))

print(verify_ring_signature(message, y, *signature))
print(verify_ring_signature(message2, y, *signature))
