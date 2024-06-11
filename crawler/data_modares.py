import csv
from xml.dom import minidom
import os

FA_CHARS = ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ', 'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و', 'آ', 'ژ']

issue_files = os.listdir('./Ecor Issues')

articles_file = 'articles_modares.csv'
csv_file = open(articles_file, 'a', newline='', encoding='utf-8')
feature_names = ['title_fa', 'title_en',
                 'abstract_fa', 'abstract_en',
                 'authors',
                 'keywords_fa', 'keywords_en',
                 'issue_year', 'issue_vol', 'issue_no']
writer = csv.DictWriter(csv_file, fieldnames=feature_names)
writer.writeheader()

no_articles = 0
for issue in issue_files:
    print('====================')
    try:
        issue_dom = minidom.parse(f'./Ecor Issues/{issue}')
        print(f'Issue {issue}')
    except:
        print(f'Skip issue {issue}!')
        continue

    issue_year = issue_dom.getElementsByTagName('YEAR')[0].childNodes[0].data
    issue_vol = issue_dom.getElementsByTagName('VOL')[0].childNodes[0].data
    issue_no = issue_dom.getElementsByTagName('NO')[0].childNodes[0].data

    articles = issue_dom.getElementsByTagName('ARTICLE')
    for index, article in enumerate(articles):
        print(f'>>> Article {index + 1} out of {len(articles)}')
        title_fa = article.getElementsByTagName('TitleF')[0].childNodes[0].data
        try:
            title_en = article.getElementsByTagName('TitleE')[0].childNodes[0].data
        except:
            title_en = ''

        abstracts = article.getElementsByTagName('ABSTRACT')
        abstract_fa = None
        abstract_en = None
        for abstract in abstracts:
            lang_id = abstract.getElementsByTagName('Language_ID')[0].childNodes[0].data
            if lang_id == '1':
                abstract_fa = abstract.getElementsByTagName('CONTENT')[0].childNodes[0].data
            elif lang_id == '2':
                abstract_en = abstract.getElementsByTagName('CONTENT')[0].childNodes[0].data

        authors_elements = issue_dom.getElementsByTagName('AUTHOR')
        authors = []
        for author in authors_elements:
            first_name = author.getElementsByTagName('Name')[0].childNodes[0].data
            try:
                middle_name = author.getElementsByTagName('MidName')[0].childNodes[0].data
            except:
                middle_name = ''
            last_name = author.getElementsByTagName('Family')[0].childNodes[0].data
            authors.append(f'{first_name} {middle_name} {last_name}')
        authors = ', '.join(authors)

        keywords_elements = article.getElementsByTagName('KEYWORD')
        keywords_en = []
        keywords_fa = []
        for keyword in keywords_elements:
            keyword = keyword.getElementsByTagName('KeyText')[0].childNodes[0].data
            is_persian = False
            for char in FA_CHARS:
                if char in keyword:
                    is_persian = True
                    break
            if is_persian:
                keywords_fa.append(keyword)
            else:
                keywords_en.append(keyword)
        keywords_en = ', '.join(keywords_en)
        keywords_fa = ', '.join(keywords_fa)
        writer.writerow({
            'title_en': title_en, 'title_fa': title_fa, 'abstract_fa': abstract_fa,
            'abstract_en': abstract_en, 'authors': authors, 'keywords_en': keywords_en,
            'keywords_fa': keywords_fa, 'issue_year': issue_year, 'issue_vol': issue_vol,
            'issue_no': issue_no
        })

        no_articles += 1

print(f'=== Total Extracted Articles: {no_articles}')
