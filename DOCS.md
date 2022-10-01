# Documentation


## ✅ First Setup

1. Initialise project
    ```
    poetry init
    ```

2. Install pre-commit hooks
    ```
    pre-commit install --install-hooks
    ```

2. Vscode workspace setting with [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension
    ```
    {
        "python.defaultInterpreterPath": "/home/*/.cache/pypoetry/virtualenvs/rest-template-***/"
    }
    ```

## 🏃‍♂️ Running

- Development mode
    ```
    ./start.sh
    ```


## 📦 Packages

- Add new python package into project
    
    Poetry tend to upgrade unrelated package and its takes a long time to resolve.
    To avoid it when add/upgrade single package, change the `pyproject.toml` manually and then execute:
    ```
    poetry lock --no-update
    poetry install
    ```


## 🌲 File Hierarchy

To avoid circular dependencies, here's a guide line of the file hierarchy:
- /config.py
- /utils.py
- /database.py ; /models.py ; /schemas/*
- /services/*
- /routers/*
