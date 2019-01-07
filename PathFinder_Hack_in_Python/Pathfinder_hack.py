# Paste the code for the Interpreter :
# The input is splitted into each alphabets and then converted into the each degrees of the Clock.
re_alpha=[]
re_beta=[]
def generate():
    alpha = input()
    for i in range(0, len(alpha)):
        re_alpha.append(int(ord(alpha[i]))*1.40625)
        #print(alpha[i]+"\t"+str(int(ord(alpha[i]))*1.40625))
    print(re_alpha)
def resolve():
    st = ''
    re_beta = input("Enter all the Radiant values with spaces between them\n")
    re_beta=re_beta.split()
    for i in range(0,len(re_beta)):
        st=st+str(chr(int(float(re_beta[i])/1.40625)))
    print(st)

while True:
    choice = int(input("\t\t\t1.Generate PF Code\n\t\t\t2.Resolve PF Code\n\t\t\t3.Exit\n\t Enter your choice\n"))
    if choice == 1:
        generate()
    elif choice == 2:
        resolve()
    else:
        break
# At first split the number by spaces(ascii:45.0) and then divide the floating numbers with 1.40625
# Actually all the 256 alpha numeric characters can be represented in 360Degrees(weighing 1.40625Degree for each ascii value)