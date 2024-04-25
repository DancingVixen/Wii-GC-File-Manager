# Этот документ был создан Sasha Foxr129 24-04-2024 с любовью из России

'''
  _____              __                  .__        __                     .___      
_/ ____\_ __   ____ |  | __         ____ |__| _____/  |_  ____   ____    __| _/____  
\   __\  |  \_/ ___\|  |/ /        /    \|  |/    \   __\/ __ \ /    \  / __ |/  _ \ 
 |  | |  |  /\  \___|    <        |   |  \  |   |  \  | \  ___/|   |  \/ /_/ (  <_> )
 |__| |____/  \___  >__|_ \       |___|  /__|___|  /__|  \___  >___|  /\____ |\____/ 
                  \/     \/            \/        \/          \/     \/      \/       
'''




import os
from tqdm import tqdm

def get_user_language():
    # Ask the user for their preferred language
    language = input("Please enter your preferred language (EN/RU) - Введите предпочитаемый язык (EN/RU): ")
    return language.lower()

def get_user_input(language):
    # Request user input for the source and destination directories
    if language == "russian":
        source_dir = input("Введите исходный каталог: ")
        dest_dir = input("Введите целевой каталог: ")
    else:
        source_dir = input("Enter the source directory: ")
        dest_dir = input("Enter the destination directory: ")
    return source_dir, dest_dir

def get_files(source_dir):
    # Get all files in the source directory
    files = os.listdir(source_dir)
    return files

def print_files(files, source_dir, language):
    # Print all files with numbers and their sizes
    for i, file in enumerate(files, start=1):
        size = os.path.getsize(os.path.join(source_dir, file))
        if language == "russian":
            print(f"{i}. {file} - {size / (1024 * 1024 * 1024):,.3f} ГБ")
        else:
            print(f"{i}. {file} - {size / (1024 * 1024 * 1024):,.3f} GB")

def get_selected_files(files, source_dir, language):
    # Ask the user for the ranges and individual files to copy
    if language == "russian":
        ranges_and_files = input("Введите диапазоны и отдельные файлы для копирования (например, 1-3,4): ").split(',')
    else:
        ranges_and_files = input("Enter the ranges and individual files to copy (e.g., 1-3,4): ").split(',')
    selected_files = []
    total_size = 0
    for item in ranges_and_files:
        if '-' in item:
            range_start, range_end = map(int, item.split('-'))
            selected_files.extend(files[range_start-1:range_end])
            total_size += sum(os.path.getsize(os.path.join(source_dir, file)) for file in files[range_start-1:range_end])
        else:
            selected_files.append(files[int(item)-1])
            total_size += os.path.getsize(os.path.join(source_dir, files[int(item)-1]))
    return selected_files, total_size

def confirm_copy(selected_files, total_size, language):
    # Print selected files and total size
    if language == "russian":
        print("Выбранные файлы:")
    else:
        print("Selected files:")
    for file in selected_files:
        print(file)
    if language == "russian":
        print(f"Общий размер: {total_size / (1024 * 1024 * 1024):,.3f} ГБ")
    else:
        print(f"Total size: {total_size / (1024 * 1024 * 1024):,.3f} GB")

    # Ask for confirmation
    if language == "russian":
        confirmation = input("Вы уверены, что хотите скопировать эти файлы? (да/нет): ")
        if confirmation.lower() != 'да':
            print("Операция отменена.")
            return False
    else:
        confirmation = input("Are you sure you want to copy these files? (yes/no): ")
        if confirmation.lower() != 'yes':
            print("Operation cancelled.")
            return False
    return True

def copy_files(selected_files, source_dir, dest_dir, language):
    for file in selected_files:
        # Get the file name without the extension and the extension
        file_name, file_ext = os.path.splitext(file)
        
        # Create the new folder path
        new_folder_path = os.path.join(dest_dir, file_name)
        
        # Create the new folder
        os.makedirs(new_folder_path, exist_ok=True)
        
        # Copy the file to the new folder and rename it to "game"
        with open(os.path.join(source_dir, file), 'rb') as src_file:
            with open(os.path.join(new_folder_path, "game" + file_ext), 'wb') as dest_file:
                total_size = os.path.getsize(src_file.name)
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=file) as pbar:
                    for chunk in iter(lambda: src_file.read(1024*1024), b''):
                        dest_file.write(chunk)
                        pbar.update(len(chunk))
    if language == "russian":
        print("Выбранные файлы успешно скопированы и переименованы!")
    else:
        print("Selected files copied and renamed successfully!")

def main():
    language = get_user_language()
    if language == "ru":
        language = "russian"
    else:
        language = "english"
    source_dir, dest_dir = get_user_input(language)
    files = get_files(source_dir)
    print_files(files, source_dir, language)
    selected_files, total_size = get_selected_files(files, source_dir, language)
    if confirm_copy(selected_files, total_size, language):
        copy_files(selected_files, source_dir, dest_dir, language)


if __name__ == "__main__":
    main()
