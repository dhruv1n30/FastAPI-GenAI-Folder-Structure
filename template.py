import os

def create_folder_structure():
    # Define the project structure
    project_structure = {
        "your_project": {
            "app": {
                "__init__.py": "",
                "main.py": "# FastAPI application entry point\n",
                "core": {
                    "__init__.py": "",
                    "config.py": "# Application settings and environment variables\n",
                    "database.py": "# Database connection and session management\n",
                    "security.py": "# Authentication and authorization logic\n"
                },
                "api": {
                    "__init__.py": "",
                    "v1": {
                        "__init__.py": "",
                        "endpoints": {
                            "__init__.py": "",
                            "genai.py": "# Endpoints for GenAI interactions\n",
                            "users.py": "# Example: User-related endpoints\n"
                        },
                        "schemas": {
                            "__init__.py": "",
                            "genai.py": "# Pydantic models for GenAI requests/responses\n",
                            "users.py": "# Example: Pydantic models for users\n"
                        }
                    }
                },
                "services": {
                    "__init__.py": "",
                    "genai_service.py": "# Business logic for GenAI interactions (e.g., calling LLMs)\n",
                    "user_service.py": "# Example: Business logic for user management\n"
                },
                "models": {
                    "__init__.py": "",
                    "genai_models.py": "# Database models related to GenAI (if applicable)\n",
                    "user_models.py": "# Example: Database models for users\n"
                },
                "utils": {
                    "__init__.py": "",
                    "helper_functions.py": "# General utility functions\n"
                }
            },
            "tests": {
                "__init__.py": "",
                    "test_genai_endpoints.py": ""
            },
            ".env": "# Environment variables\n",
            "requirements.txt": "# Project dependencies\n",
            "README.md": "# Project README\n"
        }
    }

    def create_files(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                # Create directory
                os.makedirs(path, exist_ok=True)
                # Recursively create files and folders
                create_files(path, content)
            else:
                # Create file with content
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

    # Create the project structure
    create_files(".", project_structure)
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()