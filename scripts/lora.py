import os
from typing import List

import numpy as np
import torch
from safetensors.torch import load_file
import onnx
from onnx import numpy_helper
from tqdm import tqdm

def merge_loras(loras: List[str], scales: List[str]) -> dict:
    refit_dict = {}
    # total_files = len(loras)
    lora_names = [os.path.splitext(os.path.basename(lora))[0] for lora in loras] # only output the file name
    for lora, scale, lora_name in zip(loras, scales, lora_names):
        lora_dict = load_file(lora)
        with tqdm(total=len(lora_dict), desc=f" > Loading '{lora_name}' LoRA", mininterval=1) as pbar:
            for k, v in lora_dict.items():
                if k in refit_dict:
                    refit_dict[k] += scale * v
                else:
                    refit_dict[k] = scale * v
                pbar.update(1)
                pbar.refresh()
    print("[TensorRT] LoRA loading completed.")
    return refit_dict


def apply_loras(base_path: str, loras: List[str], scales: List[str]) -> dict:
    refit_dict = merge_loras(loras, scales)
    # apply base model from stable_diffusion_2080ti\models\Unet-onnx\owo_checkpoint.onnx for refit, lora: ['stable_diffusion_2080ti\\models\\Unet-trt\\owo_lora.lora']
    base_name = os.path.basename(base_path)
    lora_names = [os.path.basename(os.path.dirname(lora)) for lora in loras]
    print(f"[TensorRT] apply base model from {base_name} for refit lora: {lora_names}")
    base = onnx.load(base_path)
    onnx_opt_dir = os.path.dirname(base_path)
    def convert_int64(arr):
        if len(arr.shape) == 0:
            return np.array([np.int32(arr)])
        return arr
    total_initializers = sum(1 for initializer in base.graph.initializer if initializer.name in refit_dict)
    with tqdm(total=total_initializers, desc="Updating weights", mininterval=1) as pbar:
        for initializer in base.graph.initializer:
            if initializer.name not in refit_dict:
                continue

            wt = refit_dict[initializer.name]
            initializer_data = numpy_helper.to_array(
                initializer, base_dir=onnx_opt_dir
            ).astype(np.float16)
            delta = torch.tensor(initializer_data).to(wt.device) + wt

            refit_dict[initializer.name] = delta.contiguous()

            pbar.update(1)
            pbar.refresh()
    print("[TensorRT] LoRA apply completed.")
    return refit_dict