import torch

class PromptPassthrough:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "negative_prompt": ("STRING", {"multiline": True}),
                "cfg": ("FLOAT", {"default": 7.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "FLOAT", "INT", "FLOAT")
    RETURN_NAMES = ("prompt", "negative_prompt", "cfg", "steps", "denoise")
    FUNCTION = "passthrough"
    CATEGORY = "Shichen"

    def passthrough(self, prompt, negative_prompt, cfg, steps, denoise):
        return (prompt, negative_prompt, cfg, steps, denoise)