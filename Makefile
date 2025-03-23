# Use bash as the shell
SHELL=/bin/bash

# Virtual environment directory
VENV_DIR=venv

# Setup the virtual environment and install requirements
setup:
        @echo "Setting up virtual environment..."
        python3 -m venv $(VENV_DIR)
        source $(VENV_DIR)/bin/activate && pip install -r requirements.txt
        @echo "Virtual environment setup complete."

# Run the Flask app
run:
        @echo "Running Flask app..."
        source $(VENV_DIR)/bin/activate && python app.py

# Clean up the virtual environment and cache (compatible with macOS)
clean:
        @echo "Cleaning up..."
        rm -rf $(VENV_DIR)
        find . -name "*.pyc" -delete
        find . -name "__pycache__" -exec rm -rf {} +
        @echo "Cleanup complete."

