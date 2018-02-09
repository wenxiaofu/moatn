#X1=N*2-100的合集
x1 = map(lambda i:i**2-100,range(1,100))

#X2=M*2-100-168的合集
x2 = map(lambda i:i**2-100-168,range(1,100))

#两个合集求并集结果
print(set(list(x1)) & set(list(x2)))