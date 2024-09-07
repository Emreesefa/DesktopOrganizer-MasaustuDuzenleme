import os
import shutil

def organize_desktop():
    # Masaüstü yolunu al
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Dosya türlerini ve karşılık gelen klasör isimlerini tanımla
    file_types = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.odt'],
        'Music': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Programs': ['.exe', '.msi', '.bat', '.sh'],
        'Others': []  # Tanımlanmayan dosyalar buraya gidecek
    }

    # Masaüstündeki dosyaları al
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # Sadece dosyaları işle, klasörleri atla
        if os.path.isfile(item_path):
            # Dosya uzantısını al
            _, file_extension = os.path.splitext(item)
            
            # Dosya türüne göre klasör belirle
            folder_name = 'Others'  # Varsayılan olarak 'Others'
            for key, extensions in file_types.items():
                if file_extension in extensions:
                    folder_name = key
                    break
            
            # Hedef klasörün yolunu belirle
            target_folder = os.path.join(desktop_path, folder_name)
            
            # Klasör yoksa oluştur
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            # Dosyayı hedef klasöre taşı
            shutil.move(item_path, target_folder)
            print(f"{item} taşındı {target_folder} klasörüne.")

if __name__ == "__main__":
    organize_desktop()
