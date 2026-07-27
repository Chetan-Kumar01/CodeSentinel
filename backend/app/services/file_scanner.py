import os

def scan_python_files(project_path):

    python_files = []

    for root, dirs, files in os.walk(project_path):

        # Ignore macOS metadata folders
        dirs[:] = [d for d in dirs if d != "__MACOSX"]

        for file in files:

            # Ignore hidden metadata files
            if file.startswith("._"):
                continue

            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                python_files.append(full_path)

    return python_files