# TUTORIAL

## Installation

To install the Fiesta Map Generator, clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/mariosanlina-ai/fiesta-map-generator.git

# Change directory to the project folder
cd fiesta-map-generator

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

After installation, you can generate maps using the following command:

```bash
python generate_map.py --config config.yaml
```

Make sure to adjust the `config.yaml` file according to your needs.

## Map Generation

The map generation process can be customized through different parameters in the configuration file. Here's an example configuration:

```yaml
map_size: [100, 100]
num_features: 10
features:
  - type: river
    width: 1
  - type: forest
    density: 0.5
```

## ML Model Training

To train the machine learning model on your generated maps, you can execute:

```bash
python train_model.py --data datasets/maps --model output/model.h5
```

Ensure that you have a dataset of generated maps in the specified directory.

## Practical Examples

Here are a few examples of how to use the map generator:

### Example 1: Generating a Simple Map

Run the following command to generate a simple map:

```bash
python generate_map.py --config simple_config.yaml
```

### Example 2: Training with Custom Data

To train the model with your custom dataset, use:

```bash
python train_model.py --data your_dataset_dir --model output/custom_model.h5
```
```
