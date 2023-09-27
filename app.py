import streamlit as st
from bs4 import BeautifulSoup
import datetime
from icecream import ic
import sentry_sdk
from bs4 import BeautifulSoup
import pandas as pd

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
    for keyword in keywords:
        if keyword in x:
            return True
    return False


def applyTag(news_df):
    investment_keywords = ['融资', '投资', '收购', '孵化']
    fund_keywords = ['募集', '募资', '撤资', '基金', '风险工作室']
    news_df['tag'] = news_df['title'].apply(
        lambda x: ['investment'] if check_keywords(x, investment_keywords) else [])
    news_df['tag'] = news_df.apply(
        lambda row: row['tag'] + ['fund'] if check_keywords(row['title'], fund_keywords) else row['tag'], axis=1)
    return news_df


def main():
    st.title("每周新闻生成器（Alpha）")
    # upload file
    html = st.file_uploader("上传 PANews HTML", type="html")
    if html is None:
        st.stop()
    news_df = parse(html)
    news_df = applyTag(news_df)
    tag_selector = st.selectbox('Select a tag', ('investment', 'fund'))
    for i in range(len(news_df)):
        if tag_selector in news_df.iloc[i]['tag']:
            print(news_df.iloc[i])
            st.markdown(
                f"[{news_df.iloc[i]['title']}]({news_df.iloc[i]['url']})")
            st.write(news_df.iloc[i]["content"])


if __name__ == "__main__":
    main()
