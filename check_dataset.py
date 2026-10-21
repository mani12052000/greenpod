from pathlib import Path

dataset_dir = Path(__file__).parent / "dataset"

for split in ["train", "test"]:
    folder = dataset_dir / split

    print("\n---", split.upper(), "---")

    if not folder.exists():
        print("Folder not found:", folder)
        continue

    for item in sorted(folder.iterdir()):
        if item.is_dir():
            image_count = sum(
                1 for p in item.rglob("*")
                if p.is_file()
                and p.suffix.lower() in {
                    ".jpg", ".jpeg", ".png", ".bmp", ".webp"
                }
            )
            print(f"{item.name}: {image_count} images")
