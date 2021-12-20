import random
l1 = [1, 2, 3, 4, 5, 6,7,8]

print(random.choice(l1))

random.seed(5)
print(random.random())
print(random.random())


r1 = random.randint(5, 15)
print(r1)

print("Original  list",l1)
random.shuffle(l1)
print("Shuffled list",l1)

print ("Random number from 0-100 is : ",end="")
print (random.randrange(100))