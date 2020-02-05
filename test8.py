number=7
guess=3
while guess!=number:
  guess=int(input("请输入你猜测的数字"))
  if guess==number:
    print("恭喜你猜对了，答案为{}".format(number))
    break
  elif guess<number:
    print("你猜的数值{}偏小了，请继续猜测".format(guess))
  elif guess>number:
    print("你猜的数值{}偏大了，请继续猜测".format(guess))
