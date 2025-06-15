"""
Example of how to use the Power Lora Loader with the API format

This script demonstrates two ways to use the Power Lora Loader:
1. Using the string format for simple cases (just the lora path)
2. Using the object format for more control (with on/off toggle and strength values)
"""

# Example API workflow using the Power Lora Loader
# Note: This is a simplified example and not a complete working script

# Method 1: Simple string format (default strength 1.0)
workflow = {
    "3": {
        "inputs": {
            "model": ["1", 0],  # Assuming node 1 outputs a model
            "clip": ["2", 0],   # Assuming node 2 outputs a clip
            "lora_1": "my_lora_file.safetensors",  # Simple string format with default strength 1.0
            "lora_2": "another_lora.safetensors"   # Another lora with default strength
        },
        "class_type": "RgthreePowerLoraLoader"
    }
}

# Method 2: Object format with more control
workflow_detailed = {
    "3": {
        "inputs": {
            "model": ["1", 0],  # Assuming node 1 outputs a model
            "clip": ["2", 0],   # Assuming node 2 outputs a clip
            "lora_1": {
                "on": True,
                "lora": "my_lora_file.safetensors",
                "strength": 0.8,           # Model strength
                "strengthTwo": 0.5         # Clip strength (optional)
            },
            "lora_2": {
                "on": True,
                "lora": "another_lora.safetensors",
                "strength": 0.7            # When strengthTwo is omitted, strength is used for both
            }
        },
        "class_type": "RgthreePowerLoraLoader"
    }
}

# You can also disable specific loras without removing them from the workflow
workflow_with_disabled = {
    "3": {
        "inputs": {
            "model": ["1", 0],
            "clip": ["2", 0],
            "lora_1": {
                "on": True,                # This lora is enabled
                "lora": "my_lora_file.safetensors",
                "strength": 0.8
            },
            "lora_2": {
                "on": False,               # This lora is disabled
                "lora": "another_lora.safetensors",
                "strength": 0.7
            }
        },
        "class_type": "RgthreePowerLoraLoader"
    }
}

print("These examples show how to structure your API calls to use the Power Lora Loader")
print("See the code comments for more details on each approach") 