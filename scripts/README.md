# Scripts

This directory contains various utility scripts for development tasks.

## Instructions

To set up and run the scripts in this directory, follow these steps:

1. Create a virtual environment:
   ```bash
   python -m venv .env
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .env/bin/activate
     ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the desired script from the `scripts` directory.
   ```bash
   python your_script.py
   ```
5. Update `requirements.txt` if you install new packages:
   ```bash
   pip freeze > requirements.txt
   ```
6. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

> [!IMPORTANT]
> Make sure to check the individual script directories for any additional instructions or dependencies.
