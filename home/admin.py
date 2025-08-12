from PIL import Image
image_path = 'your_image.jpg'
try:
    img = Image.open(image_path)
    img.show()
except FileNotFoundError:
    print(f"Error: Image file not found at '{image_path}'")
except Exception as e:
    print(f"An error occured: {e}")        