import os
import shutil
import subprocess
import string
import secrets

def initial():
  shutil.rmtree('conversionToZip/output/')
  os.mkdir('conversionToZip/output/')

def getAfterFileName(beforeName):
  file, _ = os.path.splitext(beforeName)
  return '../output/' + file + '.zip', file

def create_pass(num):
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(pass_chars) for i in range(num))
    return password

## 初期処理
initial()

## 変換対象一覧を取得
targets = os.listdir('conversionToZip/input')

with open('conversionToZip/output/password.txt', 'a') as f:
  
  for target in targets:

    ## 出力先のファイルパスを取得
    outputPath, file = getAfterFileName(target)

    ## 設定するパスワードを作成
    pass_word = create_pass(12)

    ## テキストファイルにパスワードを出力
    f.write(file + ':' + pass_word + '\n')

    ## zip化
    args = (
        '/usr/local/Cellar/sevenzip/24.08/bin/7zz', 
        'a', 
        outputPath, # 圧縮後のファイル
        target, # 圧縮対象フォルダ
        '-mx=1', # 圧縮レベル0-9 ９が最大
        '-p' + pass_word, # パスワード
        )
    print(args)
    result = subprocess.run(args, cwd=r'conversionToZip/input/')