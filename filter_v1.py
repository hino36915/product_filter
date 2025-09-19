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

file_configs = {
    "prod_main-sampled-20250902.csv": {
        "usecols": ["prod_id", "subject"]
    },
    "prod_detail-sampled-20250902.csv":{
        "usecols": ["prod_id", "description"]
    },
    "detail_image-sampled-20250902.csv": {
        "usecols": ["prod_id", "image_url"]
    },
    "detail_sku-sampled-20250902.csv": {
        "usecols": ["prod_id","vendor_price", "price", "sku_id"]
    },
    "prod_category-sampled-20250902.csv": {
        "usecols": ["prod_id", "prod_level_path"]
    },
      "detail_sku_attr-20250902.csv": {
        "usecols": ["prod_id", "attr_name","value","sku_id"]
    },
    "detail_sku_image-sampled-20250902.csv": {
        "usecols": ["prod_id",  "image_url","sku_id"]
    }
}
dataframes = {}


try:

    for file_path in all_files:
        if file_path in file_configs:
            
            print(f"正在讀取: {file_path}...")
            # 根據設定檔，讀取該檔案特定的欄位
            config = file_configs[file_path]
            df = pd.read_csv(file_path, usecols=config["usecols"])
            dataframes[file_path] = df
        
        else:
              print(f"警告：檔案 {file_path} 沒有對應的設定，已跳過。")        


    merge_df =dataframes["prod_main-sampled-20250902.csv"]
    
    
    
    prod_id_join_files = [
        "prod_detail-sampled-20250902.csv",
        "prod_category-sampled-20250902.csv",
        "detail_image-sampled-20250902.csv",
        "detail_sku-sampled-20250902.csv" 
    ]
    multi_join_files = [
        "detail_sku_attr-20250902.csv",
        "detail_sku_image-sampled-20250902.csv"
    ]
    for file_name in prod_id_join_files:
        
            print(f"正在合併 : {file_name}")
            merge_df = pd.merge(merge_df,
                                  dataframes[file_name],
                                  on="prod_id",
                                  how="left"
                                  
                                  )
            
            
            
     
    for file_name in multi_join_files:
           if file_name in dataframes:
                print(f"正在合併 : {file_name}")
                merge_df = pd.merge(merge_df,
                                  dataframes[file_name],
                                  on=["prod_id","sku_id"],
                                  how="left"
                                  
                                  )
            
            
     
        
except Exception as e:
    print(f"\n exception ：{e}。")