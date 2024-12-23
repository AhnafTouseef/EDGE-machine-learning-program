number=100

fib=[0,1]

if number<=0:
    print('Invalid')

elif number==1:
    print('Fibonacci sequence\n',[0])
    print('Sum is 0')
else:
    for i in range(number-2):
        fibns = fib[-1] + fib[-2]
        fib.append(fibns)
    print(fib)
    Sum=sum(fib)
    print('\nSum is ',Sum)
