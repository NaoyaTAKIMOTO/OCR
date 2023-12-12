import easyocr
import os
import PIL.Image


reader = easyocr.Reader(["ja"])
directory_path = os.path.join(".", "data")
files = [f for f in os.listdir(directory_path) if f.endswith(".jpg") or f.endswith(".jpeg")]

# 処理したいディレクトリが存在しなければ作成する
output_directory = os.path.join(directory_path, "output")
os.makedirs(output_directory, exist_ok=True)
output_directory = os.path.join(directory_path, "tmp")
os.makedirs(output_directory, exist_ok=True)

# ファイルごとに処理を行う
for file in files:
    file_path = os.path.join(directory_path, file)
    # 画像を読み込む
    image = PIL.Image.open(file_path)

    # 画像サイズを変更する
    image = image.resize((1024, 1024))

    # 画像を保存する
    tmp_path = os.path.join(directory_path, "tmp", file)
    image.save(tmp_path)

    result = reader.readtext(tmp_path)
    text_parts = [item[1] for item in result]
    # ファイルに書き込む
    output_file_path = os.path.join(directory_path, "output", os.path.basename(file).split(".")[0]+".txt")
    with open(output_file_path, 'w') as file:
        for string_item in text_parts:
            file.write(f"{string_item}\n")
