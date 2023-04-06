from MetRobert_rel import main_dutch
# import our own output prettifier
import MetRubert_parser as outputgen
import os

# import used for docx generation
from docx.shared import Inches
from docx import Document
from docx.enum.text import WD_COLOR_INDEX
inputfile = "dev.tsv"
main_dutch.main(inputfile)

# settings and modules
# whether to include this pos tag
noun = "yes"
verb = "yes"
adj = "yes"
adv = "yes"
pron = "yes"
det = "no"
num = "no"
# wheter to include softmax data or not
softmax = "yes"

print("What mode would you like to use? Type tok for tokenised input, txt for simple text input and dev for dev.tsv input.")
mode = input("Please enter your choice: ")
while mode != "tok" and mode != "txt" and mode != "dev":
    mode = input("Invalid choice, try again: ")


def wordfunction(outputdir):

    # Create a document, add heading
    document = Document()
    document.add_heading('MetRuBert Output', 0)

    ######################
    # SENTENCE RETRIEVAL #
    ######################

    previous_sentence = None
    pos_list = []
    met_list = []

    sentences = []

    with open(os.path.join(outputdir, 'output.tsv'), mode='r', encoding='utf-8') as output:
        for line in output:
            if line[:5] != "index":
                splitted = line.split("\t")

                sentence = splitted[1]

                if previous_sentence == None or sentence == previous_sentence:
                    # append pos tag
                    pos = splitted[2]
                    index = splitted[3]
                    pos_list.append([index, pos])

                    # append metaphor
                    met = splitted[5]
                    if met.find("1") != -1 and met.find("-1") == -1:
                        met_list.append(index)
                elif sentence != previous_sentence:
                    split_sen = previous_sentence.split()
                    p = document.add_paragraph('')

                    for i in range(len(split_sen)):
                        word = split_sen[i]
                        found = False
                        if f'{str(i)} ' in met_list:
                            for pos in pos_list:
                                # print(pos)
                                if pos[0] == f'{str(i)} ':
                                    found = True
                                    if pos[1] == "NOUN":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.YELLOW
                                        font.bold = True
                                    elif pos[1] == "VERB":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.BRIGHT_GREEN
                                        font.bold = True
                                    elif pos[1] == "DET":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.GRAY_25
                                        font.bold = True
                                    elif pos[1] == "ADV":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.PINK
                                        font.bold = True
                                    elif pos[1] == "ADJ":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.RED
                                        font.bold = True
                                    elif pos[1] == "PRON":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.TURQUOISE
                                        font.bold = True
                                    else:
                                        p.add_run(word).bold = True
                            if found == False:
                                p.add_run(word).bold = True
                        else:
                            for pos in pos_list:
                                # print(pos)
                                if pos[0] == f'{str(i)} ':
                                    found = True
                                    if pos[1] == "NOUN":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.YELLOW
                                    elif pos[1] == "VERB":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.BRIGHT_GREEN
                                    elif pos[1] == "DET":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.GRAY_25
                                    elif pos[1] == "ADV":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.PINK
                                    elif pos[1] == "ADJ":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.RED
                                    elif pos[1] == "PRON":
                                        font = p.add_run(word).font
                                        font.highlight_color = WD_COLOR_INDEX.TURQUOISE
                                    else:
                                        print(word)
                                        print(pos[1])
                                        print(pos[0])
                                        print(pos_list)

                                        p.add_run(word)
                            if found == False:
                                # print(word)
                                # print(i)
                                # print(pos_list)
                                # Missing elements in list
                                p.add_run(word)

                        p.add_run(' ')
                    sentences.append(previous_sentence)

                    pos_list = []
                    met_list = []

                previous_sentence = sentence

    document.add_page_break()
    document.save(outputdir + '/' + 'MetRubert_runx.docx')


# use parameter values to create a parameter list
pos_list = []
if str(noun) == "no":
    pos_list.append("noun")
if str(verb) == "no":
    pos_list.append("verb")
if str(adj) == "no":
    pos_list.append("adj")
if str(adv) == "no":
    pos_list.append("adv")
if str(pron) == "no":
    pos_list.append("pron")
if str(det) == "no":
    pos_list.append("det")
if str(num) == "no":
    pos_list.append("num")

if mode == "dev":
    dev_path = input("Please enter the path of the dev.tsv file")
elif mode == "tok":
    tok_folder = input(
        "Please enter the path of the folder containing the tok files")
    # TODO: implement tok file usage and retrieval


# TODO: use output folder (replace first none with outputdir)
outputgen.main(None, pos_list, False, dev_path, softmax)
outputdir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
if True:
    # cleanup
    for file in os.listdir(outputdir):
        if file.endswith("dev_float.txt"):  # and str(unres) == "no":
            try:
                os.remove(outputdir + "/" + file)
            except:
                print("Error while deleting tok file : ", file)
        elif file.endswith("dev_soft.txt"):  # and str(sof) == "no":
            try:
                os.remove(outputdir + "/" + file)
            except:
                print("Error while deleting tok file : ", file)
        elif file.endswith("_dev2.txt") or file.endswith("dev2.tsv") or file.endswith("soft2.txt"):
            try:
                os.remove(outputdir + "/" + file)
            except:
                print("Error while deleting tok file : ", file)

    # Generate word output
    wordfunction(outputdir=outputdir)
