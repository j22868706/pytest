### Pytest
- Auto-discovery of tests
- Install
    ```
    pip install pytest
    ```

### Virtual Environments and Packages
- Creating virtual environment
    ```python
    python -m venv tutorial-env
    source tutorial-env/bin/activate
    ```

### Resolve Errors
- Cannot import module while using virtualenv
    - Error messages
        ```
        import source.my_functions as my_functions
        E   ModuleNotFoundError: No module named 'source'
        ```
    - Solution: to add __init__.py in tests folder
