from bs4 import BeautifulSoup
# read monday.html as html
with open('panews.html', 'r') as f:
    html = f.read()

# html = '''
# <div data-v-6a3c8fec="" class="outer"><div data-v-6a3c8fec="" class="kx-date"><div data-v-6a3c8fec="" class="month">6 月</div> <div data-v-6a3c8fec="" class="date">12</div> <div data-v-6a3c8fec="" class="week"><p data-v-6a3c8fec="">星期一</p></div></div> <div data-v-6a3c8fec="" class="item"><div data-v-6a3c8fec="" class="point"></div> <div data-v-6a3c8fec="" class="pubtime">23:59</div> <div data-v-6a3c8fec="" class="content"><a data-v-6a3c8fec="" href="/zh/sqarticledetails/t4crhgt0.html" target="_blank" class="n-title">美国法院裁定 Galaxy Digital 无需向 BitGo 支付退出收购赔偿金</a> <p data-v-6a3c8fec="" class="">PANews 6 月 12 日消息，据彭博社援引美国特拉华州衡平法院的裁定报道，Galaxy Digital 去年退出收购 BitGo 交易计划是 “彻底终止”，驳回了 BitGo 要求的 1 亿美元终止费，或超过该金额的损害赔偿金，并指出 BitGo “未能在约定的日期前提交符合合同规定的 2021 年公司审计财务报表”。BitGo 发言人表示：“BitGo 计划对法院的裁决提出上诉，并继续认为 Galaxy 错误地终止了协议”。</p> <!----></div></div>
# '''
# parse html
soup = BeautifulSoup(html, 'html.parser')
# get kx-list class element
kx_list = soup.find(class_='kx-list')

# find all items
items = kx_list.find_all(class_='item')

for item in items:
    # extract title
    title = item.find(class_='n-title').get_text()

    # extract link
    link = item.find(class_='n-title')['href']

    # in case the base url is not in the 'href' attribute
    base_url = "https://www.panewslab.com"
    full_url = base_url + link

    # extract content
    content = item.find('p').get_text()

    print(f'Title: {title}\nLink: {full_url}\nContent: {content}\n---')
