def main():
    print("Улирлаа оруулна уу 1=Хавар, 2=Зун, 3=Намар, 4=Өвөл")
    n=int(input())
    def printSpring():
        print("Хавар болж цэцэгс цэцэглэлээ.")
    def printSummer():
        print("Зун болж халуун боллоо.")
    def printFall():
        print("Намар болж навч уналаа.")
    def printWinter():
        print("Өвөл болж цас орлоо.")
    if(n==1):
        printSpring()
    if(n==2):
        printSummer()
    if(n==3):
        printFall()
    if(n==4):
        printWinter()
main()