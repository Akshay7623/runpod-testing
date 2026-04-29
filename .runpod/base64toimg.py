import json
import base64
import os

def decode_json_file(file_path, output_dir="decoded_images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        images = data.get("output", {}).get("images", [])
        
        if not images:
            print("No images found in the JSON file.")
            return

        print(f"Found {len(images)} images. Starting decode...")

        for i, img_info in enumerate(images):
            base64_data = img_info.get("data")
            original_name = img_info.get("filename", "output.png")
            
            name_root, extension = os.path.splitext(original_name)
            filename = f"{i}_{name_root}{extension}"
            
            if not base64_data:
                continue
            
            if "," in base64_data:
                base64_data = base64_data.split(",")[1]

            img_bytes = base64.b64decode(base64_data)
            save_path = os.path.join(output_dir, filename)

            with open(save_path, "wb") as img_file:
                img_file.write(img_bytes)
            
            print(f"✅ Saved: {save_path}")

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Set your path here ---
json_file_path = "sample.json" 
decode_json_file(json_file_path)