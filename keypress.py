import getch

if __name__ == '__main__':
    i = 0
    while True:
        print(i)
        c = getch.getch()
        print(repr('you pressed {}'.format(c)))
        i += 1
