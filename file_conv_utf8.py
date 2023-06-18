import os
def convert_nf1_to_txt(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".nf1"):
            nf1_file = os.path.join(folder_path, file_name)
            txt_file = os.path.join(folder_path, os.path.splitext(file_name)[0] + ".txt")
            with open(nf1_file, "r") as nf1:
            # with open(nf1_file, "r", encoding="s-jis") as nf1:
                nf1_contents = nf1.read()
            with open(txt_file, "w", encoding="utf-8") as txt:
                txt.write(nf1_contents)
            os.remove(nf1_file)
    print("変換が完了しました")
if __name__ == "__main__":
    print('変換したいnf1ファイル（例 20230618.nf1）が入っているフォルダ名を入力してください')
    folder_path = input('>> ')
    dummy = input('Enterを押すと変換を開始します（バックアップ取りません）')
    # folder_path = "C:\\Users\\user\\python\\FILE\\diary_data"  # 対象のフォルダパスを指定
    convert_nf1_to_txt(folder_path)