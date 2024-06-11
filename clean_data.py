import pandas as pd
from hazm import word_tokenizer, Lemmatizer
from hazm import Normalizer
import string


def normalize(data, text_col='Text'):
    normalizer = Normalizer(correct_spacing=True, remove_diacritics=True,
                            remove_specials_chars=True, decrease_repeated_chars=False,
                            persian_style=False, persian_numbers=True,
                            unicodes_replacement=True, seperate_mi=True)
    normalized_texts = []
    for text in data[text_col]:
        normalized_texts.append(normalizer.normalize(text))

    for i in range(len(normalized_texts)):
        normalized_texts[i] = normalized_texts[i].replace('\u200c', ' ')
        normalized_texts[i] = normalized_texts[i].replace('\u200e', '')
        normalized_texts[i] = normalized_texts[i].replace('\u200f', '')

    return normalized_texts


def lemmatize(data):
    lemmatizer = Lemmatizer()

    lemmatized = []
    for text in data:
        temp = []
        for word in text:
            temp.append(lemmatizer.lemmatize(word))
        lemmatized.append(temp)
    return lemmatized


def remove_redundnat(data):
    redundant = ['،', '؟', '؛', '»', '«', '!؟', '–','،','.']
    for s in string.punctuation:
        redundant.append(s)
    for char in range(ord('a'), ord('z') + 1):
        redundant.append(chr(char))
    for char in range(ord('A'), ord('Z') + 1):
        redundant.append(chr(char))
    redundant.append('NUM')

    for i in range(10):
        redundant.append(str(i))

    removed = []
    for text in data:
        temp = []
        for word in text:
            if word not in redundant:
                temp.append(word)
        removed.append(temp)

    return removed


def tokenize(data):
    tokenizer = word_tokenizer.WordTokenizer(join_verb_parts=True, join_abbreviations=True,
                                             separate_emoji=False, replace_links=False,
                                             replace_ids=False, replace_emails=False,
                                             replace_numbers=True, replace_hashtags=False)
    tokenized_texts = []

    for text in data:
        tokenized_texts.append(tokenizer.tokenize(text))

    return tokenized_texts


def remove_stopword(data):
    prepositional = ['به', 'که', 'در', 'با', 'از',
                     'بر', 'اثر', 'آن', 'ان', 'این', 'چنین', 'برای', 'طور', 'اینطور', 'جز', 'بنا', 'همین', 'هیج', 'بعد',
                     'سایر', 'هم', 'چه'
                                   'طی', 'های', 'که', 'را', 'نیز', 'نه', 'تا', 'باتوجه', 'یا', 'و', 'ولی', 'اگر',
                     'بلکه',
                   'است'  'ای', 'هر', 'اما']

    pronoun = ['من', 'تو', 'او', 'شما', 'ایشان', 'آن\u200cها', 'ما', 'وی']

    stopwords = prepositional + pronoun
    other = ['', 'های', 'ها','بررسی','تاثیر','تحلیل','اثرات','تأثیرپذیری','آثار','ایران', 'اقتصاد', 'اقتصادی']

    removed = []

    for text in data:
        temp = []
        for word in text:
            if word not in stopwords and word not in other and '#' not in word:
                temp.append(word)
        removed.append(temp)

    return removed


df = pd.read_csv(r'modares_papers\articles_modares.csv', encoding='utf-8')
normalized = normalize(df, 'abstract')
tokenized = tokenize(normalized)
lemmatized = lemmatize(tokenized)
removed_stopwords = remove_stopword(tokenized)
removed_redundants = remove_redundnat(removed_stopwords)
clean_df = pd.DataFrame({
    'abstract': removed_redundants
})
clean_df.to_csv(r'cleaned\cleaned_abstract.csv', encoding='utf-8')
