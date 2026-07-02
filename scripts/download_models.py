import os
import zipfile
import gdown

MODEL_URL = "https://drive.google.com/uc?id=1XdT4rhWCOhd0yWKcJr6aGKnMC62Juh09"

ZIP_NAME = "models.zip"
OUTPUT_DIR = "models"


def download_models():

    if os.path.exists(OUTPUT_DIR) and any(f.endswith(".pt") for f in os.listdir(OUTPUT_DIR)):
        print("Los modelos ya están descargados.")
        return

    print("Descargando modelos...")

    gdown.download(MODEL_URL, ZIP_NAME, quiet=False)

    print("Descomprimiendo modelos...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with zipfile.ZipFile(ZIP_NAME, "r") as zip_ref:
        zip_ref.extractall(OUTPUT_DIR)

    os.remove(ZIP_NAME)

    print(f"Modelos listos en '{OUTPUT_DIR}'")


if __name__ == "__main__":
    download_models()
