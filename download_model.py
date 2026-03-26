"""
Script untuk download model dari Hugging Face Hub
"""
from huggingface_hub import hf_hub_download
import os

# Hugging Face repo ID
REPO_ID = "dz4ic7/amazon-sales-predictor"

def download_model():
    print("=" * 50)
    print("Amazon Sales Predictor - Download Model")
    print("=" * 50)
    
    # Cek apakah model sudah ada
    if os.path.exists("model.joblib"):
        print("\n✅ Model sudah ada di folder ini!")
        print("Hapus file 'model.joblib' jika ingin download ulang.")
        return
    
    print(f"\n📥 Downloading model dari Hugging Face...")
    print(f"   Repo: {REPO_ID}")
    
    try:
        # Download model
        model_path = hf_hub_download(
            repo_id=REPO_ID,
            filename="model.joblib",
            local_dir=".",
            force_download=False  # Use cache if available
        )
        
        print(f"\n✅ Download berhasil!")
        print(f"   Model disimpan di: {os.path.abspath(model_path)}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPastikan:")
        print(f"1. REPO_ID sudah diubah di file download_model.py")
        print("2. Model sudah diupload ke Hugging Face")
        print("3. Koneksi internet stabil")
        print("\nAtau download manual dari:")
        print(f"   https://huggingface.co/{REPO_ID}/resolve/main/model.joblib")

if __name__ == "__main__":
    download_model()
