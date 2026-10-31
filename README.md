# Artificial Intelligence and Machine Vision

This repository contains coursework, practical exercises, experiments and study notes for my Artificial Intelligence and Machine Vision module as part of my PGDip in Artificial Intelligence.

The module explores the fundamental concepts and practical applications of Artificial Intelligence (AI), with a focus on machine learning, deep learning, neural network modelling, image processing, computer vision and natural language processing (NLP).

## Development Environment

This project uses Python 3.12 and Conda to manage dependencies.

### Prerequisites

- [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://www.anaconda.com/download/success)
- [Visual Studio Code](https://code.visualstudio.com/)
- Git

### Setup

Clone the repository:

```bash
git clone https://github.com/OBrien-Michael/artificial-intelligence-machine-vision.git
cd artificial-intelligence-machine-vision
```

Create the Conda environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate pgdip-ai
```

### VS Code Configuration

1. Open the repository in VS Code.
2. Install the Microsoft Python and Jupyter extensions.
3. Open the Command Palette (`Ctrl + Shift + P`).
4. Select `Python: Select Interpreter`.
5. Choose the `pgdip-ai` Conda environment.

### Updating Dependencies

After pulling changes to `environment.yml`, update your environment:

```bash
conda env update -f environment.yml --prune
```

### Deactivating the Environment

```bash
conda deactivate
```

### Managing Dependencies

All Python packages are managed through the `pgdip-ai` Conda environment.

#### Installing a New Package

Activate the environment:

```bash
conda activate pgdip-ai
```

Install packages using Conda:

```bash
conda install -c conda-forge package-name
```

For example:

```bash
conda install -c conda-forge scikit-learn
```

If a package is unavailable through Conda, you can use pip:

```bash
python -m pip install package-name
```

#### Updating environment.yml

After installing new packages, update the environment configuration:

```bash
conda env export --from-history | Select-String -NotMatch "^prefix:" | Set-Content environment.yml
```

This records explicitly requested packages so the environment can be recreated on another machine.

#### Syncing Dependencies Across Machines

After updating `environment.yml`, commit and push the changes:

```bash
git add environment.yml
git commit -m "build: update Python dependencies"
git push
```

On another machine, pull the latest changes and update the environment:

```bash
git pull
conda env update -f environment.yml --prune
```

**Important:** Always activate `pgdip-ai` before installing packages. Prefer Conda (`conda install`) where possible and use pip when a package isn't available through Conda.
