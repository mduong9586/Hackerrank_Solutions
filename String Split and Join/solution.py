def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line2 = "-".join(line)
    return line2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
