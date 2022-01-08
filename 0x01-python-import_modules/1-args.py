#!/usr/bin/python3

if __name__=="__main__":

    import sys

    print(len(sys.argv) - 1, end=' ')

    if (len(sys.argv) - 1) == 0:
        print('arguments.')

    elif (len(sys.argv) - 1) == 1:
        print('argument:')
        print(1, end='')
        print(':', sys.argv[1])

    else:
        print('arguments:')
        

        for i in range(len(sys.argv) - 1):
            print(i + 1, end='')
            print(':', sys.argv[i + 1])
            i += 1
