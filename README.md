# el-la

This is an experimental Python script to create mirror sentences (counterfactuals)
where we switch the gender of everyone in a sentence. It's designed to test bias
in Spanish language models (el actor / la actriz), but I'm releasing a more general
script in hopes it can work for French and other languages with grammatical
gender.

The script currently uses BETO (monolingual Spanish BERT) for word embeddings,
and spaCy for grammatical dependencies.

## Dependencies

```bash
pip3 install --upgrade numpy spacy transformers gender-guesser

# download a spaCy model
python3 -m spacy download es_core_news_md

# optional: download substitute names
wget https://github.com/lead-ratings/gender-guesser/blob/master/gender_guesser/data/nam_dict.txt?raw=true
mv nam_dict.txt\?raw\=true nam_dict.txt

# restart notebook runtime
```

## Sample inputs

```python
from MirrorFactory import MirrorFactory

import spacy
nlp = spacy.load("es_core_news_md")

from transformers import AutoTokenizer, BertModel
tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
transformer = BertModel.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")

noun_diff = ["maestro", "maestra"]
mf = MirrorFactory(spacy=nlp, transformer=transformer, tokenizer=tokenizer,
                    noun_diff=noun_diff)
mf.flip_sentence('El padre de Ana es un profesor de las artes.')
> "La madre de Ana es una profesora de los artes ."
```

### Other features

A longer example (including name flipping and an ```article_diff```
  for certain words) is in this repo under ```example_code.py```


**Raw embedding for a word**
Once you've created a MirrorFactory, you can get the raw tensor / embedding / vector:

```mf.embedding_for_word("biblioteca")```

**Closest word**

Pass a word and a tensor diff, and you will get back the closest word to that location
 (by cosine similarity)

```
mf.closest_word("casa", 0)
diff = mf.embedding_for_word("maestro") - mf.embedding_for_word("maestra")
mf.closest_word("médico", -1 * diff)
```

## License

Open source, GPL license
