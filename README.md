# hello-nox
Toy project to play test nox


```sh
brew install pyenv

eval $(pyenv init --path)

# Works on M1 arm64
pyenv install 2.7.18

# Failing on M1 arm64
pyenv install 3.4.10
pyenv install 3.5.10

# These are fine
pyenv install 3.6.15
pyenv install 3.7.13
pyenv install 3.8.12
pyenv install 3.9.10
pyenv install 3.10.3


poetry init
poetry add -D nox virtualenv
poetry shell
poetry install

python3 pyenv_discovery.py

PATH=$PATH:/Users/username/.pyenv/versions/2.7.18/bin:/Users/username/.pyenv/versions/3.9.10/bin:/Users/username/.pyenv/versions/3.10.3/bin:/Users/username/.pyenv/versions/3.6.15/bin:/Users/username/.pyenv/versions/3.7.13/bin:/Users/username/.pyenv/versions/3.8.12/bin

nox
```
