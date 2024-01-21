# Do classfication with the hlep of cohere
import cohere
from cohere.responses.classify import Example
import os


def cohere_investment_tag():
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    news = [
        "比特币矿企 Stronghold 完成 1500 万美元融资股权融资",
        "TON 生态 Launchpad 平台 TonUP 完成新一轮融资，Antalpha 等参投",
        "知情人士：OpenAI 正就新一轮融资进行讨论，估值在 1000 亿美元以上",
        "澳大利亚比特币矿商 Arkon Energy 完成 1.1 亿美元融资，Bluesky Capital Management 领投",
        "Tether 宣布投资 Academy of Digital Industries",
        "港交所：已准备好把握 “虚拟资产现货 ETF” 主题投资带来的机遇",
        "数据中心基础设施公司 Akron Energy 完成 1.1 亿美元融资，拟向美国比特币矿企提供支持",
        "公链项目 Shardeum 今年共计完成 720 万美元战略融资，估值 2.489 亿美元",
        "积分整合平台 Assemble Protocol 宣布获得 DWF Labs 战略投资",
        "Framework Ventures 对 Immutable 生态系统进行战略投资，具体金额暂未披露",
        "Web3 增长营销服务公司 Addressable 完成 600 万美元融资，Bitkraft Ventures 领投",
        "Qredo 获得 10T Holdings 领投的债务融资以维持运营，原领导层发生更迭",
        "Web3 粉丝平台 Medallion 完成 1370 万美元 A 轮融资，Dragonfly 和 Lightspeed Faction 共同领投",
        "去中心化患者网络 Humanscape 完成约 1534 万美元 C 轮延期融资，C 轮融资额已超 3000 万美元",
        "知情人士：Anthropic 正洽谈在 Menlo Ventures 牵头的一轮风投中融资 7.5 亿美元",
        "Web3 基础设施 Web3mine 完成 600 万美元种子轮融资，1kx 领投",
        "跨链流动性协议 Chainge Finance 已被 Coded Fi 收购，交易估值达 4700 万美元",
        "Web3 税务服务公司 Tres Finance 完成 1100 万美元 A 轮融资",
        "Web3 云计算平台 “4EVERLAND” 完成 200 万美元融资，Arweave 等参投",
        "DMM Group 旗下 Web3 子公司 DM2C Studio 完成 230 万美元融资，Galaxy Interactive 领投",
        "DWF Labs：热衷于支持和投资去中心化 AI 项目",
        "蓝港互动旗下 LK Venture 对比特币金融层解决方案 ALEX Labs 进行战略投资",
        "VanEck：投资比特币广告的机会成本很高，宁愿购买并持有比特币",
        "去中心化网络 formless 完成超 220 万美元 Pre-Seed 轮融资，a16z crypto 参投",
        "美国参议员 Warren 指责加密游说活动破坏了打击反恐融资的努力",
        "银行即服务平台 Fiat Republic 完成 700 万美元融资，Kraken Ventures 参投",
        "Web3 初创公司 Wynd Network 完成 350 万美元种子轮融资，Polychain Capital 等领投",
        "Algorand 生态成员推出分叉项目 “Voi” 并完成种子轮融资，Arrington Capital 参投",
        "Animoca Brands：截至 11 月 30 日持有现金和代币资产约 21 亿美元，已投资超 400 家公司",
        "CoinShares：上周数字资产投资产品净流出 1600 万美元，结束连续 11 周净流入趋势",
        "DID 市场聚合器 GoDID 以 3000 万美元估值完成新一轮融资，NGC 领投",
        "香港数字资产保险公司 OneDegree 获 Dubai Insurance 战略投资",
        "Nexon 旗下 NFT 游戏项目 MapleStory Universe 宣布获得 1 亿美元投资",
        "一 MUBI 早期投资者卖出价值 118 万美元的 MUBI 代币，预计获利 100 万美元",
        "比特币矿企 Unblock Global 完成 1500 万美元融资",
    ]
    response = co.classify(
        model="embed-multilingual-v3.0",
        inputs=news,
      examples=[Example("连接法币和数字货币的 B2B 技术公司 Almond FinTech 融资 700 万美元", "项目融资"), Example("Velo Labs 宣布获得 DWF Labs 的 1000 万美元投资", "项目融资"), Example("加密分析公司 Block Scholes 完成 330 万美元融资", "项目融资"), Example("基于 DLT 技术的债券交易所 BondbloX 完成 600 万美元 B 轮融资，花旗参投", "项目融资"), Example("基于区块链的房产投资平台 mogul Club 完成 360 万美元融资", "项目融资"), Example("Web3 电信数字解决方案提供商 Moflix 完成 310 万美元种子轮融资", "项目融资"), Example("DeFi 初创公司 Definitive 完成 410 万美元融资，Coinbase Ventures 等参投", "项目融资"), Example("以太坊扩容公司 Stackr Labs 完成 550 万美元种子轮融资，Archetype 领投", "项目融资"), Example("自托管加密投资应用 Sock 完成 300 万美元种子轮融资", "项目融资"), Example("去中心化 AI 计算平台 Ritual 完成 2500 万美元融资，Arcetype 领投\n", "项目融资"), Example("NFT 认证公司 Authentick 完成 400 万美元种子轮融资", "项目融资"), Example("GameFi 平台 Citadel 完成 330 万美元种子轮融资，1kx 领投", "项目融资"), Example("Web3 开发商 QuickNode 获得韩国 LG CNS 战略投资", "项目融资"), Example("Pimlico 完成由 a16z crypto 领投的 420 万美元种子轮融资", "项目融资"), Example("稳定币初创公司 StablR 完成 330 万欧元种子轮融资", "项目融资"), Example("支付初创公司 Due 完成 330 万美元种子轮融资，以开发基于区块链的平台", "项目融资"), Example("Llama 完成 600 万美元种子轮融资，Founders Fund 和 Electric Capital 领投", "项目融资"), Example("杜均：将成立资金规模 1 亿美元、专注 AI 投资孵化的实验室", "基金募资"), Example("渣打银行子公司和 SBI Holdings 计划联合向加密初创公司投资 1 亿美元", "基金募资"), Example("蓝港互动将发起规模 1500 万美元的比特币网络生态投资基金 BTC NEXT", "基金募资"), Example("Kyber Network 联创 Loi Luu 推出风险投资工作室 Calibre Venture Builder Studio", "基金募资"), Example("HashKey Capital 将为其第三支基金募集 5 亿美元", "基金募资"), Example("加密风投 Maven 11 正在为其第三只基金募资 1 亿美元", "基金募资"), Example("Lightspeed Faction 推出首支 2.85 亿美元的早期加密基金", "基金募资"), Example("SBI Holdings 将于年内启动规模达 6.63 亿美元的 Web3 基金", "基金募资"), Example("Ninety Eight 推出 2500 万美元的生态系统基金", "基金募资"), Example("EJF Capital 旗下一只基金已募资 1.04 亿美元，将投资区块链等领域", "基金募资"), Example("高盛筹集 150 亿美元购买私募股权基金股份", "基金募资"), Example("蚂蚁集团计划退出对 A&T Capital 的投资，从 1 亿美元的基金中撤资", "基金募资"), Example("欧洲加密资管公司 CoinShares 推出其美国对冲基金部门", "基金募资"), Example("韩国釜山拟建立市级区块链主网，并设立 7500 万美元区块链基金", "基金募资"), Example("Varys Capital 拟为其为区块链创新股权基金筹集 7500 万美元", "基金募资"), Example("Oak Grove Ventures 推出 6000 万美元新基金，将投资 Web3、AI 等领域", "基金募资"), Example("Blockchain Capital 为两只新的加密基金筹集了 5.8 亿美元", "基金募资"), Example("Tim Draper 推出新加密风险工作室 Draper Goren Blockchain", "基金募资")]
    )
    print(len([i for i in response.classifications if i.prediction == "项目融资"]))
    for i in range(len(response.classifications)):
        if (
            response.classifications[i].prediction == "项目融资"
            and response.classifications[i].confidence > 0.3
        ):
            print(news[i])


def cohere_fund_tag():
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    news = [
        "彭博分析师：贝莱德拟于 1 月 3 日为比特币现货 ETF 注入 1000 万美元种子基金",
        "韩国游戏公司 Wemade 与新加坡 Whampoa Digital 共同推出 1 亿美元的 Web3 基金",
        "致力于以太坊提议者与构建者分离的 PBS 基金会已筹集 100 万美元",
        "Trustless Labs 推出 1000 万美元的比特币生态系统第一阶段基金",
        "可编程隐私网络 Aleo 宣布成立 Aleo 基金会",
        "Cardano 基金会与巴西国家石油公司 Petrobras 合作开展区块链教育",
        "人权基金会向全球 18 个比特币项目捐赠 50 万美元",
        "MetisDAO 基金会推出 1 亿美元的生态发展基金",
        "Dfinity 基金会在 ICP 上推出符合 GDPR 标准的欧洲子网",
    ]
    response = co.classify(
        model="embed-multilingual-v3.0",
        inputs=news,
        examples=[
            Example(
                "杜均：将成立资金规模 1 亿美元、专注 AI 投资孵化的实验室", " 基金募资"
            ),
            Example(
                "渣打银行子公司和 SBI Holdings 计划联合向加密初创公司投资 1 亿美元",
                " 基金募资",
            ),
            Example(
                "蓝港互动将发起规模 1500 万美元的比特币网络生态投资基金 BTC NEXT",
                " 基金募资",
            ),
            Example(
                "Kyber Network 联创 Loi Luu 推出风险投资工作室 Calibre Venture Builder Studio",
                " 基金募资",
            ),
            Example("HashKey Capital 将为其第三支基金募集 5 亿美元", " 基金募资"),
            Example("加密风投 Maven 11 正在为其第三只基金募资 1 亿美元", " 基金募资"),
            Example(
                "Lightspeed Faction 推出首支 2.85 亿美元的早期加密基金", " 基金募资"
            ),
            Example(
                "SBI Holdings 将于年内启动规模达 6.63 亿美元的 Web3 基金", " 基金募资"
            ),
            Example(
                "加密投资机构 Deus X Capital 宣布成立，并称已积累 10 亿美元的投资资产与资本",
                " 基金募资",
            ),
            Example("Ninety Eight 推出 2500 万美元的生态系统基金", " 基金募资"),
            Example(
                "彭博社：自年初以来 Silver Point 等对冲基金已购入价值逾 2.5 亿美元的 FTX 债权",
                "Other",
            ),
            Example(
                "Uniswap 基金会近一年资助 72 个项目，承诺资金约 450 万美元", "Other"
            ),
            Example(
                "任景信：香港数码港与 40 多支 Web3 基金联系紧密，这些基金资产总计 40 亿美元",
                "Other",
            ),
            Example("美国 SEC 联合其它五家监管机构对加密投资发出警告", "Other"),
            Example(
                "数据：2023 年 9 月加密市场融资 5.05 亿美元，同比下降 72.6%", "Other"
            ),
            Example(
                "美国司法部：FTX 客户、投资者和员工将在 SBF 审判中出庭作证", "Other"
            ),
            Example(
                "南华早报：JPEX 暴雷可能成为香港历史上最大的金融欺诈案，但投资者信心会随牛市而恢复",
                "Other",
            ),
            Example(
                "连接法币和数字货币的 B2B 技术公司 Almond FinTech 融资 700 万美元",
                "项目融资",
            ),
            Example("Velo Labs 宣布获得 DWF Labs 的 1000 万美元投资", "项目融资"),
            Example("加密分析公司 Block Scholes 完成 330 万美元融资", "项目融资"),
            Example(
                "拉美加密公司 Galactic Holdings 完成 625 万美元 A 轮融资，Dragonfly 等领投",
                "项目融资",
            ),
            Example(
                "基于 DLT 技术的债券交易所 BondbloX 完成 600 万美元 B 轮融资，花旗参投",
                "项目融资",
            ),
            Example(
                "基于区块链的房产投资平台 mogul Club 完成 360 万美元融资", "项目融资"
            ),
            Example(
                "Web3 电信数字解决方案提供商 Moflix 完成 310 万美元种子轮融资",
                "项目融资",
            ),
            Example(
                "DeFi 初创公司 Definitive 完成 410 万美元融资，Coinbase Ventures 等参投",
                "项目融资",
            ),
            Example(
                "以太坊扩容公司 Stackr Labs 完成 550 万美元种子轮融资，Archetype 领投",
                "项目融资",
            ),
            Example("自托管加密投资应用 Sock 完成 300 万美元种子轮融资", "项目融资"),
            Example(
                "去中心化 AI 计算平台 Ritual 完成 2500 万美元融资，Arcetype 领投",
                "项目融资",
            ),
            Example("NFT 认证公司 Authentick 完成 400 万美元种子轮融资", "项目融资"),
            Example(
                "GameFi 平台 Citadel 完成 330 万美元种子轮融资，1kx 领投", "项目融资"
            ),
            Example("Web3 开发商 QuickNode 获得韩国 LG CNS 战略投资", "项目融资"),
            Example(
                "Pimlico 完成由 a16z crypto 领投的 420 万美元种子轮融资", "项目融资"
            ),
            Example("稳定币初创公司 StablR 完成 330 万欧元种子轮融资", "项目融资"),
            Example(
                "支付初创公司 Due 完成 330 万美元种子轮融资，以开发基于区块链的平台",
                "项目融资",
            ),
            Example(
                "Llama 完成 600 万美元种子轮融资，Founders Fund 和 Electric Capital 领投",
                "项目融资",
            ),
        ],
    )
    print(len([i for i in response.classifications if i.prediction == "基金募资"]))
    for i in range(len(response.classifications)):
        if (
            response.classifications[i].prediction == "基金募资"
            and response.classifications[i].confidence > 0.51
        ):
            print(news[i])


if __name__ == "__main__":
    cohere_investment_tag()
    # cohere_fund_tag()
