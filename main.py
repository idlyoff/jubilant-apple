import os
import multiprocessing
from pathlib import Path
from moviepy import VideoFileClip

# Папка с AVI-файлами
input_folder = Path(r"C:\Users\idlyo\OneDrive\Рабочий стол\avi")

# Папка для конвертированных файлов
converted_folder = input_folder / "converted"
converted_folder.mkdir(exist_ok=True)

def convert_file(filepath: Path):
    output_filepath = converted_folder / (filepath.stem + ".mp4")
    try:
        with VideoFileClip(str(filepath)) as video:
            video.write_videofile(
                str(output_filepath),
                codec="libx264",
                audio_codec="aac"
            )
        print(f"✅ Конвертирован: {filepath.name} -> {output_filepath.name}")
        # os.remove(filepath)  # если хочешь удалять оригиналы
    except Exception as e:
        print(f"❌ Ошибка при конвертации {filepath.name}: {e}")

if __name__ == "__main__":
    avi_files = list(input_folder.glob("*.avi"))
    if not avi_files:
        print("В папке нет AVI-файлов.")
    else:
        with multiprocessing.Pool() as pool:
            pool.map(convert_file, avi_files)

    print("Готово!")

