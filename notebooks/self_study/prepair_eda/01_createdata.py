import pandas as pd
import numpy as np

# Cố định seed
np.random.seed(42)

# 1. Categories (Danh mục chính của Apple)
categories_list = ['Mac', 'iPad', 'iPhone', 'Watch', 'AirPods', 'Accessories']
categories = pd.DataFrame({
    'CategoryID': range(1, len(categories_list) + 1),
    'CategoryName': categories_list
})
categories.to_csv('Categories_2.csv', index=False)

# 2. SubCategories (Các dòng sản phẩm cụ thể)
subcat_mapping = {
    'Mac': ['MacBook Air', 'MacBook Pro', 'iMac', 'Mac mini', 'Mac Studio'],
    'iPad': ['iPad Pro', 'iPad Air', 'iPad mini', 'iPad'],
    'iPhone': ['iPhone 15 Pro Max', 'iPhone 15', 'iPhone 14', 'iPhone 13', 'iPhone SE'],
    'Watch': ['Apple Watch Ultra 2', 'Apple Watch Series 9', 'Apple Watch SE'],
    'AirPods': ['AirPods Pro 2', 'AirPods Max', 'AirPods 3'],
    'Accessories': ['AirTag', 'MagSafe Charger', 'Apple Pencil', 'Magic Keyboard']
}
subcat_data = []
subcat_id = 101
for cat_idx, cat in enumerate(categories_list):
    cat_id = cat_idx + 1
    for sub in subcat_mapping[cat]:
        subcat_data.append([subcat_id, cat_id, sub])
        subcat_id += 1

subcategories = pd.DataFrame(subcat_data, columns=['SubCategoryID', 'CategoryID', 'SubCategoryName'])
subcategories.to_csv('SubCategories_2.csv', index=False)

# 3. Products (100 sản phẩm với giá USD)
n_prod = 100
suffixes = ['256GB', '512GB', '1TB', 'Wi-Fi', 'Cellular', 'Midnight', 'Starlight', 'Space Gray', 'Silver', 'Titanium']
product_names = []
subcat_ids_for_prod = []

for i in range(n_prod):
    random_subcat = subcategories.sample(1).iloc[0]
    subcat_ids_for_prod.append(random_subcat['SubCategoryID'])
    suffix = np.random.choice(suffixes)
    product_names.append(f"{random_subcat['SubCategoryName']} {suffix} (SKU-{i+100})")

products = pd.DataFrame({
    'ProductID': range(1001, 1001 + n_prod),
    'ProductName': product_names,
    'SubCategoryID': subcat_ids_for_prod,
    'Price_USD': np.round(np.random.uniform(99.0, 2999.0, n_prod), 2) # Giá USD
})
products.to_csv('Products_2.csv', index=False)

# 4. Countries (11 nước Đông Nam Á)
sea_countries = [
    'Vietnam', 'Thailand', 'Indonesia', 'Malaysia', 'Singapore', 
    'Philippines', 'Myanmar', 'Cambodia', 'Laos', 'Brunei', 'Timor-Leste'
]
countries = pd.DataFrame({
    'CountryID': range(1, 12),
    'CountryName': sea_countries
})
countries.to_csv('Countries_2.csv', index=False)

# 5. States (Các thành phố/tỉnh)
states_data = [
    (1, 'Hanoi'), (1, 'Ho Chi Minh City'), (1, 'Da Nang'),
    (2, 'Bangkok'), (2, 'Chiang Mai'), (2, 'Phuket'),
    (3, 'Jakarta'), (3, 'Bali'), (3, 'Surabaya'),
    (4, 'Kuala Lumpur'), (4, 'Penang'), (4, 'Johor Bahru'),
    (5, 'Singapore'), 
    (6, 'Metro Manila'), (6, 'Cebu'), (6, 'Davao'),
    (7, 'Yangon'), (7, 'Mandalay'),
    (8, 'Phnom Penh'), (8, 'Siem Reap'),
    (9, 'Vientiane'), (9, 'Luang Prabang'),
    (10, 'Bandar Seri Begawan'),
    (11, 'Dili')
]
states = pd.DataFrame(states_data, columns=['CountryID', 'StateName'])
states.insert(0, 'StateID', range(1, len(states) + 1))
states.to_csv('States_2.csv', index=False)

# 6. Sales Data (Thêm CustomerName tiếng Anh và TotalAmount_USD)
n_sales = 1800

# Bộ từ điển tên tiếng Anh ngẫu nhiên
first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']

# Lấy ngẫu nhiên các trường
product_ids_sales = np.random.randint(1001, 1001 + n_prod, n_sales)
quantities = np.random.randint(1, 5, n_sales)
customer_names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(n_sales)]

# Map giá từ bảng Products sang để tính tổng tiền (Total Amount)
price_dict = dict(zip(products['ProductID'], products['Price_USD']))
prices_for_sales = [price_dict[pid] for pid in product_ids_sales]
total_amounts = np.round(np.array(prices_for_sales) * np.array(quantities), 2)

sales = pd.DataFrame({
    'SaleID': range(1, n_sales + 1),
    'CustomerName': customer_names,
    'ProductID': product_ids_sales,
    'StateID': np.random.randint(1, len(states) + 1, n_sales),
    'Quantity': quantities,
    'TotalAmount_USD': total_amounts, # Đã tính sẵn tổng tiền
    'Date': pd.date_range(start='2025-01-01', periods=n_sales, freq='h').strftime('%Y-%m-%d %H:%M:%S')
})
sales.to_csv('sales_data_2.csv', index=False)

print("Đã tạo xong dữ liệu! Có sẵn Tên khách hàng (EN) và Tổng tiền (USD).")