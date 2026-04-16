import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(df, save_path):
    plt.figure(figsize=(10, 5))
    # 用新列名 Year
    if "Year" in df.columns:
        df["Year"].value_counts().sort_index().plot(kind="line", marker="o", color="#2196F3")
    plt.title("GaN 年度发文趋势")
    plt.xlabel("年份")
    plt.ylabel("发文量")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_keywords(df, save_path, top_n=15):
    # 用新列名 Author_Keywords_DE
    if "Author_Keywords_DE" in df.columns:
        keywords = df["Author_Keywords_DE"].str.split(";").explode().str.strip()
        keywords = keywords[keywords != ""]
        top = keywords.value_counts().head(top_n)

        plt.figure(figsize=(12, 6))
        sns.barplot(x=top.values, y=top.index)
        plt.title(f"Top {top_n} 关键词")
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        plt.close()