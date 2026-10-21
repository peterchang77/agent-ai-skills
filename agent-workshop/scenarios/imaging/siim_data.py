"""Download and cache the SIIM-ACR pneumothorax 'siim_small' subset (250 DICOM files, ~33 MB)."""
import hashlib
import tarfile
import urllib.request
from pathlib import Path

URL = "https://s3.amazonaws.com/fast-ai-imagelocal/siim_small.tgz"
CACHE = Path(__file__).parent / ".cache"


def fetch_siim_small() -> Path:
    """Return the folder containing train/{Pneumothorax,No Pneumothorax}/*.dcm, downloading if needed."""
    CACHE.mkdir(exist_ok=True)
    root = CACHE / "siim_small"
    if not root.exists():
        tgz = CACHE / "siim_small.tgz"
        if not tgz.exists():
            urllib.request.urlretrieve(URL, tgz)
        with tarfile.open(tgz) as t:
            t.extractall(CACHE, filter="data")
    return root / "train"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
