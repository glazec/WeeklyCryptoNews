import streamlit as st
from bs4 import BeautifulSoup
import datetime
from icecream import ic
import sentry_sdk
from bs4 import BeautifulSoup
import pandas as pd
from classifier import classifier
import time

# sentry_sdk.init(
#     dsn="https://fc880ea6ee11c5613ad2eb62d9eb2bf1@o262884.ingest.sentry.io/4505684111785984",

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0
# )


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    news_html = soup.find(class_='kx-list')
    # find all items
    items = news_html.find_all(class_='item')
    titles = []
    urls = []
    contents = []

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
        contents.append(content)
        urls.append(full_url)
        titles.append(title)

        # print(f'Title: {title}\nLink: {full_url}\nContent: {content}\n---')
    news_df = pd.DataFrame({'title': titles, 'url': urls, 'content': contents})
    return news_df


def check_keywords(x, keywords):
    return any(keyword.lower() in x.lower() for keyword in keywords)


def applyTag(news_df):
    keywords_dict = {
        'investment': ['融资', '投资', '收购', '孵化'],
        'fund': ['募集', '募资', '撤资', '基金', '风险工作室'],
        'infra': ['基础设施', '上线', '主网', '测试网'],
        'defi': ['DeFi', 'Uniswap', 'Aave', 'MakerDAO', 'compound'],
        'nft': ['NFT', 'OpenSea', 'Rarible', 'SuperRare', 'Nifty Gateway'],
        'wallet': ['钱包', 'Safe', 'MetaMask', 'imToken', 'Ledger', 'Trezor'],
        'exchange': ['交易所'],
        'regulation': ['监管', '法律', '法规', '政策', 'SEC', '诉讼']
    }

    keywords_blacklist = {
        'investment': ['数据：'],
        'fund': ['数据：'],
        'infra': ['数据：'],
        'defi': ['数据：', ],
        'nft': ['数据：'],
        'wallet': ['数据：'],
        'exchange': ['数据：'],
        'regulation': ['数据：']
    }

    news_df['tag'] = news_df['title'].apply(lambda x: [
        tag for tag, keywords in keywords_dict.items()
        if check_keywords(x, keywords) and not any(blackword.lower() in x.lower() for blackword in keywords_blacklist[tag])
    ])
    # use classfier(title) to refine investment tag
    # for i in range(len(news_df)):
    #     if 'investment' in news_df.iloc[i]['tag']:
    #         new_tag = classifier(news_df.iloc[i]['title'])
    #         if new_tag != news_df.iloc[i]['tag']:
    #             ic(
    #                 f"Changed tag for {news_df.iloc[i]['title']} from {news_df.iloc[i]['tag']} to {new_tag}")
    #             news_df.iloc[i]['tag'] = [new_tag]
    #             ic(news_df.iloc[i]['tag'], [new_tag])
    #         # sleep 0.5s
    #         time.sleep(0.5)
    # save to csv
    news_df.to_csv('news_df.csv')
    ic("Apply Tag")
    return news_df


def main():
    st.title("每周新闻生成器（Alpha）")
    # upload file
    html = st.file_uploader("上传 PANews HTML", type="html")
    if html is not None:
        if 'news_df' not in st.session_state or st.session_state['html'] != html:
            news_df = parse(html)
            news_df = applyTag(news_df)
            st.session_state['news_df'] = news_df
            st.session_state['html'] = html
        else:
            news_df = st.session_state['news_df']
        tag_selector = st.selectbox('Select a tag', ('investment', 'fund',
                                    'infra', 'defi', 'nft', 'wallet', 'exchange', 'regulation'))
        # format_string = ''
        for i in range(len(news_df)):
            if tag_selector in news_df.iloc[i]['tag']:
                # print(news_df.iloc[i])
                st.markdown(
                    f"[{news_df.iloc[i]['title']}]({news_df.iloc[i]['url']})")
                st.write(news_df.iloc[i]["content"])
                # format_string += f"{news_df.iloc[i]['title']}\n"
        # st.write(format_string)
        # print(format_string)


if __name__ == "__main__":
    main()
