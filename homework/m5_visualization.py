"""
M5 Matplotlib & Seaborn 視覺化 — 課後作業
==========================================
情境：把分析結果做成圖表，用視覺化說故事。

資料路徑：datasets/ecommerce/orders_enriched.csv
"""
import matplotlib
matplotlib.use("Agg")  # 無 GUI 環境也能跑
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def _load_data():
    """輔助函式：讀取資料"""
    return pd.read_csv("datasets/ecommerce/orders_enriched.csv",
                       parse_dates=["order_date"])


# ============================================================
# 🟢 送分題（每題 10 分，共 30 分）
# ============================================================

def green_bar_category():
    """
    畫出每個商品類別 (category) 的訂單數長條圖
    回傳 matplotlib Figure 物件
    提示：sns.countplot 或 value_counts().plot.bar()
    """
    # TODO: 你的程式碼
    cate_count = df['category'].value_counts().reset_index()
    cate_count.columns = ['category', 'order_count']

    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(
        data = cate_count,
        x = 'category',
        y = 'order_count',
        hue = 'category',
        palette = 'viridis',
        legend = False,
        ax = ax,
    )
    plt.tight_layout()
    return plt


def green_hist_amount():
    """
    畫出訂單金額 (amount) 的分佈直方圖，分 20 個 bin
    回傳 matplotlib Figure 物件
    提示：sns.histplot(bins=20) 或 plt.hist()
    """
    # TODO: 你的程式碼
    fig, ax = plt.subplots(figsize = (8,4))
    sns.histplot(
        data = df,
        x = 'amount',
        bins = 20,
        ax = ax,
    )
    ax.set_xlabel('Amount(NT$)')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    return fig


def green_set_labels():
    """
    建立一個簡單的長條圖（內容不限），但必須設定：
    - 圖標題 (title)
    - X 軸標籤 (xlabel)
    - Y 軸標籤 (ylabel)
    回傳 matplotlib Figure 物件
    """
    # TODO: 你的程式碼
    cate_count = df['category'].value_counts().reset_index()
    cate_count.columns = ['category', 'order_count']

    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(
        data = cate_count,
        x = 'category',
        y = 'order_count',
        hue = 'category',
        palette = 'viridis',
        legend = False,
        ax = ax,
    )
    ax.set_title('Order Count by Category', fontweight='bold')
    ax.set_xlabel('Category')
    ax.set_ylabel('Order Count')

    plt.tight_layout()
    return fig



# ============================================================
# 🟡 核心題（每題 15 分，共 45 分）
# ============================================================

def yellow_line_region_trend():
    """
    畫折線圖：比較 North 和 South 兩個地區的月營收趨勢
    - X 軸：月份
    - Y 軸：該月總營收
    - 兩條線，有圖例 (legend)
    回傳 matplotlib Figure 物件
    提示：分別 groupby 再 plot，或用 sns.lineplot(hue='region')
    """
    # TODO: 你的程式碼
    ns_df = df[df['region'].isin(['North', 'South'])].copy()
    ns_df['month'] = ns_df['order_date'].dt.to_period('M')

    monthly_ns = (
        ns_df.groupby(['month', 'region'])['amount']
        .sum()
        .reset_index()
    )
    monthly_ns['month'] = monthly_ns['month'].astype(str)

    fig, ax = plt.subplots(figsize = (10, 4))
    sns.lineplot(
        data = monthly_ns,
        hue = 'region',
        x = 'month',
        y = 'amount',
        marker = 'o',
        linewidth = 2,
    )
    ax.set_title('Monthly Revenue: North vs South', fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue(NT$)')
    plt.xticks(rotation = 45)
    ax.legend(title = 'Region')
    plt.tight_layout
    return fig


def yellow_box_vip():
    """
    畫箱形圖：比較不同 VIP 等級 (vip_level) 的訂單金額分佈
    回傳 matplotlib Figure 物件
    提示：sns.boxplot(x='vip_level', y='amount', data=df)
    """
    # TODO: 你的程式碼
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(
        data = df,
        x = 'vip_level',
        y = 'amount',
        hue = 'vip_level',
        palette = 'Set3',
        legend = False,
        ax = ax
    )
    ax.set_title('Order Amount Distribution by VIP Level', fontweight='bold')
    ax.set_xlabel('VIP Level')
    ax.set_ylabel('Amount(NT$)')
    plt.tight_layout()
    return fig


def yellow_scatter_price_amount():
    """
    畫散佈圖：X=商品單價 (unit_price)，Y=訂單金額 (amount)
    回傳 matplotlib Figure 物件
    提示：plt.scatter() 或 sns.scatterplot()
    """
    # TODO: 你的程式碼
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(
        data = df,
        x = 'unit_price',
        y = 'amount',
        alpha = 0.5,
        ax = ax
    )
    ax.set_title('Unit Price vs Amount')
    ax.set_xlabel('Unit Price(NT$)')
    ax.set_ylabel('Amount(NT$)')
    plt.tight_layout()
    return fig



# ============================================================
# 🔴 挑戰題（25 分）
# ============================================================

def red_category_dashboard(category="Electronics"):
    """
    針對指定類別，畫 2×2 的 subplot dashboard：
    1. 左上：該類別月營收趨勢 (折線圖)
    2. 右上：該類別各地區營收 (長條圖)
    3. 左下：該類別 Top 5 商品營收 (水平長條圖)
    4. 右下：該類別訂單金額分佈 (直方圖)

    回傳 matplotlib Figure 物件
    提示：fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    """
    # TODO: 你的程式碼
    cat_df = df[df['category'] == category].copy()
    cat_df['month'] = cat_df['order_date'].dt.to_period('M').astype(str)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'{category} Dashboard', fontsize=16, fontweight='bold')
    
    monthly = cat_df.groupby('month')['amount'].sum().reset_index()
    sns.lineplot(data=monthly, x='month', y='amount', marker='o', ax=axes[0, 0])
    axes[0, 0].set_title('Monthly Revenue Trend')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Revenue')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    region = cat_df.groupby('region')['amount'].sum().reset_index()
    sns.barplot(data=region, x='region', y='amount', palette='viridis', ax=axes[0, 1])
    axes[0, 1].set_title('Revenue by Region')
    axes[0, 1].set_xlabel('Region')
    axes[0, 1].set_ylabel('Revenue')
    
    top5 = cat_df.groupby('product_name')['amount'].sum().nlargest(5).reset_index()
    sns.barplot(data=top5, x='amount', y='product_name', palette='viridis', ax=axes[1, 0])
    axes[1, 0].set_title('Top 5 Products')
    axes[1, 0].set_xlabel('Revenue')
    axes[1, 0].set_ylabel('Product')
    
    sns.histplot(data=cat_df, x='amount', bins=20, ax=axes[1, 1])
    axes[1, 1].set_title('Amount Distribution')
    axes[1, 1].set_xlabel('Amount')
    axes[1, 1].set_ylabel('Frequency')
    
    plt.tight_layout()
    return fig
