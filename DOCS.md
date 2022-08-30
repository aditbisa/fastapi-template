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
    ```
    poetry add <python-library>
    ```
