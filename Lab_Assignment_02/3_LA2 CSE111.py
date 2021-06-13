def addition(minimum,maximum,divisor):
    sum=0
    for i in range(minimum,maximum,+divisor):
        sum+=i
    print(sum)


MIN=int(input())
MAX=int(input())
div=int(input())

addition(MIN, MAX, div)