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
    {Fore.MAGENTA}Версия: {platform.python_version()}
    {Fore.MAGENTA}Билд: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.MAGENTA}Компилятор: {platform.python_compiler()}
    {Fore.MAGENTA}Расположение скрипта: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.MAGENTA}Текущее положение: {os.getcwd()}
    {Fore.RED}:=== Системное инфо:
    {Fore.MAGENTA}Сиситема: {platform.system()}
    {Fore.MAGENTA}Релиз: {platform.release()}
    {Fore.MAGENTA}Версия: {platform.version()}
    {Fore.MAGENTA}Архитектура: {'{} {}'.format(*platform.architecture())}
    {Fore.MAGENTA}Процессор: {platform.processor()}
    {Fore.MAGENTA}Машина: {platform.machine()}
    {Fore.MAGENTA}Хост: {platform.node()}
    {Fore.MAGENTA}Время: {ctime()}
    {Fore.RED}:=== Репорт:
    {Fore.MAGENTA}Сообщи об ошибке в телеграм @tea_allkash
    {Fore.RESET}
    """)
    sys.exit(5)
