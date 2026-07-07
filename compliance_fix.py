import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta and Headings
html = html.replace('in PAN India', 'in Delhi NCR')
html = html.replace('🏆 #1 RO Service Provider', '🏆 Experienced RO Technicians')

# Geographic misrepresentations
html = html.replace('across PAN India', 'across Delhi NCR')
html = html.replace('all across PAN India', 'all across Delhi NCR')
html = html.replace('across India', 'across Delhi NCR')
html = html.replace('PAN India', 'Delhi NCR')

# Authorization claims
html = html.replace('authorized, original components', 'high-quality, genuine components')
html = html.replace('from authorized suppliers', 'from reliable suppliers')
html = html.replace('authorized spare parts', 'genuine spare parts')

# Toll free
html = html.replace('Toll Free Number', 'Service Helpline')
html = html.replace('toll-free number', 'Service Helpline')
html = html.replace('(Toll Free)', '(Call Us)')

# Exaggerated claims
html = html.replace("India's largest and fastest growing independent RO water purifier service provider. We undertake service, AMC, repair, and maintenance of all brands across Delhi NCR with over 20 lac happy customers.", "A trusted independent RO water purifier service provider. We provide service, AMC, repair, and maintenance for multiple brands across Delhi NCR.")
html = html.replace("Instant support", "Professional support")
html = html.replace("instant support", "professional support")
html = html.replace("We are the Largest &amp; Fastest Growing Service Provider", "We are an experienced service provider")

# Disclaimer update
old_disclaimer = "This is an independent service centre. We are an experienced service provider and undertake job work of Service, AMC, Repair &amp; Maintenance of RO Service &amp; repair. We are totally responsible for these services and have no relation to any RO purifier manufacturer company in any regard."
new_disclaimer = "This is an independent service centre. We provide repair and maintenance services for RO water purifiers of multiple brands. We are not an official or authorized service center for any specific brand."
html = html.replace(old_disclaimer, new_disclaimer)
# Also try replacing the original just in case it wasn't modified yet:
orig_disclaimer = "This is an independent service centre. We are the Largest &amp; Fastest Growing Service Provider and undertake job work of Service, AMC, Repair &amp; Maintenance of RO Service &amp; repair. We are totally responsible for these services and have no relation to any RO purifier manufacturer company in any regard."
html = html.replace(orig_disclaimer, new_disclaimer)

# Footer Links Updates
# We need to update the Quick Links and Bottom links to point to the real pages
html = html.replace('<li><a href="#"><i class="fas fa-chevron-right"></i> Privacy Policy</a></li>', '<li><a href="privacy-policy.html"><i class="fas fa-chevron-right"></i> Privacy Policy</a></li>\n          <li><a href="terms-conditions.html"><i class="fas fa-chevron-right"></i> Terms & Conditions</a></li>\n          <li><a href="refund-policy.html"><i class="fas fa-chevron-right"></i> Refund Policy</a></li>')

html = html.replace('<p>Copyright © 2024 Delhi RO Repairing Service. All rights reserved. | <a href="#">Privacy Policy</a></p>', '<p>Copyright © 2024 Delhi RO Repairing Service. All rights reserved. | <a href="privacy-policy.html">Privacy Policy</a> | <a href="terms-conditions.html">Terms & Conditions</a> | <a href="refund-policy.html">Refund Policy</a></p>')

# Save the fixed index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html compliance replacements completed.")
