print("Tic Tac Toe!!!!")
t=0
print(" 1 | 2 | 3\n---|---|---\n 4 | 5 | 6\n---|---|---\n 7 | 8 | 9 ")
p1=input("Player's 1 Name?:")
p2=input("Player's 2 Name?:")
print("Welcome", p1 ,"(X) and", p2 ,"(O)\n Let the Game begin!!!")
t1=1
t2=2
t3=3
t4=4
t5=5
t6=6
t7=7
t8=8
t9=9
t=0
while t<=8:
    a=int(input("Choose the number to put x:"))
    if a==t1:
        t1='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t2:
        t2='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t3:
        t3='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t4:
        t4='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t5:
        t5='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t6:
        t6='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t7:
        t7='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t8:
        t8='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if a==t9:
        t9='x'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if (t1=='x' or t1=='o')and(t2=='x' or t3=='o')and(t4=='x' or t4=='o')and(t5=='x' or t5=='o')and(t6=='x' or t6=='o')and(t7=='x' or t7=='o')and(t8=='x' or  t8=='o')and(t9=='x' or  t9=='o'):        
        t=9
        break
    if (t1==t2==t3) or (t4==t5==t6) or (t7==t8==t9) or (t1==t4==t7) or (t2==t5==t8) or (t3==t6==t9) or(t1==t5==t9) or (t3==t5==t7):
        t=9
        break
    b=int(input("Choose the number to put o:"))
    if b==t1:
        t1='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t2:
        t2='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t3:
        t3='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t4:
        t4='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t5:
        t5='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t6:
        t6='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t7:
        t7='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t8:
        t8='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if b==t9:
        t9='o'
        print("\n",t1," |", t2 ," |",t3,"\n ---|----|---\n",t4," |",t5," |",t6,"\n ---|----|---\n",t7," |",t8," |",t9)
    if (t1==t2==t3) or (t4==t5==t6) or (t7==t8==t9) or (t1==t4==t7) or (t2==t5==t8) or (t3==t6==t9) or(t1==t5==t9) or (t3==t5==t7):
        t=9
        break
print("Game over!!!")
if (t1==t2==t3=='x') or (t4==t5==t6=='x') or (t7==t8==t9=='x') or (t1==t4==t7=='x') or (t2==t5==t8=='x') or (t3==t6==t9=='x') or(t1==t5==t9=='x') or (t3==t5==t7=='x'):
    print("Congratulations!!",p1 , "You won")
elif (t1==t2==t3=='o') or (t4==t5==t6=='o') or (t7==t8==t9=='o') or (t1==t4==t7=='o') or (t2==t5==t8=='o') or (t3==t6==t9=='o') or(t1==t5==t9=='o') or (t3==t5==t7=='o'):
    print("Congratulations!!",p2 , "You won")
else:
    print("Game draw")