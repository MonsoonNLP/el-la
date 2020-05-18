import csv
ovfile = open('./train_output.csv', 'w')
wrt = csv.writer(ovfile)
wrt.writerow(['index', 'x', 'y'])

from MirrorFactory import MirrorFactory

import spacy
nlp = spacy.load("es_core_news_md")

from transformers import AutoTokenizer, BertModel
tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
transformer = BertModel.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")

article_diff = ["el", "la"]
articles = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas']
noun_diff = ["hombre", "mujer"] # ["maestro", "maestra"]
hardcoded = {"nosotros": "nosotras"}

mf = MirrorFactory(spacy=nlp, transformer=transformer, tokenizer=tokenizer,
                    noun_diff=noun_diff, article_diff=article_diff,
                    articles=articles, names_file="./nam_dict.txt")

with open('./summary_df.csv', 'r') as csvfile:
    rdr = csv.reader(csvfile)
    headers = None
    index = 0
    for line in rdr:
        if headers == None:
            headers = line
        else:
            mirror_txt = ''
            review = line[1]
            sentences = review.split('.')
            for sentence in sentences:
                mirror_txt += mf.flip_sentence(sentence.strip()) + '. '
            line[1] = mirror_txt
            wrt.writerow(line)
            print(index)
            index += 1
