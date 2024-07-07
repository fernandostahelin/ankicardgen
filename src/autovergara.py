import os
import pymupdf
import pathlib

fname = "/Users/fernandostahelin/Applications/AutoVergara/data/I'll Have You Know - O que significa esta expressão.pdf"

def flags_decomposer(flags):
    """Make font flags human readable."""
    l = []
    if flags & 2 ** 0:
        l.append("superscript")
    if flags & 2 ** 1:
        l.append("italic")
    if flags & 2 ** 2:
        l.append("serifed")
    else:
        l.append("sans")
    if flags & 2 ** 3:
        l.append("monospaced")
    else:
        l.append("proportional")
    if flags & 2 ** 4:
        l.append("bold")
    return ", ".join(l)


def extract_text():
    sentences = {}
    english_styles_list = ["bold","italic"]
    with pymupdf.open(fname) as doc:
        for page in doc:
            text_blocks = page.get_text("dict", flags=pymupdf.TEXTFLAGS_TEXT)["blocks"]

            for block in text_blocks:
                for line in block["lines"]:
                # print(line)
                    for span in line["spans"]:
                    #  print("")
                        font_properties = "%s" % (
                            flags_decomposer(span["flags"]),  # readable font flags
                        )
                        for style in english_styles_list:
                            if style not in font_properties:
                                return "not"
                            else:
                                return "\nText: '%s'" % span["text"]  # simple print of text
                                return font_properties


def save_file():
    #save txt file in a direcotry using the same file name
    # write as a binary file to support non-ASCII characters
    #pathlib.Path(fname + ".txt").write_bytes(text.encode())
    pass

def contact_files():
    #concatenate all the txt files into one in order to effectvely import into anki
    for file in file_path:
        if file.endswith(".txt"):
            #concatenas

def list_all_pdfs(file_path):
    list_pdfs = []
    #list all pdf files inside the path, return
    return list_pdfs

def main():
    try:
        for file in list_pdfs:
            extract_text()
            save_file()
        contact_files()
        return 0
    except Exception as e:
        print(str(e))
        return 1
