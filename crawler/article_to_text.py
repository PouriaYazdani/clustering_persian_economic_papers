import csv
import os
import warnings

import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings(action='ignore', category=InsecureRequestWarning)
base_dir = './Articles'
base_url = 'https://ecor.modares.ac.ir'
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# index_urls = [
#     'https://ecor.modares.ac.ir/browse.php?sid=18&slc_lang=fa',
#     'https://ecor.modares.ac.ir/browse.php?sid=18&slc_lang=fa&mag_limit_start=5',
#     'https://ecor.modares.ac.ir/browse.php?sid=18&slc_lang=fa&mag_limit_start=10',
#     'https://ecor.modares.ac.ir/browse.php?sid=18&slc_lang=fa&mag_limit_start=15',
# ]
#
# issue_urls = dict()
# print(f'==== Issue URLs extracting...')
#
# for index in index_urls:
#     req = requests.get(index, verify=False)
#     soup = BeautifulSoup(req.text, 'html.parser')
#     issue_divs = soup.find_all('div', class_='yw_text_small persian')
#     for issue in issue_divs:
#         issue_tag = issue.find_all('a')[-1]
#         issue_name = issue_tag.contents[0].strip()
#         issue_url = issue_tag['href']
#         if not os.path.exists(f'{base_dir}/{issue_name}'):
#             os.makedirs(f'{base_dir}/{issue_name}')
#         issue_urls[issue_name] = f'{base_url}/{issue_url}'
#
# print(issue_urls)
# print(f'==== Articles PDF Downloading....')
# article_urls = dict()
#
# for issue_name, issue_url in issue_urls.items():
#     print(f'>>> Issue {issue_name}')
#     req = requests.get(issue_url, verify=False)
#     soup = BeautifulSoup(req.text, 'html.parser')
#     article_divs = soup.find_all('strong')[1:]
#     for index, article in enumerate(article_divs):
#         article_tag = article.find('a')
#         article_name = article_tag.contents[0].strip()
#         article_url = article_tag['href'].replace('html', 'pdf')
#         if not os.path.exists(f'{base_dir}/{issue_name}/{index + 1}'):
#             os.makedirs(f'{base_dir}/{issue_name}/{index + 1}')
#         article_urls[article_name] = f'{base_url}/{article_url}'
#
#         if not os.path.exists(f'{base_dir}/{issue_name}/{index + 1}/{article_name}.pdf'):
#             req = requests.get(f'{base_url}/{article_url}', verify=False)
#             f = open(f'{base_dir}/{issue_name}/{index + 1}/{article_name}.pdf', 'wb')
#             f.write(req.content)
#             f.close()
#             print(f'>> Download {article_name} complete.')
#         else:
#             print(f'>> {article_name} already downloaded.')
#
# print(f'==== Converting PDF to text....')
# # convertapi.api_secret = 'yOooxgmVceZNkXPO'
# # convertapi.api_secret = 'ligBGM9qArepsWh5'
# convertapi.api_secret = 'aV9jfZSEdWLXFuzE'
#
# for root, sub_dirs, files in os.walk(base_dir):
#     if '.DS_Store' in files:
#         files.remove('.DS_Store')
#     if len(files) == 0:
#         continue
#     if len(files) == 1:
#         print(f'Converting {files[0]}...')
#         file_name = f'{root}/{files[0]}'
#         convertapi.convert('txt', {
#             'File': file_name
#         }, from_format='pdf').save_files(file_name.replace('pdf', 'txt'))
#     else:
#         print(f'{files[0]} already converted...')

print(f'==== Preparing CSV File....')

articles_file = 'articles_modares_with_text.csv'
csv_file = open(articles_file, 'a', newline='', encoding='utf-8')
feature_names = ['title',
                 'text',
                 'issue_vol', 'issue_no']
writer = csv.DictWriter(csv_file, fieldnames=feature_names)
writer.writeheader()

for root, sub_dirs, files in os.walk(base_dir):
    if len(files) > 1:
        directory = root.split('/')
        try:
            issue_vol = directory[2].split('دوره ')[1].split(' -')[0]
            issue_no = directory[2].split('دوره ')[1].split(' -')[1].replace('شماره', '').strip()
        except:
            issue_vol = directory[2]
            issue_no = directory[2]
        txt_file = [file for file in files if '.txt' in file][0]
        title = txt_file.replace('.txt', '')
        f = open(f'{root}/{txt_file}')
        text = f.read()
        f.close()

        writer.writerow({
            'title': title,
            'text': text,
            'issue_vol': issue_vol, 'issue_no': issue_no
        })
        print(f'>> Add {title}')
    else:
        continue

