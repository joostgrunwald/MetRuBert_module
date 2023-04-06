# MetRuBert_module
This contains only the python MetRuBert module to use externally

# Running the model
.1 clone this github repository (https://github.com/joostgrunwald/MetRuBert_module.git) <br>
.2 download the actual model from huggingface's transformers (https://huggingface.co/joostgrunwald/MetRuBert/blob/main/pytorch_model.bin) <br>
.3 put the model inside MetRuBert_module/MetRobert_rel/saves/roberta-base/3_20220822-1301/ <br>
.4 install the requirement using pip install -r requirements.txt <br>
.5 you can now run the model by doing python3 MetRuBert.py <br>

# The input
MetRuBert.py will ask you for the location of a dev.tsv file, these are the input files our model uses, an example was added in this repo as well.

# Virtual env
it might be usefull to create a virtual environment <br>
you do this by doing python3 -venv {name of virtual env} <br>
you can then load the venv by doing source {name of virtual env}/bin/activate (do this from the folder the virtual env is in)
