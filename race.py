import argparse
import time

def increment_counter(num_iterations, delay):
    # nazwa pliku przechowującego licznik
    file_name = 'licznik.txt'

    # otwieramy plik w trybie do odczytu
    with open(file_name, 'r') as file:
        # odczytujemy wartość licznika z pierwszej linii pliku
        counter = int(file.readline())

    # inkrementujemy wartość licznika i zapisujemy nową wartość do pliku
    for i in range(num_iterations):
        time.sleep(delay)  # opóźnienie między odczytem i zapisem nowej wartości
        counter += 1
        with open(file_name, 'w+') as file:
            file.write(str(counter) + '\n')
            file.seek(0)  # ustawiamy kursor na początek pliku
            print('Wartość licznika po', i+1, 'inkrementacji:', file.readline().strip())

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_iterations', type=int, default=10, help='ilość powtórzeń inkrementacji')
parser.add_argument('-d', '--delay', type=float, default=1, help='opóźnienie między odczytem i zapisem nowej wartości (w sekundach)')
args = parser.parse_args()

increment_counter(args.num_iterations, args.delay)
