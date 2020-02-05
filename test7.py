age=int(input("please input age:"))
if age<=0:
  print("你是在逗我吧")
elif age==1:
  print("你家狗14岁")
elif age==2:
  print("你家狗22岁")
elif age>2:
  ha=22+(age-2)*5
  print("你家狗{}岁".format(ha))
input("请输入enter键退出")
