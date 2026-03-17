"""Download ISOT Fake News Dataset from University of Victoria."""
import urllib.request, os, zipfile
from pathlib import Path

ISOT_URLS = {
    "True.csv":  "https://uvic.ca/files/True.csv",
    "Fake.csv":  "https://uvic.ca/files/Fake.csv",
}
# Note: actual UVic URLs change. Use Kaggle CLI if available.

def download_isot():
    Path("data/raw/isot").mkdir(parents=True, exist_ok=True)
    # Try Kaggle first (requires kaggle.json credentials)
    try:
        import subprocess
        result = subprocess.run([
            "kaggle", "datasets", "download",
            "clmentbisaillon/fake-and-real-news-dataset",
            "-p", "data/raw/isot", "--unzip"
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("ISOT downloaded via Kaggle CLI")
            return True
    except Exception:
        pass
    print("Kaggle not available. Download manually:")
    print("  kaggle datasets download clmentbisaillon/fake-and-real-news-dataset")
    print("  OR: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset")
    return False

if __name__ == "__main__":
    download_isot()
