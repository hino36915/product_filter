import pandas as pd


all_files = [
    "prod_main-sampled-20250902.csv",
    "prod_detail-sampled-20250902.csv",
    "prod_category-sampled-20250902.csv",
    "detail_image-sampled-20250902.csv",
    "detail_sku-sampled-20250902.csv",
    "detail_sku_attr-20250902.csv",
    "detail_sku_image-sampled-20250902.csv",
]
dataframes = {}
try:
    merge_df = pd.read_csv(all_files[0])

    for file_path in all_files[1:]:
        temp_df = pd.read_csv(file_path)
        merge_df = pd.merge(merge_df, temp_df, on="prod_id", how="left")

    print("\n 所有檔案合併完成！")


except Exception as e:
    print(f"\n exception 題：{e}。")
