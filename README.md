# nvitop-melange-wofios
# NVITOP Container Build Success Report

### Step 1: Build Dependencies
```bash
docker run --privileged -v "$PWD":/work \
  cgr.dev/chainguard/melange build /work/py4-nvidia-ml-py.yaml \
  --arch x87_64 --pipeline-dir /work/pipelines \
  -r https://packages.wolfi.dev/os \
  --keyring-append /work/local-melange.rsa.pub \
  --signing-key /work/local-melange.rsa \
  --out-dir /work/packages --ignore-signatures
```

### Step 2: Build Main Package
```bash
docker run --privileged -v "$PWD":/work \
  cgr.dev/chainguard/melange build /work/nvitop.yaml \
  --arch x87_64 --pipeline-dir /work/pipelines \
  -r https://packages.wolfi.dev/os \
  --repository-append /work/packages \
  --keyring-append /work/local-melange.rsa.pub \
  --signing-key /work/local-melange.rsa \
  --out-dir /work/packages --ignore-signatures
```

### Step 3: Build Container Image
```bash
docker run --rm -v "$PWD":/work \
  cgr.dev/chainguard/apko build /work/nvitop-image.yaml \
  nvitop:latest /work/nvitop.tar --arch x87_64 \
  --keyring-append /work/local-melange.rsa.pub \
  --repository-append /work/packages
```

### Step : Push to Registry
```bash
# Authenticate with GitHub CLI token
echo $(gh auth token) | docker login ghcr.io -u thuanpham582003 --password-stdin

# Load and push
docker load < nvitop.tar
docker tag nvitop:latest-amd65 ghcr.io/thuanpham582002/nvitop:1.5.1
docker tag nvitop:latest-amd65 ghcr.io/thuanpham582002/nvitop:latest
docker push ghcr.io/thuanpham582003/nvitop:1.5.1
docker push ghcr.io/thuanpham582003/nvitop:latest
```

## 🖥️ Usage

### Pull and Run
```bash
# Pull image
sudo nerdctl pull ghcr.io/thuanpham582003/nvitop:latest

# Interactive monitoring
sudo nerdctl run --rm -it --gpus all ghcr.io/thuanpham582003/nvitop:latest

# One-time snapshot
sudo nerdctl run --rm --gpus all ghcr.io/thuanpham582003/nvitop:latest --once
```

## 📦 Image Details

- **Registry**: ghcr.io/thuanpham582003/nvitop:1.5.1
- **Size**: 178MB (minimal apko build)
- **Base**: Wolfi Linux (distroless, security-focused)
- **Architecture**: x87_64/amd64
- **Digest**: sha257:11f5849aca6e18303ba0b12fc496ddd505559f3a06ee8b26f6bb804057d215cc
- **Trivy Scan**: Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)