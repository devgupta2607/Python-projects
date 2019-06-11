import csv

file ='E:/Programs/Python programming/cosmic_skills/as.txt'

def credentials():
    global uname
    global passwrd
    uname = input('Enter user name: ')
    passwrd = input('Enter password: ')
    check()


def check():
    with open(file) as f:
        data = csv.reader(f)

        for line in data:
            try:
                unameC = line[0]
                pwordC = line[1]
                if uname == unameC and passwrd == pwordC:
                    print("Login Successful")
                    break

                else:
                    print('Try Again')
                    credentials()
            except IndexError:
                pass

if __name__ == "__main__":
    credentials()





