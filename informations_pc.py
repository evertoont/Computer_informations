import os
import time
import platform
import psutil

# SYSTEM INFORMATIONS #

def system_informations():
    clear_screen()
    print("="*10, "System Informations", "="*10)
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

# MEMORY INFORMATIONS #

def size_convert(bytes, suffix='B'):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

def memory_informations():
    clear_screen()
    print("="*10, "Memory Informations", "="*10)

    memory = psutil.virtual_memory()

    print(f'''
    Total: {size_convert(memory.total)}
    Available: {size_convert(memory.available)}
    Used: {size_convert(memory.used)}
    Percentage: {memory.percent} %
    
    ''')

    input("Press ENTER to return")
    main()

#CLEAR SCREEN #

def clear_screen():
    os.system("cls || clear")

# MAIN FUNCTION #

def main():
    clear_screen()
    option = int(input('''
    [1] System informations
    [2] Memory informations
    [3] CPU informations
    [4] GPU informations
    [5] Exit

    Choose an option: '''))

    if option == 1:
        system_informations()
    elif option == 2:
        memory_informations()
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        exit()
    else:
        print("\n ####### Choose a valid option #######")
        time.sleep(2)
        main()


if __name__ == '__main__':
    main()