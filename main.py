import telebot
import os
import zipfile

token_file = open('API_token.txt')
token = token_file.readline()

bot = telebot.TeleBot(token)
ch_id = "@testing_bot_channel_new"

archive_path = '312-Furniture.zip'

def find_photo():
    return 0


def get_unique_filename(filename, directory):
    """Функция возвращает уникальное имя файла в заданной директории."""
    base, ext = os.path.splitext(filename)
    # print(base)
    counter = 1
    while True:
        unique_filename = f"{base}_{counter}{ext}" if counter > 1 else filename
        if not os.path.exists(os.path.join(directory, unique_filename)):
            return unique_filename.encode('utf-8')
        counter += 1

def extract_images_from_zip(zip_file_path, output_folder , i = 0):
    
    # Создаем директорию вывода, если она еще не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with zipfile.ZipFile(zip_file_path, 'r') as zf:
        for i in range(1):
            # print(os.path.splitext(zip_file_path))
            split_text = zip_file_path.split("\\")
            print(split_text[-1])
            for file in zf.namelist():
                # print(zf.namelist())
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # i+=1
                    # print(i)
                    split_text = zip_file_path.split("\\")
                    # Извлекаем файл изображения в указанную директорию
                    unique_filename = get_unique_filename(os.path.basename(file), output_folder)
                    # print(unique_filename)
                    # bot.send_message(ch_id, split_text[-1])
                    bot.send_photo(ch_id, photo=open(os.path.basename(file), 'rb'))
            
                    
                
                elif file.endswith('.zip'):
                    # Если это другой архив, извлекаем его и обрабатываем рекурсивно
                    zf.extract(file, path=output_folder)
                    nested_archive = os.path.join(output_folder, file)
                    extract_images_from_zip(nested_archive, output_folder, i)
                    os.remove(nested_archive)
        



question = "Нравится?"
options = ["Да", "Нет", "Ой, админ иди н@#уй"]

# bot.send_poll(
#     chat_id=ch_id,
#     question=question,
#     options=options,
#     is_anonymous=True  # Опрос анонимный или нет
# )
archive_path = '312-Furniture.zip'
output_dir = 'out'
extract_images_from_zip(archive_path, output_dir)