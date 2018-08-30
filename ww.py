import math
HP = int(input().split( )[0])
normal = float(input().split( )[0])
buffed = float(input().split( )[0])

if buffed >=2*normal:
    if HP % buffed ==0:
        print(int((HP / buffed)  * 2 ))

    else:
        print ((math.ceil(HP / buffed) -1)*2 +1)

else:
    print(math.ceil(HP / normal))
