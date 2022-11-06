##########################################
import io
import sys

_INPUT = """\


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = "13 DUP 4 POP 5 DUP + DUP + -"

def solution(expression):
    stack = []
    for i in expression.split(' '):
        if i == '+' and len(stack)>=2:
            # +のときはスタックから2つ取り出して加算し，再度格納する
            b, a = stack.pop(), stack.pop() #後の演算のために順序を整えている
            stack.append(a + b)

        elif i == '-' and len(stack)>=2:
            # -のときはスタックから2つ取り出して減算し，再度格納する
            b, a = stack.pop(), stack.pop() #後の演算のために順序を整えている
            stack.append(b - a)

        elif i == 'DUP':
            # -のときはスタックから2つ取り出して減算し，再度格納する
            a = stack.pop() #後の演算のために順序を整えている
            stack.append(a)
            stack.append(a)
        elif i == 'POP':
            # -のときはスタックから2つ取り出して減算し，再度格納する
            a = stack.pop() #後の演算のために順序を整えている
            #stack.append(a)
        elif i == '+' and len(stack)<2:
            return -1
        elif i == '-' and len(stack)<2:
            return -1
        else:
            stack.append(int(i))    #受け取っているものは文字列であるが，後に計算されるので，intに変換

    temp = stack.pop()
    if temp<0:
        temp=-1
    elif temp>2**20-1:
        temp =-1

    return temp



print (solution(S))