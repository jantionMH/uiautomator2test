
def isValid(s):
        #
        # if s1 == '(':
        #     return True
        # elif s1 == '(' and s2 == ')':
        #     return True
        # elif s1 == ')':
        #     return False
        # if len(s1)==1 and s1 in ['(','{','[']:
        #     print(True)
        # elif len(s1)==1 and s1 in [')','}',']']:
        #     print(False)
        # elif
        # l=['(',')','{','}','[',']']
        l=['(','[','{','}',']',')']
        if l[0] in ['(','[','{'] and (len(l)%2==0 or len(l)%2==2 ):

            if len(l)==6 or len(l)==2:
                for i in range(len(l)):
                    if (l[i]=='(' and l[i+1]==')')or (l[i]=='[' and l[i+1]==']') or (l[i] == '{' and l[i + 1] == '}') or (l[i]=='('and l[-1]==')'):
                        print(True)



        elif l[0] in [']','}',')']:
            print(False)



if __name__ == '__main__':
    isValid('()')
