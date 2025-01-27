from PIL import Image

def encrypt_image(image_path):
    """
    Encrypts an image by swapping the pixel values of each pair of pixels.
    
    Args:
        image_path (str): The path to the image file.
    
    Returns:
        None
    """
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB mode
        img = img.convert('RGB')
        
        # Get the pixel data
        pixels = img.load()
        
        # Get the dimensions of the image
        width, height = img.size
        
        # Swap the pixel values of each pair of pixels
        for x in range(0, width, 2):
            for y in range(height):
                # Check if we're not at the last column
                if x + 1 < width:
                    # Swap the pixel values
                    pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]
        
        # Save the encrypted image
        img.save('encrypted_image.png')

def decrypt_image(image_path):
    """
    Decrypts an image by swapping the pixel values of each pair of pixels.
    
    Args:
        image_path (str): The path to the image file.
    
    Returns:
        None
    """
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB mode
        img = img.convert('RGB')
        
        # Get the pixel data
        pixels = img.load()
        
        # Get the dimensions of the image
        width, height = img.size
        
        # Swap the pixel values of each pair of pixels
        for x in range(0, width, 2):
            for y in range(height):
                # Check if we're not at the last column
                if x + 1 < width:
                    # Swap the pixel values
                    pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]
        
        # Save the decrypted image
        img.save('decrypted_image.png')

def main():
    while True:
        print("Image Encryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            image_path = input("Enter the path to the image file: ")
            encrypt_image(image_path)
            print("Image encrypted successfully!")
        elif choice == '2':
            image_path = input("Enter the path to the encrypted image file: ")
            decrypt_image(image_path)
            print("Image decrypted successfully!")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
