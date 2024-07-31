import os
import pymupdf
import pathlib
import logging
from datetime import datetime


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            t = dt.strftime("%Y-%m-%d %H:%M:%S")
            s = f"{t}.{dt.microsecond:06d}"
        return s


def set_logger(log_path):
    global logger
    print("\nInitializing log service...")
    try:

        log_folder = log_path
        print("logs will be saved at: {}\n".format(str(log_folder)))
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_file = os.path.join(
            log_folder,
            f'auto_vergara_{datetime.now().strftime("%Y-%m-%d_%Hh:%Mm:%Ss:%f")}.log',
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        formatter = CustomFormatter(
            "%(asctime)s %(levelname)s:%(message)s", "%Y-%m-%d %H:%M:%S.%f"
        )

        # create a console handler for logging
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # create a file handler for logging
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.info("Logger service initialized sucessfully.")
        return logger
    except Exception as e:
        print("Logging Initialization failed.")
        print(str(e))


def flags_decomposer(flags):
    """Make font flags human readable."""
    l = []
    if flags & 2**0:
        l.append("superscript")
    if flags & 2**1:
        l.append("italic")
    if flags & 2**2:
        l.append("serifed")
    else:
        l.append("sans")
    if flags & 2**3:
        l.append("monospaced")
    else:
        l.append("proportional")
    if flags & 2**4:
        l.append("bold")
    return ", ".join(l)


def extract_text(pdf_file):
    logger.info("Extracting text: {}".format(str(pdf_file)))
    sentences = {}
    english_styles_list = ["bold", "italic"]
    english_phrase_counter = 0
    try:
        with pymupdf.open(pdf_file) as doc:
            extracted_text = {}
            for page in doc:
                text_blocks = page.get_text("dict", flags=pymupdf.TEXTFLAGS_TEXT)[
                    "blocks"
                ]
                for block in text_blocks:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span.get("text")
                            style = flags_decomposer(span["flags"])
                            #print(span)
                            if text == ' ':
                               print("!------------------------!")
                            else:
                                print("FRASE: " + text + "| ")
                           

        logger.info("Text extracted. Closing file...")
        return extracted_text
    except Exception as e:
        logger.error("Error {} during text extraction.".format( str(e)))


def write_file(text, folder):
    logger.info("Starting writing process...")

    try:
        logger.info("Files stored.")
        pass
    except Exception as e:
        logger.error("Error {} during file writing.".format(str(e)))
    # save txt file in a direcotry using the same file name
    # write as a binary file to support non-ASCII characters
    # pathlib.Path(fname + ".txt").write_bytes(text.encode())


def concatenate_files(destination_folder):
    logger.info("Starting concat process...")
    try:
        # concatenate all the txt files into one in order to effectvely import into anki
        for file in destination_folder:
            if file.endswith(".txt"):
                # concatenar
                pass
        logger.info("concat successful.")

    except Exception as e:
        logger.error("Error {} during file concat.".format(str(e)))


def list_all_pdfs(pdf_folder):
    logger.info("Listing all pdf files...")
    try:
        list_pdfs = []
        logger.info("Searching for PDFs inside: {}".format(pdf_folder))
        # list all pdf files inside the pdf folder, return
        for root, dirs, filenames in os.walk(pdf_folder):
            for filename in filenames:
                if str(filename).endswith(".pdf"):
                    list_pdfs.append(os.path.join(root, filename))
                    logger.info("{} found!".format(str(filename)))

        message = "{} pdf files found in folder.".format(str(len(list_pdfs)))
        logger.info(message)
        return list_pdfs
    except Exception as e:
        logger.error("Error {} while listing pdf files.".format(str(e)))


def main():
    try:
        cwd = os.getcwd()
        log_folder = f"{cwd}/logs"
        set_logger(log_folder)

        pdf_folder = f"{cwd}/data/"
        destination_folder = f"{cwd}/txt"

        pdf_list = list_all_pdfs(pdf_folder)
        for file in pdf_list:
            text = extract_text(file)
            #write_file(text, destination_folder)
        #concatenate_files(destination_folder)
        return 0
    except Exception as e:
        print(str(e))
        return 1


if __name__ == "__main__":
    main()
