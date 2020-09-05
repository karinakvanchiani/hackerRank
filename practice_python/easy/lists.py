if __name__ == '__main__':
    N = int(input())
    commands = {}
    my_list = []
    print_list = []
    for _ in range(N):
        key, *line = input().split()
        value = list(map(int, line))
        commands[key] = value
        if key == 'append':
            my_list.append(value[0])
        elif key == 'print':
            print(my_list)
        elif key == 'insert':
            my_list.insert(value[0], value[1])
        elif key == 'pop':
            my_list.pop()
        elif key == 'remove':
            my_list.remove(value[0])
        elif key == 'sort':
            my_list.sort()
        elif key == 'reverse':
            my_list.reverse()
