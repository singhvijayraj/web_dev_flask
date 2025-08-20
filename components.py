import os

# Directories and files to create
structure = {
    "app": {
        "__init__.py": "",
        "routes": {
            "__init__.py": "",
            "public_routes.py": "# Handles public pages\n",
            "admin_routes.py": "# Handles admin pages\n"
        },
        "models": {
            "__init__.py": "",
            "user.py": "# User model will go here\n"
        },
        "templates": {
            "base.html": "<!-- Base HTML template -->\n"
        },
        "static": {
            "css": {},
            "js": {}
        },
        "forms": {
            "__init__.py": "",
            "login_form.py": "# Login form using Flask-WTF\n"
        },
        "utils": {
            "__init__.py": "",
            "helpers.py": "# Helper functions go here\n"
        }
    },
    "instance": {
        "config.py": "# Config settings for Flask app\n"
    },
    "tests": {
        "__init__.py": "",
        "test_basic.py": "# Basic test file\n"
    },
    # Root files
    "run.py": "# Entry point to run Flask app\n"
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create directory
            os.makedirs(path, exist_ok=True)
            # Recurse into directory
            create_structure(path, content)
        else:
            # Create file if not exists
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Created file: {path}")
            else:
                print(f"File already exists: {path}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    create_structure(project_root, structure)
    print("\nAll directories and files have been created.")

