import os
from app.io.input import read_from_console
from app.io.output import print_output_to_console, write_to_file_builtin

def main():
    data_dir = "results"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Створено файл з результом: {data_dir}")
    path_output = os.path.join(data_dir, "output.txt")

    print("Введіть дані")
    input_from_console = read_from_console()

    print("Вивід у консоль")
    print_output_to_console(f"Користувачем було введено такі дані:\n {input_from_console}")

    print("Запис у файл")
    output_to_file = f"{path_output}"

    write_to_file_builtin(input_from_console, output_to_file)

if __name__ == "__main__":
    main()