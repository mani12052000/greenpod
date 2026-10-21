from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

DATASET_DIR = Path(__file__).parent / "dataset"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

train_dir = DATASET_DIR / "train"

images = [
    path for path in train_dir.rglob("*")
    if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
]

if not images:
    print("No images found. Check your dataset/train folder.")
else:
    sample_images = images[:9]

    fig, axes = plt.subplots(3, 3, figsize=(10, 10))

    for ax, path in zip(axes.flat, sample_images):
        try:
            with Image.open(path) as img:
                ax.imshow(img.convert("RGB"))
            ax.set_title(path.name[:25])
            ax.axis("off")
        except Exception as error:
            ax.set_title("Cannot open image")
            ax.axis("off")
            print(path.name, error)

    # Hide unused spaces if fewer than 9 images exist
    for ax in axes.flat[len(sample_images):]:
        ax.axis("off")

    plt.tight_layout()
    plt.show()
