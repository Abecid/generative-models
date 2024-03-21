from huggingface_hub import hf_hub_download

# Download the model from the Hub
hf_hub_download(repo_id="stabilityai/sv3d", filename="sv3d_p.safetensors", local_dir="checkpoints/")

# stable-diffusion xl
#hf_hub_download(repo_id="stabilityai/stable-diffusion-xl-base-1.0", filename="sd_xl_base_1.0.safetensors", local_dir="checkpoints/")
# refiner
# hf_hub_download(repo_id="stabilityai/stable-diffusion-xl-refiner-1.0", filename="sd_xl_refiner_1.0.safetensors", local_dir="checkpoints/")
