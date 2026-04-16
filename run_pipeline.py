# 项目一键运行总入口
# 运行命令：python run_pipeline.py

import os
import pandas as pd
from src.data_management import load_data, clean_data
from src.visualization import plot_trends, plot_keywords

def make_dirs():
    folders = [
        "data/raw",
        "data/processed",
        "outputs/figures",
        "outputs/networks",
        "reports"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def main():
    print("=" * 60)
    print("🚀 GaN 文献计量分析 开始运行")
    print("=" * 60)

    # 自动创建文件夹
    make_dirs()
    print("✅ 目录检查完成")

    # 直接读取你已经生成好的 CSV（完全匹配你现在的文件）
    data_path = "data/processed/gan_power_devices_cleaned_all.csv"

    # 加载数据
    df = load_data(data_path)
    print(f"✅ 数据加载完成：{len(df)} 篇文献")

    # 清洗数据
    df_clean = clean_data(df)
    df_clean.to_csv("data/processed/gan_power_devices_cleaned_all.csv", index=False, encoding="utf-8")
    print(f"✅ 数据清洗完成：{len(df_clean)} 篇有效文献")

    # 自动出图
    plot_trends(df_clean, "outputs/figures/yearly_trends.png")
    plot_keywords(df_clean, "outputs/figures/top_keywords.png")

    print("✅ 图表已保存到 outputs/figures/")
    print("🎉 项目全部运行完成！")

if __name__ == "__main__":
    main()