fig = plt.figure()
lowerBoundVal = 10
c1 = lowerBoundVal;c2 = lowerBoundVal;c3 = lowerBoundVal
cap = 15

for var in variants:
    print(c1,c2,c3)
    ax1 = fig.add_subplot(c1,c2,c3)
    ax1.imshow( var )

    if(c3 >= cap):
        c2+=1
        if(c2 > cap):
            c2 = lowerBoundVal
            c1+=1
    else:
        c3+=1