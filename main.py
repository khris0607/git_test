import random

value_1 = random.randint(1,6)
value_2 = random.randint(1,6)
value_3 = random.randint(1,6)
value_4 = random.randint(1,6)



if value_1  + value_2 > value_3 + value_4:
    print("Виграв перший гравець")

elif value_1  + value_2 < value_3 + value_4:
    print("Виграв другий гравець")

else:
    print("Нічія")