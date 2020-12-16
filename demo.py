print("hello")
try:
    score=(float(input("enter the score")))
    if score>1.0 or score<0.0:
        print("error")
    else:
        if score>=0.9:
            print("grade A")
        elif score>=0.8 and score<0.9:
            print("grade B")
        elif score>=0.7 and score<0.8:
            print("grade C")
        elif score>=0.6 and score<0.7:
            print("grade D")
        else :
            print("grade F")
except:
    print("bad input")

#temp= float(input('enter temperature in celsius'))
#fhartemp= (temp-32)*5/9
#print('the fhar temp is',fhartemp)



#inr=input("enter rate")
#inh=input("enter  hours")
#hours=float(inh)
#rate=float(inr)
#gross=(hours*rate)
#print("gross is",gross)
