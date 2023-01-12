# Tayyab Jafar
#In Class Activity #1 in Python
import gmpy2
# import mod inverse math in python

def mod_inverse(n, m):
  return gmpy2.invert(n, m)

def calculationsIfSame(A, B):  # formula if P = Q
  p1 = 3 * pow(A[0], 2) + a
  p2 = mod_inverse(2 * A[1], Z)
  lam = p1 * p2 % Z
  x_3 = (pow(lam, 2) - B[0]) - A[0]
  x_3 = x_3 % Z
  y_3 = ((-1) * lam * (x_3 - A[0]) - A[1]) % Z
  return x_3, y_3

def calculationsIfDifferent(A, B):  #formula if P != Q
  p1 = B[1] - A[1]
  p2 = B[0] - A[0]
  result = mod_inverse(p2, Z)
  lam = p1 * result % Z
  x_3 = (pow(lam, 2) - B[0]) - A[0]
  x_3 = x_3 % Z
  y_3 = ((-1) * lam * (x_3 - A[0]) - A[1]) % Z
  return x_3, y_3


# Starting Values:
a = 3  # a is the constant in the y^2 formula
Z = 17  # Z is the modulus space (Z_17)
A = (1, 3)  # A is the starting value
B = (10, 10)  # B is the starting value
q = 23 # given starting q.

# Custom Inputs:
# a = int(input("What is your a value?\n"))
# Z = int(input("What is your Z space value?\n"))
# Ax = int(input("What is your x-value for A coordinate (x1)\n"))
# Ay = int(input("What is your y-value for A coordinate (y1)\n"))
# A = (Ax,Ay);
# Bx = int(input("What is your x-value for B coordinate (x2)\n"))
# By = int(input("What is your y-value for B coordinate (y2)\n"))
# B = (Bx,By);
# q = int(input("What is your q value?\n"))


# starting signature of sig(x,k) of A;
r = int(input("What is your r value?\n"))
s = int(input("What is your s value?\n"))

sig = (r, s) #the sig

# hash h(x) = 8;
hash_of_x = 8

# calculate i and j values for ECDSA verification;
i = hash_of_x * mod_inverse(s, 23)
i = i % q
j = r * mod_inverse(s, q)
j = j % q

sig = (i, j)
print("(i,j) = ({}, {})".format(sig[0], sig[1]))

print("Calculate for {}A + {}B:".format(sig[0], sig[1]))

#Calculation for A:
print("")
print("Calculate for {}A".format(sig[0]))

# Calculate for A + A
Ax_3 = calculationsIfSame(A, A)[0]
Ay_3 = calculationsIfSame(A, A)[1]
A_r = (Ax_3, Ay_3)

# Calculate 2A + A and repeat until iA
amount_of_recursions = i - 2  # since we already did A+A
for i in range(amount_of_recursions):
  Ax_3 = calculationsIfDifferent(A, A_r)[0]
  Ay_3 = calculationsIfDifferent(A, A_r)[1]
  A_r = (Ax_3, Ay_3)

A_fr = A_r

print("{}A = ({}, {})".format(sig[0], A_fr[0], A_fr[1]))

#Calculations for B:
Bx_3 = calculationsIfSame(B, B)[0]
By_3 = calculationsIfSame(B, B)[1]
B_r = (Bx_3, By_3)

amount_of_recursions = j - 2  # since we already did B + B;

# Calculate 2B + B and repeat until jB
for i in range(amount_of_recursions):
  Bx_3 = calculationsIfDifferent(B, B_r)[0]
  By_3 = calculationsIfDifferent(B, B_r)[1]
  B_r = (Bx_3, By_3)

B_fr = B_r

print("")
print("Calculate for {}B".format(sig[1]))
print("{}B = ({}, {})".format(sig[1], B_fr[0], B_fr[1]))

#Calculations for iA * jB:
Ax_3 = calculationsIfDifferent(A_fr, B_fr)[0]
Ay_3 = calculationsIfDifferent(A_fr, B_fr)[1]

Result = (Ax_3, Ay_3)
print("")
print("Calculate for {}A * {}B".format(sig[0], sig[1]))
print("{}A * {}B = ({}, {})".format(sig[0], sig[1], Result[0], Result[1]))
print("ver(x,(r,s)) = true <=> u mod q = r")
print("r = {}".format(r))
print("u = {}".format(Result[0]))

if (Result[0] % q == r):
  print("Signature matches!")
else:
  print("Signature does not match!")

# Private Key (m) Calculation:
A = (1, 3)

# Calculate for A + A
Ax_3 = calculationsIfSame(A, A)[0]
Ay_3 = calculationsIfSame(A, A)[1]
A_r = (Ax_3, Ay_3)

# Calculate 2A + A and repeat until mA = B
amount_of_recursions = q - 2  # since we already did A+A
count = 2
# add the counter starting at 2 since we already did A+A
for i in range(amount_of_recursions):
  Ax_3 = calculationsIfDifferent(A, A_r)[0]
  Ay_3 = calculationsIfDifferent(A, A_r)[1]
  A_r = (Ax_3, Ay_3)
  count += 1
  if A_r == B:
    break
print("")
print("Bonus: Private key (m) = {}".format(count))
