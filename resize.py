from PIL import Image
import os

paths=['1.jpg','2.jpg','3.jpg']
def resize_image(input_path, output_path, target_size):
    # Open the image
    image = Image.open(input_path).convert("RGB")
    image.thumbnail(target_size)
    min_quality = 1  # Min quality
    max_quality = 100  # Max quality
    target_file_size = 720 * 720  # final out size this is nearl 500kb
    # print(target_file_size)
    # Binary search to find the optimal quality value
    while min_quality < max_quality:
        quality = (min_quality + max_quality) // 2
        image.save(output_path, optimize=True, quality=quality)
        file_size = os.path.getsize(output_path)
        if file_size < target_file_size:
            min_quality = quality + 1
        elif file_size > target_file_size:
            max_quality = quality - 1
        else:
            break
    image.save(output_path, optimize=True, quality=min_quality)

target_size = (1920, 1080)  # e.g., (width, height)

for index,path in enumerate(paths):
    input_path = path  
    output_path = 'out/'+path  # Path to save the resized image
    try:
        resize_image(input_path, output_path, target_size)
    except Exception as e:
        print(path)

# # Target size in pixels (adjust as desired)

