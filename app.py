from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageChops, ImageEnhance
import os
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# Ensure upload and result folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

def perform_ela_analysis(input_image_path, output_image_path, quality=95):
    """
    Perform Error Level Analysis (ELA) on an image to detect potential manipulations.
    """
    temp_path = None
    try:
        # Open the original image
        original = Image.open(input_image_path)
        
        # Create a temporary file for the recompressed image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_path = temp_file.name
            original.save(temp_path, "JPEG", quality=quality)
        
        # Open the recompressed image
        recompressed = Image.open(temp_path)
        
        # Perform ELA by finding the difference between the original and recompressed images
        ela_image = ImageChops.difference(original, recompressed)
        
        # Enhance the differences for better visibility
        extrema = ela_image.getextrema()
        if isinstance(extrema[0], tuple):  # Multi-channel image (e.g., RGB)
            max_diff = max([ex[1] for ex in extrema])
        else:  # Single-channel image (e.g., grayscale)
            max_diff = extrema[1]

        scale = 255.0 / max_diff if max_diff != 0 else 1
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
        
        # Save the ELA result image
        ela_image.save(output_image_path)
    finally:
        # Clean up the temporary file
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file is uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        # Get the quality value from the form
        quality = request.form.get('quality', 95)
        try:
            quality = int(quality)
        except ValueError:
            quality = 95  # Default to 95 if invalid input
        
        # Save the uploaded file
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(input_path)
        
        # Perform ELA analysis
        output_filename = f"ela_{file.filename}"
        output_path = os.path.join(app.config['RESULT_FOLDER'], output_filename)
        perform_ela_analysis(input_path, output_path, quality)
        
        # Pass the file paths to the template
        return render_template('index.html', original=file.filename, result=output_filename, quality=quality)
    
    return render_template('index.html', original=None, result=None, quality=None)

if __name__ == '__main__':
    app.run(debug=True)