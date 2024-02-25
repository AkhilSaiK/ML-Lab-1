features=[0,1,2,3,4,5,6,7,8,9]
output=[1,3,2,5,7,8,8,9,10,12]
def coeff(x,y):
    # sum(xi(xi-xmean))
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    
    ssx=0
    ssy=0
    for i in range(len(x)):
        ssx+=x[i]*(y[i]-y_mean)
        ssy+=x[i]*(x[i]-x_mean)
    c=ssx/ssy
    m=y_mean-c*x_mean
    return c,m

b1,b0=coeff(features,output)
print("b0 = ",b0)
print("b1 = ",b1)


x_test=features
y_test=output
y_pred=[0]*len(x_test)
sse=[0]*len(x_test)
for i in range(len(x_test)):
    y_pred[i]=b0+b1*x_test[i]
    sse[i]=(y_test[i]-y_pred[i])**2
    # print(x_test[i],"   ",y_pred[i],"    ",sse[i])
y_mean=sum(output)/len(output)
numerator=0
denominator=0
for i in range(len(features)):
    numerator+=((output[i]-y_pred[i])**2)
    denominator+=((output[i]-y_mean)**2)
r2=1-(numerator/denominator)

print("r2 value : ",r2)
print("Sum Squared Error : ",sum(sse))


