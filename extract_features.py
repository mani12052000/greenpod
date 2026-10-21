from pathlib import Path
import csv
import numpy as np
from PIL import Image

BASE_DIR = Path(__file__).parent
DATASET_DIR = BASE_DIR / "dataset"
OUTPUT_FILE = BASE_DIR / "image_features.csv"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def extract_features(image_path):
    with Image.open(image_path) as image:
        image = image.convert("RGB").resize((128, 128))
        pixels = np.asarray(image, dtype=np.float32) / 255.0

    # Mean RGB color
    mean_rgb = pixels.mean(axis=(0, 1))

    # Mean HSV color
    hsv = np.asarray(
        Image.fromarray((pixels * 255).astype("uint8")).convert("HSV"),
        dtype=np.float32
    ) / 255.0
    mean_hsv = hsv.mean(axis=(0, 1))

    # Simple texture features: average and standard deviation
    gray = (
        0.299 * pixels[:, :, 0]
        + 0.587 * pixels[:, :, 1]
        + 0.114 * pixels[:, :, 2]
    )
    gray_mean = float(gray.mean())
    gray_std = float(gray.std())

    return [
        *mean_rgb.tolist(),
        *mean_hsv.tolist(),
        gray_mean,
        gray_std
    ]


rows = []

for split in ("train", "test"):
    folder = DATASET_DIR / split

    if not folder.exists():
        print("Missing folder:", folder)
        continue

    images = [
        path for path in folder.rglob("*")
        if path.is_file()
        and path.suffix.lower() in IMAGE_EXTENSIONS
    ]

    print(split, "images:", len(images))

    for path in images:
        try:
            features = extract_features(path)
            rows.append([
                split,
                str(path.relative_to(DATASET_DIR)),
                *features
            ])
        except Exception as error:
            print("Skipped:", path.name, error)

headers = [
    "split", "image_path",
    "mean_r", "mean_g", "mean_b",
    "mean_h", "mean_s", "mean_v",
    "gray_mean", "gray_std"
]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("\nFeature extraction complete.")
print("Images processed:", len(rows))
print("Saved to:", OUTPUT_FILE)

