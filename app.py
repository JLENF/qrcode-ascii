from flask import Flask, render_template, request, url_for
import os
import requests
from PIL import Image, ImageEnhance
from io import BytesIO
import uuid

app = Flask(__name__)

def get_qr_code_image(text):
    """Get a QR code image from the QR Server API"""
    # Create QR code URL
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={text}"
    
    # Download the QR code image
    response = requests.get(qr_url)
    if response.status_code != 200:
        raise Exception("Failed to generate QR code image")
    
    return BytesIO(response.content), qr_url

def convert_qr_to_ascii(image_data):
    """Convert a QR code image to ASCII art using a simple and reliable approach"""
    # Open the image
    img = Image.open(image_data).convert('L')  # Convert to grayscale
    
    # Enhance contrast for better black/white separation
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # Increase contrast
    
    # Apply threshold to make it truly black and white
    threshold = 128
    img = img.point(lambda p: p > threshold and 255 or 0)
    
    # Get image dimensions
    width, height = img.size
    
    # Calculate an appropriate module size (scaling factor)
    # For complex QR codes (URLs), we need a smaller module size
    module_size = max(2, min(width, height) // 40)
    
    # Create ASCII representation
    ascii_qr = ""
    
    # Process the image in pairs of rows to account for half-block characters
    for y in range(0, height - module_size, module_size * 2):
        line = ""
        for x in range(0, width, module_size):
            # Check if coordinates are within bounds
            if y + module_size >= height or x >= width:
                line += " "  # Out of bounds, add a space
                continue
            
            # Get the top and bottom pixels
            top_pixel = img.getpixel((x, y)) < 128  # True if black
            bottom_pixel = img.getpixel((x, y + module_size)) < 128  # True if black
            
            # Choose appropriate character based on pixel values
            if top_pixel and bottom_pixel:
                line += "█"  # Full block
            elif top_pixel and not bottom_pixel:
                line += "▀"  # Top half block
            elif not top_pixel and bottom_pixel:
                line += "▄"  # Bottom half block
            else:
                line += " "  # Space
        
        # Only add non-empty lines to the output
        if line.strip():
            ascii_qr += line + "\n"
    
    # If ASCII QR is empty or too small, use a fallback method
    if len(ascii_qr.strip().split('\n')) < 10:  # Not enough lines
        ascii_qr = generate_fallback_ascii_qr(img, module_size)
    
    return ascii_qr.rstrip()


def generate_fallback_ascii_qr(img, module_size):
    """Generate a fallback ASCII QR code using a simpler approach"""
    width, height = img.size
    ascii_qr = ""
    
    # Simple approach: just sample at regular intervals
    for y in range(0, height, module_size):
        line = ""
        for x in range(0, width, module_size):
            if x < width and y < height and img.getpixel((x, y)) < 128:
                line += "█"  # Black pixel = full block
            else:
                line += " "  # White pixel = space
        
        if line.strip():  # Only add non-empty lines
            ascii_qr += line + "\n"
    
    return ascii_qr

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text.strip():
            try:
                # Generate QR code
                image_data, image_url = get_qr_code_image(text)
                
                # Convert to ASCII
                ascii_qr = convert_qr_to_ascii(image_data)
                
                return render_template('result.html', 
                                       ascii_qr=ascii_qr, 
                                       image_url=image_url, 
                                       text=text)
            except Exception as e:
                error_message = str(e)
                return render_template('index.html', error=error_message)
                
    return render_template('index.html')

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True, host='0.0.0.0', port=5001)
