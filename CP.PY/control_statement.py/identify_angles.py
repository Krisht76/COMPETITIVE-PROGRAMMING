##You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180.
A = int(input("Enter angle A: "))
B = int(input("Enter angle B: "))
C = int(input("Enter angle C: "))
if A + B + C == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
