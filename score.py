project=int(input("Enter project score:"))
internal=int(input("Enter internal score:"))
external=int(input("Enter external score:"))
if(project>=50 and internal>=50 and external>=50):
    total=(70/100)*project+(10/100)*internal+(20/100)*external
    if(total>90):
        print("A grade")
    elif(80<total<90):
        print("B grade")
    else:
        print("C grade")
else:
    if(project<50):
        print("Student failed in project",project)
    if(internal<50):
        print("Student failed in internal",internal)
    if(external<50):
        print("Student failed in external",external)