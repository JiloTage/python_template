Python環境構築手順 (公式版Python)
===

## Windows

### Pythonのインストール

こちらより `Windows installer (64-bit)` をインストールしてください。

- https://www.python.org/downloads/release/python-3913/

### poetryのインストール

コマンドプロンプトまたはpowershellで下記コマンドを実行してください。

```
pip install poetry==1.3.1
```

## Mac

### Pythonのインストール

以下を実行してください。
```
brew install python@3.9
```
pythonのパスを以下のコマンドで通します。バージョンは適宜調整してください。
```
echo "PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:\${PATH}" > ~/.zshrc
echo "export PATH"
```

### poetryのインストール

下記コマンドを実行してください。

```
pip install poetry==1.3.1
```
