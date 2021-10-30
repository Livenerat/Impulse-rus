sys=$(uname -o)
sysid=$(lsb_release -i)
clear
echo "Определение системы..."
if [[ $sys = 'Android' ]]; then
    clear
    echo "Определена система -" $sys
    sleep 1
    clear
    echo "Получение прав на запуск..."
    sleep 2
    chmod +x ~/Impulse-rus/impulse && cp impulse /data/data/com.termux/files/usr/bin
    clear
    echo "Успешно"
    sleep 1
    clear
    echo Установка зависимостей...
    sleep 2
    clear
    python3 -m pip install -r requirements.txt
    clear
    echo Успешно
    sleep 1
    clear
    echo Установка выполнена успешно, чтобы запустить Импульс, наберите команду impulse
    echo
    echo Удаление установщика...
    rm -f setup.sh
elif [[ $sys = 'GNU/Linux' ]]; then
    clear
    echo "Определена система -" $sys
    sleep 1
    clear
    echo Получение прав на запуск...
    sleep 2
    chmod +x impulse && sudo cp impulse /usr/bin
    clear
    echo Успешно
    sleep 1
    clear
    echo Установка зависимостей...
    sleep 2
    clear
    python3 -m pip install -r requirements.txt
    clear
    echo Успешно
    sleep 1
    clear
    echo Установка выполнена успешно, чтобы запустить Импульс, наберите команду impulse из любого расположения
    echo
    echo Удаление установщика...
    rm -f setup.sh
else
    echo "Ошибка. Система не соответствует требованиям!"
    sleep 1
    clear
    exit 3
fi
