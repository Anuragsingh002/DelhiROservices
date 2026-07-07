import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract head, header, footer
head_match = re.search(r'(<head>.*?</head>)', html, flags=re.DOTALL)
header_match = re.search(r'(<header.*?</header>)', html, flags=re.DOTALL)
footer_match = re.search(r'(<footer.*?</footer>)', html, flags=re.DOTALL)

head = head_match.group(1) if head_match else ''
header = header_match.group(1) if header_match else ''
footer = footer_match.group(1) if footer_match else ''

def create_page(filename, title, content):
    page_html = f"""<!DOCTYPE html>
<html lang="en">
{head}
<style>
  .legal-section {{ padding: 100px 0 60px; background: #f8fafc; min-height: 60vh; }}
  .legal-container {{ max-width: 800px; margin: 0 auto; background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
  .legal-container h1 {{ color: var(--primary); margin-bottom: 20px; font-family: var(--font-head); }}
  .legal-container h2 {{ margin-top: 30px; margin-bottom: 15px; color: var(--text-dark); font-size: 1.2rem; }}
  .legal-container p, .legal-container li {{ margin-bottom: 15px; line-height: 1.6; color: var(--text-mid); }}
  .legal-container ul {{ padding-left: 20px; margin-bottom: 20px; }}
</style>
<body>
{header}
<section class="legal-section">
  <div class="container">
    <div class="legal-container">
      <h1>{title}</h1>
      {content}
    </div>
  </div>
</section>
{footer}
</body>
</html>"""
    
    # Fix the title tag in the head for each page
    page_html = re.sub(r'<title>.*?</title>', f'<title>{title} - Delhi RO Service</title>', page_html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_html)

privacy_content = """
<p>At Delhi RO Service, accessible from our website, one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by Delhi RO Service and how we use it.</p>
<h2>Information We Collect</h2>
<p>The personal information that you are asked to provide, and the reasons why you are asked to provide it, will be made clear to you at the point we ask you to provide your personal information.</p>
<p>If you contact us directly, we may receive additional information about you such as your name, email address, phone number, the contents of the message and/or attachments you may send us, and any other information you may choose to provide.</p>
<h2>How We Use Your Information</h2>
<ul>
  <li>Provide, operate, and maintain our website and services</li>
  <li>Improve, personalize, and expand our website</li>
  <li>Understand and analyze how you use our website</li>
  <li>Communicate with you for customer service and updates</li>
  <li>Process your service requests and bookings</li>
</ul>
"""

terms_content = """
<p>Welcome to Delhi RO Service!</p>
<p>These terms and conditions outline the rules and regulations for the use of Delhi RO Service's Website and services.</p>
<h2>Independent Service Provider</h2>
<p>We provide independent repair and maintenance services for RO water purifiers of multiple brands. We are not an official or authorized service center for any specific brand.</p>
<h2>Service Booking and Execution</h2>
<p>By booking a service with us, you agree to provide accurate information regarding your location and the issue with your RO unit. Our engineers strive to provide same-day service within the Delhi NCR region, subject to availability.</p>
<h2>Pricing and Payments</h2>
<p>All prices quoted are subject to inspection by our technicians. Final pricing will be provided before any repair work commences. Customers must pay the agreed amount upon successful completion of the service.</p>
"""

refund_content = """
<p>Thank you for choosing Delhi RO Service.</p>
<h2>Refunds</h2>
<p>If you are not entirely satisfied with your repair service, we're here to help. Since we offer physical repair and maintenance services, refunds are generally processed only if the installed spare parts are found to be defective within the warranty period (as stated on the invoice).</p>
<h2>Cancellations</h2>
<p>You can cancel your service booking at any time before the technician is dispatched to your location without any cancellation fee. If a technician has already arrived at your location, a nominal visitation fee may apply even if you choose not to proceed with the repair.</p>
"""

about_content = """
<p>Delhi RO Service is a trusted, independent service provider dedicated to offering high-quality RO water purifier repair, maintenance, and installation services across the Delhi NCR region.</p>
<h2>Who We Are</h2>
<p>We are a team of experienced and skilled technicians who understand the importance of clean, safe drinking water for your family. We specialize in servicing multi-stage RO systems of all major brands.</p>
<h2>Our Commitment</h2>
<ul>
  <li><strong>Experienced RO Technicians:</strong> Our professionals are trained to handle complex repairs efficiently.</li>
  <li><strong>High-Quality Genuine Parts:</strong> We use authentic components to ensure the longevity of your water purifier.</li>
  <li><strong>Transparent Pricing:</strong> No hidden costs. We believe in clear, upfront pricing for all our services.</li>
</ul>
<p>We serve customers across Delhi, Noida, Gurgaon, Ghaziabad, and Faridabad.</p>
"""

contact_content = """
<p>We are here to help you with all your RO water purifier needs. Reach out to us using the details below:</p>
<h2>Contact Information</h2>
<p><strong>Service Helpline:</strong> <a href="tel:8340452413" style="color:var(--primary); font-weight:bold;">8340452413</a></p>
<p><strong>Email Address:</strong> <a href="mailto:c23068324@gmail.com" style="color:var(--primary);">c23068324@gmail.com</a></p>
<p><strong>Service Area:</strong> Delhi NCR (Delhi, Noida, Gurgaon, Ghaziabad, Faridabad)</p>
<p><strong>Business Address:</strong> P-67, Anuj Vihar, Sankar Vihar, Delhi NCR</p>
<h2>Working Hours</h2>
<p><strong>Customer Support:</strong> Available 24×7</p>
<p><strong>Engineer Visits:</strong> 8:00 AM – 8:00 PM (All days)</p>
"""

create_page('privacy-policy.html', 'Privacy Policy', privacy_content)
create_page('terms-conditions.html', 'Terms & Conditions', terms_content)
create_page('refund-policy.html', 'Refund & Cancellation Policy', refund_content)
create_page('about-us.html', 'About Us', about_content)
create_page('contact-us.html', 'Contact Us', contact_content)

print("Legal pages generated successfully.")
