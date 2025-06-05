# 项目提案 —— 中国A股市场经典因子分析

> English: [docs/proposal.md](proposal.md)

本项目旨在系统性分析中国A股市场中经典投资因子的表现。分析内容包括：

- **单因子分析**：因子包括：
  - **市场因子**
    - Beta
  - **技术因子**
    - 动量
    - 反转
    - 低波动
    - 换手率
  - **基本面因子**
    - 市值
    - 价值
    - 质量
    - 投资
    - 盈利能力
- **经典因子模型**：
  - Fama-French三因子模型（1993）
  - Carhart四因子模型（1997）
  - Novy-Marx四因子模型（2013）
  - Fama-French五因子模型（2015）
  - Hou-Xue-Zhang四因子模型（2015）
  - Stambaugh-Yuan四因子模型（2017）
  - Hou-Xue-Zhang五因子模型（2019）
  - Daniel-Hirshleifer-Sun三因子模型（2020）

## 数据来源

- **Tushare**：中国金融市场的综合数据提供商，涵盖股票价格、财务报表及其他市场数据。

数据将通过 [Tushare API](https://tushare.pro) 获取，并借助 [bagel-tushare](https://github.com/bagelquant/bagel-tushare) 包存储到本地 MySQL 数据库。为简化流程，项目将从本地 MySQL 数据库提取数据，并保存为 `data/` 目录下的 CSV 文件。所有分析均基于这些 CSV 文件进行。

## 因子构建

- **股票池**
  - 上交所和深交所主板（主板）全部股票
  - 剔除市值低于1亿元人民币的股票
  - 剔除上市时间少于6个月的股票
- **构建方法（单因子分析）**
  - 排序法：将股票分为10组，构建多空组合为第10组减第1组
  - 横截面回归
- 经典因子模型的构建方法将遵循原始论文。

## 报告与可视化

将使用 Streamlit 实现交互式报告与可视化。报告内容包括：

- 单因子分析
- 经典因子模型

## 项目结构

项目结构如下：

```
project_root/
├── data/                  # CSV 文件目录
├── docs/                  # 文档文件
├── src/                   # 数据处理与分析源码
│   ├── database/          # 数据库访问与管理模块
│   ├── analysis/          # 因子分析与模型实现模块
│   └── streamlit_pages/   # Streamlit 页面定义与界面逻辑
├── tests/                 # 源码单元测试
├── reports/               # 生成的报告与可视化内容
├── requirements.txt       # Python 依赖包
├── README.md              # 项目概述与安装说明
├── config.json            # 数据库配置文件（不纳入 Git 管理）
├── update_data.py         # 从数据库提取数据并保存为 CSV 的脚本
├── main.py                # 分析主脚本
└── streamlit_app.py       # Streamlit 交互式报告应用
```