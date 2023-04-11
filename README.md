# Github入門研修資料

## 概要
- Github入門ハンズオン用環境構築方法の説明
- fizzbuzzプログラム作成演習
  - 環境構築方法の説明
  - スクリプトの共有

## ディレクトリ構成

```shell
.
├── README.md          READMEファイル。環境構築方法などの説明も記載。
├── docs               その他ドキュメント類
├── src                ソースコード群。適宜サブディレクトリを作成することも可。
└── tests              srcディレクトリのスクリプトのテストコード。
```

# 環境構築方法（ハンズオン用）

**申し送り事項**  
- プロキシの設定が別途必要になるケースがあります

## 環境構築
### gitのインストール

gitがインストールされていない場合は下記手順でインストールしてください。

- Mac:
```
$ brew install git
```
- Linux（Ubuntu）:
```
$ sudo apt-get install git
```
- Windows:
git for windows のサイトからダウンロードしてインストールします  
https://gitforwindows.org/

### git設定

```
$ # ユーザー名とメールアドレスの設定
$ git config --global user.name <your_name>
$ git config --global user.email <mail_address>
$
$ # (必要な時のみ実行) プロキシの設定
$ git config --global http.proxy http://10.63.0.11:8080
$ git config --global https.proxy http://10.63.0.11:8080
$
$ # 設定の確認
$ git config -l
```

## VSCodeの設定

### VSCodeのインストール

以下のURLからダウンロード
https://code.visualstudio.com/

### VSCodeの拡張機能インストール

VSCodeの`Extension`から以下の拡張機能をインストールします。
* python
* gitlens
* git graph
* remote-ssh

### (Windowsユーザー向け)VSCodeのデフォルトターミナルをGitBashにする

1. `File`→`Preferences`→`Settings`と選択
2. 検索窓に`Terminal.Integrated.Default Profile: Windows`と入力
3. プルダウンの中から「Git Bash」をクリック
※VSCodeターミナル右側の「+」マークをクリックすることでGit Bashを使用できるようになる

## Github設定

### アカウントの作成方法

https://github.com/ にアクセスし、「Sign up」から必要情報を入力する

### アカウントへのSSHキー設定

以下の手順で SSH キーペアを生成し、GitHub へ公開鍵を登録すれば SSH でGitHubのリポジトリにアクセスできるようになります。

1. SSH キーペアを生成します
```
$ ssh-keygen -t rsa -b 4096 -C '<mail_address>' -f ~/.ssh/github_key
```
2. ~/.ssh/config に GitHub 用の設定を追加します

```
Host            github.com
  HostName      github.com
  User          git
  IdentityFile  ~/.ssh/github_key
```
VSCodeでは以下のコマンドでファイルを開けます
```
code ~/.ssh/config
```

※VS Codeの拡張機能「Remote-SSH」が導入済みであれば、「REMOTE EXPLORER」タブから設定ファイルを編集可能です

3. GitHub アカウントに公開鍵を設定します
  a. GitHub 画面右上にあるアカウントをクリックし、「Settings」を選択します
  b. 左メニューから「SSH and GPG keys」を選択します
  c. 「New SSH key」ボタンをクリックし、キーの名前（任意の名前）と 1. で生成した公開鍵（~/.ssh/github_key.pub）を設定します

4. 以下のsshコマンドを実行し、疎通確認をします
```
ssh -T git@github.com
```



# 環境構築(fizzbuzz演習用)

演習で使用するライブラリを仮想環境上にインストールします。今回は仮想環境をpoetryで作成します。

## pythonとpoetryのインストール

使用する環境によりインストール手順が異なります。  
講師の指示に従ってインストール手順に沿ってインストールしてください。

- [公式のPythonを使用する場合(docs/poetry_venv.md)](docs/poetry_venv.md)
- [Minicondaを使用する場合(docs/poetry_miniconda.md)](docs/poetry_miniconda.md)
- [pyenvを使用する場合(docs/poetry_pyenv.md)](docs/poetry_pyenv.md)

## poetryの環境作成先の変更
```
poetry config --list
poetry config virtualenvs.in-project true
```

## poetry仮想環境作成

poetryはPythonの仮想環境とパッケージ管理ツールです。

**仮想環境作成とパッケージインストール手順**

`python_template`直下で以下のコマンドを実行します。
※windowsの方はコマンドプロンプトから実行してください。

```
poetry install
```

**仮想環境への切り替え方法**

```
poetry shell
```


## （仮想環境を有効化した状態で）VSCodeの起動方法
<span style="font-size: 150%; color: red;">`python_template`ディレクトリ直下まで移動し、</span>
- mac: ターミナル
- windows: コマンドプロンプト
から以下のコマンドを実行してください。
```
# すでにpoetry shellしている場合はcodeコマンドのみでOK
poetry shell
code .
```

### codeコマンドが見つからない場合
※`code`コマンドの有効化
- windowsの場合

codeコマンドがみつからないときはスタートメニューで `環境変数を編集` を開き、PATHを編集して↓の値を追加してください。
```
%HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Microsoft VS Code\bin
```
- macの場合
Visual Studio Codeを起動して、`command + shift + P`でコマンドパレットを開き、`shell command install`で検索し、
```
シェルコマンド: PATH内に `code` コマンドをインストールします
```
を選択します。

## VSCode起動後の設定

1. 拡張機能からPythonの拡張機能をインストール
  - 画面左部の拡張機能をクリックし、Pythonと入力
  - Pythonをインストール
2. VSCodeで使用するPythonインタプリタを選択
  - コマンドパレットを開き、`> Python: Select Interpreter`と入力
    - Windows: `Ctrl + Shift + P` でコマンドパレットを開く
    - Windows: `Command + Shift + P` でコマンドパレットを開く
  - 使用するPython環境名を選択 (講師の指示に従ってください)


# 追加の設定

## pre-commitの設定
pre-commitがインストールされた環境で以下のコマンドを実行します。
```
poetry shell
pre-commit install
```

## pytest実行手順

- poetry仮想環境下でのテストは以下のコマンドにより実行する
```zsh
pytest tests/test_fizzbuzz.py
```

# 参考（時間がある人向け）

## 参考: Linter、FormatterとのVS Codeの連携
Formatterとしてblack、isort、
Linterとしてflake8を用います。セーブ時にこれらが自動で実行されるように設定します。

### blackの設定
1. VSCode上で設定画面を開きます
  - Macの場合：「command」+「,」
  - Windowsの場合：「ctrl」+「,」
2. 検索窓に「Format On」と入力します
3. 「Python › Formatting: Provider」のプルダウンを開いて、autopep8からblackに変更してください
4. 「Format On Save」のボックスにチェックを入れます。これにより保存したタイミングで自動でフォーマットされます

### isortの設定
1. VSCode上で設定画面を開きます
  - Macの場合：「command」+「,」
  - Windowsの場合：「ctrl」+「,」
2. 検索窓に「Editor: Code Actions On Save」を入力します
3. 「settings.json で編集」を選択します
4. 「editor.codeActionsOnSave」を以下のように変更します
- 変更前
```
"editor.codeActionsOnSave": null
```
- 変更後
```
"editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
```
### flake8の設定
1. VSCode上で設定画面を開く
  - Macの場合：「command」+「,」
  - Windowsの場合：「ctrl」+「,」
2. 検索窓に「Python › Linting」と入力し、「Enabled」にチェックを入れます
3. 「Python › Linting: Pylint Enabled」のチェックを外します
4. 「Python › Linting: Flake8 Enabled」にチェックを入れます

### pre-commitのインストール
1. ライブラリをインストールします
  ```
  poetry add pre-commit
  ```
2. 設定ファイルを追跡対象に追加します
  ```
  git add .pre-commit-config.yaml
  ```
3. commitを実行します
  ```
  git commit -m "pre-commit settings"
  ```
4. 以下を実行します
  ```
  pre-commit install
  ```
### formatter/linterのインストール
poetryで作成した仮想環境に入り、以下を追加インストールします（今回はインストール済みなので不要です)
```
poetry add black isort flake8
```
## 各種リンク

- pythonの実験環境構築: https://data.gunosy.io/entry/can-you-reproduce-the-experiment-pyenv-poetry
- pythonのパッケージ管理について: https://vaaaaaanquish.hatenablog.com/entry/2021/03/29/221715
- Google Style Python Docstringsの説明: https://qiita.com/11ohina017/items/118b3b42b612e527dc1d
- pytest
  - ブログ: https://www.m3tech.blog/entry/pytest-summary
  - 書籍: https://www.amazon.co.jp/%E3%83%86%E3%82%B9%E3%83%88%E9%A7%86%E5%8B%95Python-Brian-Okken/dp/4798157600
