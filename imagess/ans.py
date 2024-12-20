from pygoogle_image import image as pi

def download_images(query, num_images):
    # Use the download function with only query and limit as inputs
    pi.download(query, limit=num_images)  # We don't need output_dir here

# Example usage
if __name__ == "__main__":
    search_query = input("Enter search keyword: ")
    num_images = int(input("Enter number of images to download: "))

    download_images(search_query, num_images)
