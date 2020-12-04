# Lambda function syntax is :   functionObject = lambda arguments:expression

sq = lambda num:num*num
result = sq(10)
print(result)

output = lambda a,b,c:2*a+3*b+4*c
result = output(3, 5, 6)
print(result)