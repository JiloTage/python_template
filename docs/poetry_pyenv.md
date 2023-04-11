Python環境構築手順 (pyenv)
===

pyenvとは任意のPythonバージョンを指定して利用するためのツールです。

## Windows

### pyenvとPythonのインストール

下記手順でpyenv-winをインストールしてください。

- Step1: コマンドプロンプトで下記コマンドを実行
  ```bash
  pip install pyenv-win --target %USERPROFILE%\\.pyenv
  ```
  https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#python-pip


- Step2: PowerShellで下記コマンドを実行 (4コマンド全て)
  ```powershell
  [System.Environment]::SetEnvironmentVariable(‘PYENV’,$env:USERPROFILE + “\.pyenv\pyenv-win\“,”User”)

  [System.Environment]::SetEnvironmentVariable(‘PYENV_ROOT’,$env:USERPROFILE + “\.pyenv\pyenv-win\“,”User”)

  [System.Environment]::SetEnvironmentVariable(‘PYENV_HOME’,$env:USERPROFILE + “\.pyenv\pyenv-win\“,”User”)

  [System.Environment]::SetEnvironmentVariable(‘path’, $env:USERPROFILE + “\.pyenv\pyenv-win\bin;” + $env:USERPROFILE + “\.pyenv\pyenv-win\shims;” + [System.Environment]::GetEnvironmen
  ```

  https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#add-system-settings

- Step3: Pythonをインストール
  ```
  pyenv install 3.9.13
  pyenv global 3.9.13
  ```

### poetryのインストール

下記コマンドを実行してください。

```
pip install poetry==1.3.1
```


## Mac

### pyenvとPythonのインストール

下記手順でpyenvをインストールしてください。
- 1. Homebrewでpyenvインストール
```
brew update
brew install pyenv
```
- 2. pyenvの設定
  ```zsh
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init -)"' >> ~/.zshrc
  ```
- 3. shellの再起動
  ```
  exec "$SHELL"
  ```
- 4. pythonインストール
  ```
  pyenv install 3.9.13
  pyenv global 3.9.13
  ```

### poetryのインストール

下記コマンドを実行してください。

```
pip install poetry==1.3.1
```
