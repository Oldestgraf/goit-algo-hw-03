from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst)  # Рекурсивний виклик для піддиректорії
            else:
                extension = item.suffix[1:].lower()  # Отримання розширення файлу
                if not extension:
                    extension = 'no_extension'
                extension_dir = dst / extension
                extension_dir.mkdir(parents=True, exist_ok=True)  # Створення піддиректорії

                # Формування нового імені файлу з назвою директорії
                parent_dir_name = item.parent.name
                new_file_name = f"{item.stem}_{parent_dir_name}{item.suffix}"
                new_file_path = extension_dir / new_file_name

                shutil.copy2(item, new_file_path)  # Копіювання файлу
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    args = parse_args()
    source_dir = args.source
    dest_dir = args.dest

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Вихідна директорія {source_dir} не існує або не є директорією.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()

# Usage:
# $python3 main.py --source test --dest copy_test
