import os
import yara

def scan_directory(directory_path, rule_file):
    try:
        # Compile the YARA rule from the provided file
        compiled_rule = yara.compile(filepath=rule_file)

        # Walk through the directory and scan files
        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "rb") as file:
                        data = file.read()
                        matches = compiled_rule.match(data=data)
                        if matches:
                            print(f"Match found in {file_path}: {matches[0].rule}")
                except Exception as e:
                    print(f"Error scanning {file_path}: {e}")
    except Exception as e:
        print(f"Error compiling YARA rule: {e}")

if __name__ == "__main__":
    target_directory = "/path/to/your/directory"  # Replace with the directory you want to scan
    yara_rule_file = "/path/to/your/my_rules.yar"  # Replace with the path to your YARA rule file
    scan_directory(target_directory, yara_rule_file)
