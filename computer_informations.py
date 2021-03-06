import os
import time
import platform
import psutil
import GPUtil
from tabulate import tabulate
from banner import banner

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

# CPU INFORMATIONS #


def cpu_informations():
    clear_screen()
    print("="*10, "CPU Informations", "="*10)

    cpu = psutil.cpu_freq()

    print(f'''
    Physical cores: {psutil.cpu_count(logical=False)}
    Total cores: {psutil.cpu_count(logical=True)}
    Max frequency: {cpu.max:.2f} Mhz
    Min frequency: {cpu.min:.2f} Mhz
    Current frequency: {cpu.current:.2f} Mhz

    CPU usage per Core:
    ''')
    for core, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"\tCore {core}: {percentage}%")
    print(f"\n \tTotal CPU usage: {psutil.cpu_percent()}% \n")

    input("Press ENTER to return")
    main()


# CPU INFORMATIONS #

def gpu_informations():
    clear_screen()
    print("="*40, "GPU Informations", "="*40)

    gpus = GPUtil.getGPUs()
    gpus_list = []

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100} %"
        gpu_free_memory = f"{gpu.memoryFree} MB"
        gpu_used_memory = f"{gpu.memoryUsed} MB"
        gpu_total_memory = f"{gpu.memoryTotal} MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid

        gpus_list.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(gpus_list, headers=("Id", "Name", "Load", "Free memory",
                                       "Used memory", "Total memory", "Temperature", "Uuid")))

    input("\nPress ENTER to return")
    main()

#CLEAR SCREEN #


def clear_screen():
    os.system("cls || clear")

# MAIN FUNCTION #


def main():
    clear_screen()
    banner()
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
        cpu_informations()
    elif option == 4:
        gpu_informations()
    elif option == 5:
        exit()
    else:
        print("\n ####### Choose a valid option #######")
        time.sleep(2)
        main()


if __name__ == '__main__':
    main()
