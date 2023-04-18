yn=list((input("Enter your full name: ")).lower())
ln=list((input("Enter your crush's full name: ")).lower())
un=[]
fls=list("flames")
for i in yn:
    if i in ln:
        ln.remove(i)
    else:
        un.append(i)
for i in ln:
    un.append(i)
for i in un:
    if i==" ":
        un.remove(i)
while len(fls)>1:
    num=len(un)
    if num>len(fls):
        num%=len(fls)
    fls.remove(fls[num-1])
    if num>0:
        l1=fls[num-1:]
        l2=fls[:num-1]
        fls=l1+l2
print(" ")
print("Calculating FLAMES for you......")
print(" ")
if fls[0]=="f":
    print("Your crush will be a good Friend to you..!")
elif fls[0]=="l":
    print("Your crush has love on you ;)")
elif fls[0]=="a":
    print("Your crush has affection on you :)")
elif fls[0]=="m":
    print("Plan your wedding soon guys! Don't forget to invite me XO")
elif fls[0]=="e":
    print("It is better to stay away from your crush. They could be your worst enemy :O")
elif fls[0]=="s":
    print("You both are meant to be brothers and sisters :(")
