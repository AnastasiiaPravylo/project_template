def print_output_to_console(text):
    """
    Виводить текст у консоль
    Args:
        data (str): текст що має виводитись
    """
    print("\nВивід:")
    if text is not None:
      print(text)
    else:
      print("Немає даних\n")

def write_to_file_builtin(data, file_path):
    """
    Записує текст у файл за допомогою вбудованих засобів Python
    Args:
        file_path (str): шлях до файлу
        data (str): текст що має записуватись
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            if data is not None:
                file.write(data)
            else:
                file.write("")
        print(f"Дані записано у файл: {file_path}")
    except Exception as e:
        print(f"Сталася помилка під час запису у файл '{file_path}': {e}")
