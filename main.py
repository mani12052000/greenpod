from pathlib import Path
from PIL import Image

DATASET_PATH = Path(__file__).parent / "dataset"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

for split in ["train", "test"]:
    folder = DATASET_PATH / split

    print(f"\n--- {split.upper()} ---")

    if not folder.exists():
        print("Folder not found:", folder)
        continue

    images = [
        path for path in folder.rglob("*")
        if path.is_file()
        and path.suffix.lower() in IMAGE_EXTENSIONS
    ]

    print("Total images:", len(images))

    for path in images[:10]:
        print("Image:", path.name)

    if images:
        try:
            with Image.open(images[0]) as image:
                print("Image size:", image.size)
                print("Image format:", image.format)
        except Exception as error:
            print("Image error:", error)