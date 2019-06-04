import re

if __name__ == "__main__":

    with open("logs.txt") as file:
        for line in file:
            if re.search("[0-2][0-9]/Mar/2004.+GET /twiki.+200", str(line)):
                print(line)
