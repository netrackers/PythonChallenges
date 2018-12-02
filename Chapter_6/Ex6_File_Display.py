def main():
    numbers = open('numbers.txt', 'r')
    line = numbers.readline()
    
    while line != "":
        print(line)
        line = numbers.readline()

    numbers.close()

main()
