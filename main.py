from PIL import Image
import argparse
import os.path

def parser_config():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--image', '-i', help='Input file path')
    parser.add_argument('--width', '-w', help='Output file path')
    return parser.parse_args()

def validate_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'The file {file_path} does not exist.')
    
def generate_vesel(output_path):
    with open(output_path, 'w') as file: pass

def resize_image(input_path, output_path, max_width):
    max_width = int(max_width)
    with Image.open(input_path) as img:
        aspect_ratio = img.width / img.height
        if img.width > img.height:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_width
            new_width = int(max_width * aspect_ratio)
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path)

def resize(selected_image, selected_width):
    input_path = "./inputs/" + selected_image
    output_path = "./outputs/" + selected_image
    print('Input Path: ', input_path)
    validate_file_exists(input_path)
    generate_vesel(output_path)
    resize_image(input_path, output_path, selected_width)

if __name__ == '__main__':
    args = parser_config()
    resize(args.image, args.width)