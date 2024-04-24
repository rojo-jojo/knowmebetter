from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
model_file = "mistral-7b-instruct-v0.2.Q4_K_S.gguf"
gpu_on = True
llm = AutoModelForCausalLM.from_pretrained(model_name, model_file=model_file, model_type="mistral", gpu_layers=-1 if gpu_on else 0)

# print(llm("AI is going to"))
