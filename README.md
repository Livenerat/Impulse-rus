# :bomb: Импульс
## Современный DoS тулкит

## :satellite: Методы:
| Метод               |   Цель   | Описание |
| ---------------------| -----------|-------------|
| SMS                  | PHONE     | Отправляет большое кол-во запросов на смс и звонок по цели. |
| EMAIL                | EMAIL     | Отправляет большое кол-во сообщений на электронную почту цели. |
| NTP                  | IP:PORT    | Использование публичных NTP серверов для выполнения DDoS атаки на цель. |
| SYN                  | IP:PORT    | SYN-флуд (полуоткрытая атака) - DDoS атака потребляющая все ресурсы целевого сервера, делая его недоступным для конечного пользователя. |
| UDP                  | IP:PORT    | UDP-флуд — тип DDoS атаки, использующей большое количество пакетов протокола UDP с целью ограничения способности целевого сервера обрабатывать и реагировать на запросы. Брандмауэр, защищающий целевой сервер, также может быть исчерпан в результате UDP флуда. |
| POD (Ping of Death)  | IP         | Ping of Death (Пинг Смерти) - тип DDoS атаки, использующей негабаритные пакеты ping для вызова отказа в обслуживании на целевом сервере, компьютере или службе. |
| ICMP                 | IP:PORT    | ICMP флуд - тип DDoS атаки, перегружающей целевой сервер большим кол-вом ICMP запросов. |
| HTTP                 | URL        | HTTP флуд - тип DDoS атаки, использующей HTTP и POST запросы с целью атаки на целевой сервер. |
| Slowloris            | IP:PORT    | Slowloris - тип DDoS атаки, перегружающей целевой сервер открывая и поддерживая множество одновременных HTTP-соединений между устройством и целью. |
| Memcached            | IP:PORT    | Атака на уязвимый UDP сервер Memcached, который потом перегружает целевой сервер трафиком. |

# Установка:
* Windows:
  * Скачайте Python [отсюда](https://www.python.org/downloads/)
  * Запустите установщик, поставьте галочку `add python to PATH`
  * Загрузите Импульс
  * Откройте командную строку или Powershell в директории Импульса
  * Выполните эту команду: `pip install -r requirements.txt`
  * Затем эту: `python impulse.py --help`

* Linux:
  * Обновите систему и установите пакеты git, python.
  * Выполните команды:
  * `git clone https://github.com/TofuYa-dev/Impulse-rus`
  * `cd Impulse-rus/`
  * `chmod +x setup.sh && ./setup.sh`

* Termux:
  * Рекомендуется установить приложение Termux:API. Обратите внимание, его нужно установить из того же источника, что и сам Termux!
  * Выполните команды:
  * `pkg update`
  * `pkg install python git -y`
  * `git clone https://github.com/TofuYa-dev/Impulse-rus`
  * `cd Impulse-rus/`
  * `chmod +x setup.sh && ./setup.sh`

* Рекомендации для Linux и Termux:
  * Устанавливайте Импульс в домашнюю директорию.
  * Не перемещайте репозиторий Импульса из первоначальной директории, иначе скрипты не будут работать!
  * Не перемещайте, не удаляйте и не переименовывайте файлы внутри директории Импульса, иначе скрипты не будут работать!

# На данный момент упрощён только СМС флуд, для доступа к остальным функциям запускайте Импульс через `python3 impulse.py`

# :moneybag: Ускорить разработку:
**BTC:** `bc1qxqtg05v8evnm5slwty5z6wwhf9c6zrqecw39mq`

