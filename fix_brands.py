import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

brands = [
    "Kent", "Aquaguard", "Pureit", "Livpure", "Whirlpool", "HUL", 
    "V-Guard", "Blue Star", "Eureka Forbes", "Tata Swach", 
    "A.O. Smith", "Havells", "LG", "Samsung", "Panasonic"
]

# Generate new compliant HTML
new_brands_html = '<div class="brands-grid" style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: center;">\n'
for brand in brands:
    new_brands_html += f'      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px 30px; border-radius: 30px; font-weight: bold; color: var(--text-dark); display: flex; align-items: center; gap: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.03);"><i class="fas fa-check-circle" style="color: var(--primary);"></i> {brand}</div>\n'
new_brands_html += '    </div>'

# Regex to replace the old brands-grid block
pattern = re.compile(r'<div class="brands-grid">.*?</div>\n    </div>\n  </div>\n</section>', re.DOTALL)

replacement = f'{new_brands_html}\n  </div>\n</section>'

if re.search(pattern, html):
    html = re.sub(pattern, replacement, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced brands grid successfully.")
else:
    print("Could not match the brands grid pattern.")
