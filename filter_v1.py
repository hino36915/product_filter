import pandas as pd


all_files = [
    'prod_main-sampled-20250902.csv', 'prod_detail-sampled-20250902.csv',
    'prod_category-sampled-20250902.csv', 'detail_image-sampled-20250902.csv',
    'detail_sku-sampled-20250902.csv', 'detail_sku_attr-20250902.csv',
    'detail_sku_image-sampled-20250902.csv'
]
dataframes = {}
try:
   
    for file_path in all_files:
       
        df = pd.read_csv(file_path)
        
    
        print(df)

 
except Exception as e:
    print(f"\n exception 題：{e}。")