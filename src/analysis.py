import pandas as pd
import networkx as nx

def compute_metrics(df):
    """计算基础文献计量指标 """
    return {
        "total_papers": len(df),
        "avg_citations": df["TC"].mean() if "TC" in df else 0
    }

def build_network(df, save_path):
    """构建关键词共现网络 """
    G = nx.Graph()
    keywords = df["DE"].str.split(";").explode().str.strip()
    keywords = keywords[keywords != ""]
    counts = keywords.value_counts().head(20)

    for kw, cnt in counts.items():
        G.add_node(kw, weight=cnt)

    nx.write_graphml(G, save_path)