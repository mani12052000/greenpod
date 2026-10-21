from pathlib import Path
from collections import Counter
from PIL import Image

BASE_DIR = Path(__file__).parent
DATASET_DIR = BASE_DIR / "dataset"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

for split in ("train", "test"):
    folder = DATASET_DIR / split

    print("\n" + "=" * 40)
    print(split.upper())
    print("=" * 40)

    if not folder.exists():
        print("Folder not found:", folder)
        continue

    images = [
        p for p in folder.rglob("*")
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    ]

    print("Total images:", len(images))

    # Count images in each immediate subfolder
    subfolder_counts = Counter(
        p.parent.name for p in images
        if p.parent != folder
    )
    print("Images by containing folder:", dict(subfolder_counts))

    for path in images[:10]:
        try:
            with Image.open(path) as img:
                print(
                    path.relative_to(folder),
                    "| size:", img.size,
                    "| format:", img.format
                )
        except Exception as error:
            print("Cannot read:", path.name, error)

