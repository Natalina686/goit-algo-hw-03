import os
import shutil
import sys

def copy_files(src_dir, dest_dir):
    # Перебираємо всі елементи у вихідній директорії
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        
        if os.path.isdir(src_path):
            # Якщо це директорія, викликаємо функцію рекурсивно
            copy_files(src_path, dest_dir)
        elif os.path.isfile(src_path):
            # Якщо це файл, копіюємо його
            file_extension = item.split('.')[-1] if '.' in item else 'no_extension'
            extension_dir = os.path.join(dest_dir, file_extension)
            
            # Створюємо піддиректорію для розширення, якщо її не існує
            os.makedirs(extension_dir, exist_ok=True)
            
            try:
                shutil.copy2(src_path, extension_dir)
                print(f"Скопійовано: {src_path} -> {extension_dir}")
            except Exception as e:
                print(f"Помилка при копіюванні {src_path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [<destination_directory>]")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.getcwd(), 'dist')

    # Перевіряємо, чи існує вихідна директорія
    if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
        print("Вихідна директорія не існує або не є директорією.")
        sys.exit(1)

    # Копіюємо файли
    copy_files(source_directory, destination_directory)
    print("Копіювання завершено.")

if __name__ == "__main__":
    main()