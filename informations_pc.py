import platform

def system_informations():
    print("="*10, "System informations", "="*10)
    info = platform.uname()

    print(f'''
    System: {info.system}
    Computer name: {info.node}
    Release: {info.release}
    Version: {info.version}
    Machine: {info.machine}
    Processor: {info.processor}
    
    ''')

    input("Press ENTER to return")
    main()

def main():
    option = int(input('''
    [1] System informations
    [2] Memory informations
    [3] CPU informations
    [4] GPU informations

    Choose an option: '''))

    if option == 1:
        system_informations()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        pass


if __name__ == '__main__':
    main()