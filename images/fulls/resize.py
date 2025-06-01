from PIL import Image
import os

# Target size
width, height = 1600, 2000

# Loop through all files in the current folder
for filename in os.listdir('.'):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        try:
            # Open image
            with Image.open(filename) as img:
                # Resize the image
                resized = img.resize((width, height), Image.ANTIALIAS)

                # Build new filename
                base_name = os.path.splitext(filename)[0]
                new_filename = f"{base_name}.webp"

                # Save as WebP
                resized.save(new_filename, 'WEBP', quality=85)

                print(f"Converted: {filename} → {new_filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")