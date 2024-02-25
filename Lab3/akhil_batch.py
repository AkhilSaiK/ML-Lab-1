# Batch gradient descent
features=[0,1,2,3,4,5,6,7,8,9]
output=[1,3,2,5,7,8,8,9,10,12]
print("features : ",features)
print("output : ",output)
# y=bo+b1*x
b0=0
b1=0
learn_rate=0.001
mean=sum(features)/len(features)
num=len(output)
y_pred=[0]*num
sse=[0]*num
for i in range(1,51):
    total_error=0
    for j in range(num):
        y_pred[j]=b0+b1*features[j]
        error=output[j]-(y_pred[j])
        total_error+=error
        sse[j]=error**2
    b0=b0+learn_rate*(total_error)
    b1=b1+learn_rate*(total_error)*(mean)
    print("iteration : ",i)
    print("total error : ",total_error)
    print("b0 : ",b0)
    print("b1 : ",b1)
    # print(y_pred)
    print()
y_mean=sum(output)/len(output)
numerator=0
denominator=0
for i in range(len(features)):
    numerator+=((output[i]-y_pred[i])**2)
    denominator+=((output[i]-y_mean)**2)
r2=1-(numerator/denominator)
print("r2 value : ",r2)
print("sum squared error : ",sum(sse))
