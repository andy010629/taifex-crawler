# Taifex Data Downloader

這個專案提供了一個 Python 腳本，用於下載台灣期貨交易所（Taifex）的每日期貨及選擇權資料，並將其解壓縮到指定的資料夾中。

## 目錄

- [需求](#需求)
- [安裝](#安裝)
- [使用方法](#使用方法)
- [文件結構](#文件結構)
- [注意事項](#注意事項)

## 需求

在運行此腳本之前，您需要安裝以下 Python 套件：

- `requests`
- `beautifulsoup4`
- `lxml`
- `wget`

您可以使用以下命令安裝這些套件：

```bash
pip install requests beautifulsoup4 lxml wget
```

## 安裝

1. 克隆此專案到本地端：

    ```bash
    git clone https://github.com/yourusername/taifex-data-downloader.git
    ```

2. 切換到專案目錄：

    ```bash
    cd taifex-data-downloader
    ```

3. 安裝需求套件：

    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

您可以通過運行 `main.py` 來下載和解壓縮最新的期貨及選擇權數據：

```bash
python crawler.py
```

腳本將自動下載最近 30 天的期貨與選擇權資料並將其解壓縮到 `DailyFuturesCSV` 和 `DailyOptionsCSV` 資料夾中。

### 函數說明

- `zip_extract(file_path, path)`: 解壓縮 ZIP 檔案至指定路徑。
- `get_daily_futures()`: 下載並解壓縮最近 30 天的期貨資料。
- `get_daily_options()`: 下載並解壓縮最近 30 天的選擇權資料。

## 文件結構

```plaintext
taifex-data-downloader/
├── main.py          # 主要的 Python 腳本
├── requirements.txt # 需求套件列表
└── README.md        # 專案說明文件
```

## 注意事項

- 請確保有穩定的網路連線以下載數據。
- 若目錄中已存在下載的 ZIP 檔案，將會覆蓋舊的檔案。
- 資料下載後將自動解壓縮並刪除 ZIP 檔案。
