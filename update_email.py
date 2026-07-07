import glob

old_email = "c23068324@gmail.com"
new_email = "c23068324@gmail.com"

files_to_check = glob.glob("*.html") + glob.glob("*.py")

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_email in content:
        new_content = content.replace(old_email, new_email)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated email in {filepath}")

print("Done updating email.")
