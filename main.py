import random
num_s7i7_max = int(input("Chnowwa el max mta3 noumrou es7i7:"))
kaddech_mn_mrra = int(input("9addech men marra ? "))
rbaht=False
num_s7i7=random.randint(0,num_s7i7_max)
for i in range(0,kaddech_mn_mrra):
    noumrouk= int(input("aatini noumrouk: "))
    if num_s7i7 == noumrouk:
        rbaht=True
        break
    else:
        print("loser")
if rbaht:
    print("sa7itekk")
    print("jibtha fi",i+1,"/",kaddech_mn_mrra)
else:
    print("Game Over ")
    

    
    
