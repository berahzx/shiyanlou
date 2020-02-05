num=int(input("请输入一个数值"))
if num%2==0:
  if num%3==0:
    print("{}数值即可整除2，也能整除3".format(num))
  else:
    print("{}数值只能整除2，不能整除3".format(num))
else:
  if num%3==0:
    print("{}数值只能整除3，不能整除2".format(num))
  else:
    print("{}数值即不能整除2，也不能整除3".format(num))
