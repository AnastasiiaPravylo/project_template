import pandas as pd
def read_from_console():
    """
    Зчитує текст з консолі
    Returns:
        str: Введений текст з консолі
    """
    try:
        input_text = input("Введіть текст: ")
        return input_text
    except Exception as e:
        print(f"Сталась помилка: {e}")
        return ""

def read_from_file_builtin(file_path):
    """
    Зчитує вміст файлу за допомогою вбудованих засобів
    Args:
        file_path (str): шлях до файлу
    Returns:
        str: вміст що знаходться у файлі
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' неіснує")
        return None
    except Exception as e:
        print(f"Сталася помилка під час читання файлу '{file_path}': {e}")
        return None

def read_from_file_pandas(file_path):
    """
    Зчитує файл за допомогою бібліотеки pandas
    Args:
        file_path (str): шлях до файлу
    Returns:
        pd.DataFrame: вміст файлу у вигляді таблиці
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' неіснує")
        return None
    except pd.errors.EmptyDataError:
        print(f"Помилка: файл '{file_path}' не має значень")
        return None
    except Exception as e:
        print(f"Сталася помилка під час читання файлу '{file_path}' : {e}")
        return None
