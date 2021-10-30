# Import modules
import os
import sys
import platform
from time import ctime
from colorama import Fore

""" This function will stop the program when a critical error occurs """


def CriticalError(message, error):
    print(f"""
    {Fore.RED}:=== Критическая ошибка:
    {Fore.MAGENTA}Сообщение: {message}.
    {Fore.MAGENTA}ОШИБКА: {error}
    {Fore.RED}:=== Python инфо:
    {Fore.MAGENTA}PYTHON ВЕРСИЯ: {platform.python_version()}
    {Fore.MAGENTA}PYTHON БИЛД: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.MAGENTA}PYTHON КОМПИЛЯТОР: {platform.python_compiler()}
    {Fore.MAGENTA}РАСПОЛОЖЕНИЕ СКРИПТА: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.MAGENTA}ТЕКУЩЕЕ ПОЛОЖЕНИЕ: {os.getcwd()}
    {Fore.RED}:=== Системное инфо:
    {Fore.MAGENTA}СИСТЕМА: {platform.system()}
    {Fore.MAGENTA}РЕЛИЗ: {platform.release()}
    {Fore.MAGENTA}ВЕРСИЯ: {platform.version()}
    {Fore.MAGENTA}АРХИТЕКТУРА: {'{} {}'.format(*platform.architecture())}
    {Fore.MAGENTA}ПРОЦЕССОР: {platform.processor()}
    {Fore.MAGENTA}МАШИНА: {platform.machine()}
    {Fore.MAGENTA}НОДА: {platform.node()}
    {Fore.MAGENTA}ВРЕМЯ: {ctime()}
    {Fore.RED}:=== РЕПОРТ:
    {Fore.MAGENTA}Доложи об ошибке сюда: https://github.com/LimerBoy/Impulse/issues/new
    {Fore.RESET}
    """)
    sys.exit(5)
