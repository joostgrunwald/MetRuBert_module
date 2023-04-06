# MetRuBert_module
This contains only the python MetRuBert module to use externally

# Running the model
.1 clone the model (https://github.com/joostgrunwald/MetRuBert_module.git) \\
.2 download the actual model from huggingface's transformers (https://huggingface.co/joostgrunwald/MetRuBert/blob/main/pytorch_model.bin)
.3 put the model inside MetRuBert_module/MetRobert_rel/saves/roberta-base/3_20220822-1301/
.4 install the requirement using pip install -r requirements.txt
.5 you can now run the model by doing python3 MetRuBert.py

# The input
MetRuBert.py will ask you for the location of a dev.tsv file, these are the input files our model uses, an example was added in this repo as well.
