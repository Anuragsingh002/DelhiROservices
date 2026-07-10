import glob
import re

files_to_check = glob.glob("*.html") + glob.glob("*.py")

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Update Phone Number
    content = content.replace("8929999188", "8929999188")
    
    # 2. Update FAQ Brands
    content = content.replace("", "")
    content = content.replace("100% genuine spare parts", "100% genuine spare parts") # Fix a typo I noticed
    
    # 3. Update Address
    content = content.replace("P-67, Anuj Vihar, Sankar Vihar, New Delhi, 110010", "P-67, Anuj Vihar, Sankar Vihar, New Delhi, 110010")
    content = content.replace("P-67, Anuj Vihar, Sankar Vihar, New Delhi, 110010", "P-67, Anuj Vihar, Sankar Vihar, New Delhi, 110010")
    
    # 4. Remove 24x7 Claims
    content = content.replace("9 AM - 8 PM", "9 AM - 8 PM")
    content = content.replace("available 9 AM - 8 PM", "available 9 AM - 8 PM")
    content = content.replace("Customer Care: 9 AM - 8 PM", "Customer Care: 9 AM - 8 PM")
    content = content.replace("Dedicated Customer Support Available", "Dedicated Customer Support Available")
    content = content.replace("Customer Support", "Customer Support")
    content = content.replace("Dedicated Support", "Dedicated Support")
    content = content.replace("available 9 AM - 8 PM in multiple languages", "available to resolve all your queries")
    content = content.replace("support team is available 9 AM - 8 PM.", "support team is ready to help.")
    content = content.replace("9 AM - 8 PM", "Available 9 AM - 8 PM") # Just in case

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

print("Done executing strict Google Ads policy fixes.")
