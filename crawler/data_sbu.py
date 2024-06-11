import csv
import requests
from bs4 import BeautifulSoup


def extract_features(article_url):
    req = requests.get(url=article_url)
    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find('span', class_='article_title bold').text.strip()
    list_a = soup.find('ul', class_='list-inline list-inline-seprator margin-bottom-6 rtl') \
        .find_all('li', class_='padding-3')
    authors = []
    for a in list_a:
        authors.append(a.find('a').text)
    abstract = soup.find('div', class_='padding_abstract justify rtl').text.strip()
    keywords = [keyword.text.strip() for keyword in
                soup.find('ul', class_='block list-inline list-inline-seprator margin-bottom-6 rtl').find_all('li')]

    return {
        'Title': title,
        'Authors': authors,
        'Link': article_url,
        'Abstract': abstract,
        'Keywords': keywords
    }


def write_to_csv(articles, writer):
    for article in articles:
        writer.writerow(article)


issue_links = [
    'https://ecoj.sbu.ac.ir/issue_6574_7158.html',
    'https://ecoj.sbu.ac.ir/issue_6574_7157.html',
    'https://ecoj.sbu.ac.ir/issue_6574_7156.html',
    'https://ecoj.sbu.ac.ir/issue_6574_7155.html',
    'https://ecoj.sbu.ac.ir/issue_6573_7153.html',
    'https://ecoj.sbu.ac.ir/issue_6573_7152.html',
    'https://ecoj.sbu.ac.ir/issue_6572_6577.html',
    'https://ecoj.sbu.ac.ir/issue_6572_6576.html',
    'https://ecoj.sbu.ac.ir/issue_6572_6575.html',
    'https://ecoj.sbu.ac.ir/issue_6567_6570.html',
    'https://ecoj.sbu.ac.ir/issue_6567_6569.html',
    'https://ecoj.sbu.ac.ir/issue_6567_6568.html',
    'https://ecoj.sbu.ac.ir/issue_6550_6551.html',
    'https://ecoj.sbu.ac.ir/issue_6550_6552.html',
    'https://ecoj.sbu.ac.ir/issue_5154_6398.html',
    'https://ecoj.sbu.ac.ir/issue_5154_6397.html',
    'https://ecoj.sbu.ac.ir/issue_5154_6396.html',
    'https://ecoj.sbu.ac.ir/issue_5154_5280.html',
    'https://ecoj.sbu.ac.ir/issue_5937_5938.html',
    'https://ecoj.sbu.ac.ir/issue_5937_6395.html',
    'https://ecoj.sbu.ac.ir/issue_5937_7566.html',
    'https://ecoj.sbu.ac.ir/issue_5937_7567.html',
    'https://ecoj.sbu.ac.ir/issue_9428_9429.html',
    'https://ecoj.sbu.ac.ir/issue_9428_10078.html',
    'https://ecoj.sbu.ac.ir/issue_9428_10446.html',
    'https://ecoj.sbu.ac.ir/issue_9428_11201.html',
    'https://ecoj.sbu.ac.ir/issue_11596_11597.html',
    'https://ecoj.sbu.ac.ir/issue_11596_11653.html',
    'https://ecoj.sbu.ac.ir/issue_11596_11664.html',
    'https://ecoj.sbu.ac.ir/issue_11596_11665.html',
    'https://ecoj.sbu.ac.ir/issue_14789_14790.html',
    'https://ecoj.sbu.ac.ir/issue_14789_14855.html',
    'https://ecoj.sbu.ac.ir/issue_14789_14856.html',
    'https://ecoj.sbu.ac.ir/issue_14789_14900.html',
    'https://ecoj.sbu.ac.ir/issue_14901_14964.html',
    'https://ecoj.sbu.ac.ir/issue_14901_14965.html',
    'https://ecoj.sbu.ac.ir/issue_14901_15004.html',
    'https://ecoj.sbu.ac.ir/issue_14901_15013.html',
    'https://ecoj.sbu.ac.ir/issue_15051_15052.html',
    'https://ecoj.sbu.ac.ir/issue_15051_15113.html',
    'https://ecoj.sbu.ac.ir/issue_15051_15181.html',
    'https://ecoj.sbu.ac.ir/issue_15051_15220.html',
    'https://ecoj.sbu.ac.ir/issue_15276_15277.html',
    'https://ecoj.sbu.ac.ir/issue_15276_15325.html'
]

articles = x = ['article_57611.html', 'article_57610.html', 'article_57609.html', 'article_57608.html', 'article_57607.html', 'article_57606.html', 'article_57605.html', 'article_57604.html', 'article_57563.html', 'article_57562.html', 'article_57561.html', 'article_57559.html', 'article_57558.html', 'article_57557.html', 'article_57556.html', 'article_57555.html', 'article_57554.html', 'article_57553.html', 'article_57552.html', 'article_57551.html', 'article_57550.html', 'article_57549.html', 'article_57548.html', 'article_57547.html', 'article_57515.html', 'article_57514.html', 'article_57513.html', 'article_57511.html', 'article_57509.html', 'article_57508.html', 'article_57507.html', 'article_57506.html', 'article_57504.html', 'article_57503.html', 'article_57502.html', 'article_57501.html', 'article_57500.html', 'article_57499.html', 'article_57498.html', 'article_57497.html', 'article_57496.html', 'article_57495.html', 'article_57494.html', 'article_57493.html', 'article_57492.html', 'article_57491.html', 'article_57489.html', 'article_57488.html', 'article_57459.html', 'article_57458.html', 'article_57457.html', 'article_57456.html', 'article_57455.html', 'article_57453.html', 'article_57445.html', 'article_53518.html', 'article_53517.html', 'article_53519.html', 'article_53520.html', 'article_53521.html', 'article_53522.html', 'article_53523.html', 'article_53524.html', 'article_53516.html', 'article_53515.html', 'article_53514.html', 'article_53513.html', 'article_53512.html', 'article_53511.html', 'article_53510.html', 'article_53508.html', 'article_53507.html', 'article_53506.html', 'article_53505.html', 'article_53504.html', 'article_53503.html', 'article_53502.html', 'article_53501.html', 'article_53500.html', 'article_53499.html', 'article_53498.html', 'article_53497.html', 'article_53496.html', 'article_53495.html', 'article_53493.html', 'article_53492.html', 'article_53491.html', 'article_53490.html', 'article_53489.html', 'article_53488.html', 'article_53440.html', 'article_53439.html', 'article_53438.html', 'article_53437.html', 'article_53436.html', 'article_53435.html', 'article_53434.html', 'article_53433.html', 'article_53487.html', 'article_53486.html', 'article_53485.html', 'article_53484.html', 'article_53483.html', 'article_53482.html', 'article_53480.html', 'article_53476.html', 'article_52260.html', 'article_52259.html', 'article_52258.html', 'article_52257.html', 'article_52255.html', 'article_52254.html', 'article_52247.html', 'article_52248.html', 'article_52249.html', 'article_52250.html', 'article_52251.html', 'article_52252.html', 'article_52237.html', 'article_52238.html', 'article_52239.html', 'article_52240.html', 'article_52241.html', 'article_52242.html', 'article_45054.html', 'article_45055.html', 'article_45056.html', 'article_45057.html', 'article_45058.html', 'article_45059.html', 'article_49613.html', 'article_49612.html', 'article_49614.html', 'article_49615.html', 'article_49616.html', 'article_49617.html', 'article_52216.html', 'article_52217.html', 'article_52215.html', 'article_52218.html', 'article_52219.html', 'article_52220.html', 'article_60377.html', 'article_60376.html', 'article_60375.html', 'article_60374.html', 'article_60373.html', 'article_60372.html', 'article_67489.html', 'article_67488.html', 'article_67486.html', 'article_67483.html', 'article_67482.html', 'article_67481.html', 'article_74826.html', 'article_74825.html', 'article_74824.html', 'article_74518.html', 'article_74255.html', 'article_74239.html', 'article_79275.html', 'article_79276.html', 'article_79277.html', 'article_79278.html', 'article_79279.html', 'article_79280.html', 'article_81629.html', 'article_81628.html', 'article_81627.html', 'article_81626.html', 'article_81625.html', 'article_81624.html', 'article_86059.html', 'article_86065.html', 'article_86066.html', 'article_86067.html', 'article_86068.html', 'article_86069.html', 'article_87134.html', 'article_87135.html', 'article_87136.html', 'article_87137.html', 'article_87138.html', 'article_87139.html', 'article_87140.html', 'article_87141.html', 'article_87394.html', 'article_87395.html', 'article_87396.html', 'article_87397.html', 'article_87398.html', 'article_87399.html', 'article_87400.html', 'article_87401.html', 'article_87456.html', 'article_87457.html', 'article_87458.html', 'article_87459.html', 'article_87460.html', 'article_87461.html', 'article_87462.html', 'article_87463.html', 'article_87619.html', 'article_87623.html', 'article_87618.html', 'article_87620.html', 'article_87622.html', 'article_87621.html', 'article_87624.html', 'article_100517.html', 'article_100518.html', 'article_100519.html', 'article_100520.html', 'article_100521.html', 'article_100522.html', 'article_100523.html', 'article_100963.html', 'article_100964.html', 'article_100968.html', 'article_100965.html', 'article_100967.html', 'article_100966.html', 'article_100975.html', 'article_100969.html', 'article_100970.html', 'article_100971.html', 'article_100972.html', 'article_100973.html', 'article_100974.html', 'article_100976.html', 'article_101269.html', 'article_101270.html', 'article_101271.html', 'article_101272.html', 'article_101274.html', 'article_101273.html', 'article_101268.html', 'article_101914.html', 'article_101915.html', 'article_101916.html', 'article_101917.html', 'article_101918.html', 'article_101919.html', 'article_101920.html', 'article_101921.html', 'article_101922.html', 'article_101923.html', 'article_101924.html', 'article_101925.html', 'article_102213.html', 'article_102214.html', 'article_102215.html', 'article_102216.html', 'article_102217.html', 'article_102218.html', 'article_102335.html', 'article_102212.html', 'article_102337.html', 'article_102336.html', 'article_102338.html', 'article_102339.html', 'article_102597.html', 'article_102598.html', 'article_102599.html', 'article_102600.html', 'article_102596.html', 'article_102340.html', 'article_103049.html', 'article_103050.html', 'article_103051.html', 'article_103052.html', 'article_103053.html', 'article_103054.html', 'article_103364.html', 'article_103365.html', 'article_103366.html', 'article_103367.html', 'article_103368.html', 'article_103369.html', 'article_103622.html', 'article_103624.html', 'article_103625.html', 'article_103370.html', 'article_103626.html', 'article_103627.html', 'article_104009.html', 'article_103623.html', 'article_104010.html', 'article_104011.html', 'article_104012.html', 'article_104013.html', 'article_104407.html', 'article_104408.html', 'article_104409.html', 'article_104410.html', 'article_104411.html', 'article_104412.html']
# for issue in issue_links:
#     req = requests.get(url=issue)
#     articles_tags = BeautifulSoup(req.text, 'html.parser').find_all('a', class_='tag_a')
#     for tag in articles_tags:
#         articles.append(tag.get('href'))
print(f'Article URLs extracted!')
print(articles)
print('--------------------------')

filename = 'articles.csv'
csvfile = open(filename, 'a', newline='', encoding='utf-8')
feature_names = ['Title', 'Authors', 'Link', 'Abstract', 'Keywords']
writer = csv.DictWriter(csvfile, fieldnames=feature_names)
articles_len = len(articles)
for index, article in enumerate(articles):
    features = extract_features(article_url=f'https://ecoj.sbu.ac.ir/{article}')
    writer.writerow(features)
    print(f'Article {article} extracted ({index + 1} out of {articles_len})!')
