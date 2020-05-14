from MirrorFactory import MirrorFactory

import spacy
nlp = spacy.load("es_core_news_md")

from transformers import AutoTokenizer, BertModel
tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
transformer = BertModel.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")

article_diff = ["el", "la"]
articles = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas']
noun_diff = ["maestro", "maestra"]
hardcoded = {"nosotros": "nosotras"}

mf = MirrorFactory(spacy=nlp, transformer=transformer, tokenizer=tokenizer,
                    noun_diff=noun_diff, article_diff=article_diff,
                    articles=articles, names_file="./nam_dict.txt")
print(mf.flip_sentence('El padre de Ana es un profesor de las artes.'))
