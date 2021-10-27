# Sanic-Pra

Sanic を用いて RESTful API を実装したい.<br>

# Todo List API

## File structure

```
    dockerfiles/
            ├- db/
            │   ├- docker-compose.yml
            └- test_db/
                └- docker-compose.yml
    SanicApiPra/
            ├- tests/
            │     ├- __inint__.py
            │     └- test_api.py
            │
            ├- __inint__.py
            └- main.py
    README.md
    requirements.txt
```

## Install

```shell
    $ pip install -r requirements.txt
```

## Setup

```shell
    $ cd docker/db/
    $ docker-compose up -d
    $ cd SanicApiPra/
    $ python3 main.py
    # localhost:8000/
```

<!-- First ,you need to create new database and change the dbname in the source code. -->

最初に Database を作成し、ソースコードに追加(編集)する必要があります。


## Poetry

```shell
    # 仮想環境の作成
    $ poetry new api_sanic
    # 仮想環境の有効化
    $ poetry shell 
    # 
    $ poetry add (パッケージ名)
    # pyproject.tomlに記載のパケージをインストール
    $ poetry install
```