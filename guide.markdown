After running the script:

1. **Activate the virtual environment using**:

    ```bash
    source flask_mariadb_venv/bin/activate  # On UNIX systems (Linux/macOS)
    .\flask_mariadb_venv\Scripts\activate    # On Windows
    ```

2. **Update the database credentials** in `app.py`.

3. **Set up your database using**:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

4. **Run your app**:

    ```bash
    python app.py
    ```
