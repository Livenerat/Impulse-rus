# Import modules
import os
import sys
import json
from colorama import Fore
from getpass import getpass, getuser
from smtplib import SMTPAuthenticationError, SMTP
# https://github.com/LimerBoy/Twilight-Algoritm
from tools.addons.twilight.twilight import Decrypt, Encrypt

# File with login data
sender_email_database = "tools/EMAIL/sender.json"
twilight_encryption_key = getuser() + ":TWILIGHT"
smtp_server = "smtp.gmail.com"
smtp_port = 587


""" Write sender email """


def WriteSenderEmail():
    username = input(f"{Fore.BLUE}[?] {Fore.MAGENTA}Введи gmail адрес с которого будем флудить: {Fore.BLUE}")
    password = getpass(f"{Fore.BLUE}[?] {Fore.MAGENTA}Введи пароль для gmail адреса: {Fore.BLUE}")
    server = SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    # Try login to gmail account
    try:
        server.login(username, password)
    except SMTPAuthenticationError:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Пароль некорректен! Или попробуй включить это:"
            f"\n    https://myaccount.google.com/lesssecureapps{Fore.RESET}"
        )
        sys.exit(1)
    else:
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}Успешно залогинен как{Fore.RESET}"
        )

    # Saved data to db?
    confirm = input(f"{Fore.BLUE}[?] {Fore.MAGENTA}Сохранить эту инфу на будущее? (yes/no) : {Fore.BLUE}")
    confirm = confirm.upper() in ("Y", "YES", "1", "TRUE")
    if confirm:
        # Write database
        with open(sender_email_database, "w") as db:
            json.dump(
                {
                    "username": Encrypt(username, twilight_encryption_key),
                    "password": Encrypt(password, twilight_encryption_key)
                }, db
            )
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}Сохранено в: {repr(sender_email_database)}{Fore.RESET}"
        )

    return [server, username]

""" Read sender email """


def ReadSenderEmail():
    # Create if not exists
    if not os.path.exists(sender_email_database):
        return WriteSenderEmail()
    # Read database
    with open(sender_email_database, "r") as db:
        auth = json.load(db)
        auth["username"] = Decrypt(auth["username"], twilight_encryption_key)
        auth["password"] = Decrypt(auth["password"], twilight_encryption_key)
    # Login
    server = SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    try:
        server.login(
            auth["username"],
            auth["password"]
        )
    except SMTPAuthenticationError:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Пароль некорректен!{Fore.RESET}"
        )
        os.remove(sender_email_database)
        sys.exit(1)
    else:
        return [server, auth["username"]]
