 DataMining_841447/
│
├── README.md                     # Giới thiệu môn học, cách chạy, ghi chú
├── requirements.txt              # Danh sách thư viện: pandas, numpy, sklearn, mlxtend,...
├── .gitignore                    # Bỏ qua data lớn, file tạm, venv,...
│
├── data/                         # Toàn bộ dữ liệu (KHÔNG sửa file gốc)
│   ├── raw/                      # Dữ liệu gốc tải về (giữ nguyên)
│   │   ├── covid-data.csv
│   │   ├── marketing_campaign.csv
│   │   ├── red_wine_quality.csv
│   │   ├── pima_indians_diabetes.csv
│   │   ├── amsterdam_house_prices.csv
│   │   ├── penguins_size.csv
│   │   ├── titanic.csv
│   │   ├── credit_card_default.csv
│   │   ├── spam.csv
│   │   ├── mushroom.csv
│   │   ├── mall_customers.csv
│   │   ├── iris.csv
│   │   ├── wine_data.csv
│   │   ├── Online Retail.xlsx
│   │   └── ml-100k/              # MovieLens 100K
│   ├── interim/                  # Dữ liệu đang xử lý dở
│   └── processed/                # Dữ liệu đã làm sạch, sẵn sàng mô hình
│
├── notebooks/                    # Jupyter Notebook theo từng chương
│   ├── 01_EDA/
│   │   ├── 01_01_thong_ke_mo_ta.ipynb
│   │   ├── 01_02_truc_quan_hoa.ipynb
│   │   ├── 01_03_don_bien_va_hai_bien.ipynb
│   │   └── 01_04_bai_tap_ve_nha.ipynb
│   ├── 02_Classification/
│   │   ├── 02_01_decision_tree_random_forest.ipynb
│   │   ├── 02_02_svm.ipynb
│   │   └── 02_03_naive_bayes.ipynb
│   ├── 03_Clustering/
│   │   ├── 03_01_kmeans.ipynb
│   │   └── 03_02_hierarchical.ipynb
│   └── 04_AssociationRules/
│       ├── 04_01_apriori.ipynb
│       └── 04_02_association_rules.ipynb
│
├── src/                          # Hàm dùng chung, tái sử dụng
│   ├── data_utils.py             # Đọc, làm sạch, chia train/test
│   ├── eda_utils.py              # Vẽ histogram, boxplot, scatter,...
│   ├── classification_utils.py   # Đánh giá mô hình, confusion matrix, ROC
│   ├── clustering_utils.py       # Elbow, Silhouette, dendrogram
│   └── association_utils.py      # Support, confidence, lift, vẽ rules
│
├── models/                       # Lưu mô hình đã huấn luyện (.pkl, .joblib)
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   ├── svm.pkl
│   └── kmeans.pkl
│
├── reports/                      # Kết quả, biểu đồ, báo cáo
│   ├── figures/
│   │   ├── eda/
│   │   ├── classification/
│   │   ├── clustering/
│   │   └── association/
│   └── final_report.md
│
└── references/                   # Tài liệu môn học, slide, PDF, link
    ├── Chap01-020P-Introduction.pptx
    ├── PHUOCNT_DM_LAB.pdf
    └── other_papers.pdf
