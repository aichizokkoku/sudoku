# 数独を画像から自動測定、そして自動的に答えを導き出す


## ファイルについて
### 数独を解くアルゴリズム
NP.py  
awsNP.py(AWSようにカスタマイズされたもの)

### 数独の文字データ
data.txt  
dataline.txt

### 数独の画像データ
sudoku.png  
sudokuD.png

### 機械学習などの様々なテスト
test.ipynb(画像から枠を検出するテスト)  
contours.ipynb(画像認識して、一つ一つの枠の画像データを出力するテスト)
awsTest.py(aws用のpythonの基本的文法のテスト)
test.txt(awsTest.pyなどで用いるテキストファイル)

## 動作の流れ
1. 画像を用意
2. 画像をインプット
3. 画像から枠を抽出
4. 画像から9*9のマスの画像を摘出
5. それぞれの画像の文字認識
6. すべての文字をリストに入れて数独アルゴリズムに投入  
 -- そのときに空欄の数字は0か.で認識させる
7. できたら元画像に数字を挿入して出力
