import pandas as pd
import numpy as np

def load_data(file_path):
    """加载 WoS 原始数据 """
    return pd.read_csv(file_path, encoding="utf-8")

def clean_data(df):
    """数据清洗：去重、缺失值填充、年份筛选 """
    # 用新列名去重（DOI）
    if "DOI" in df.columns:
        df = df.drop_duplicates(subset=["DOI"], keep="first")
    elif "Title" in df.columns:
        df = df.drop_duplicates(subset=["Title"], keep="first")

    # 填充空值
    if "Author_Keywords_DE" in df.columns:
        df["Author_Keywords_DE"] = df["Author_Keywords_DE"].fillna("")
    if "Title" in df.columns:
        df["Title"] = df["Title"].fillna("")

    # 筛选年份（用新列名 Year）
    if "Year" in df.columns:
        df = df[df["Year"].between(2020, 2025)]

    return df