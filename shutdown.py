import os
x = input("Please Select the Action: \ns\tShutdown\nr\tRestart\nh\tHibernate\n")
if (x == ('s')):
    y = input("Are you sure? (y/n)")
    if (y==('y')):
        os.system("shutdown /s")
    else:
        exit()
if (x == ('r')):
    y = input("Are you sure? (y/n)")
    if (y==('y')):
        os.system("shutdown /r")
    else:
        exit()
if (x == ('h')):
    y = input("Are you sure? (y/n)")
    if (y==('y')):
        os.system("shutdown /h")
    else:
        exit()