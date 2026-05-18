while True:
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字"))
    op = input("请输入运算符(+ - * /)：")
    if op == '+':
        print("结果:",num1 + num2)
    elif op =='-':
        print("结果:",num1 - num2)
    elif op =='*':
        print("结果:",num1 * num2)
    elif op =='/':
        print("结果:",num1 / num2)
    else:
        print("无效运算符！")
    if input("继续计算？(y/n):").lower()!='y':
        print('再见')
        break
