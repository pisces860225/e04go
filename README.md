# e04go

## 專案簡介

`e04go` 是一個基於 FastAPI 的 MTV (Model-Template-View) 應用程式生成工具。此工具能幫助你快速生成基於 FastAPI 框架的項目結構，特別適合希望使用 FastAPI 來開發 Web 應用並實現 MVC 或 MTV 架構的開發者。你可以通過命令行使用這個工具來輕鬆建立新的 FastAPI 應用程式。

## 使用的套件

本專案使用了以下主要套件：

- **FastAPI**：高效、現代的 Python Web 框架，用於構建 API 和 Web 應用程式。
- **Uvicorn**：FastAPI 預設使用的 ASGI 伺服器，支持高併發和非同步處理。
- **Jinja2**：Python 模板引擎，用於渲染 HTML 頁面。
- **Pydantic**：提供數據驗證和數據類型管理的 Python 庫，與 FastAPI 深度集成。
- **Argparse**：Python 標準庫中的命令行解析工具，用於解析命令行參數。

### 其他依賴項

- **Python 3.11** 或更高版本。

## 功能內容

- **生成 FastAPI 應用程式結構**：透過命令行工具，快速生成一個具備 MTV 架構的 FastAPI 應用程式，包括模型、視圖和模板。
- **自動化路由設置**：生成應用程式時，自動為你設置好路由和基本的視圖函數，節省開發時間。
- **支持 Jinja2 模板引擎**：可以直接生成並使用 Jinja2 模板來渲染 HTML 頁面，方便開發者進行前端和後端的快速集成。

## 安裝與部屬教學

### 安裝

你可以通過 PyPI 安裝 `e04go`：

```bash
pip install e04go
```
安裝完成後，你可以使用 e04go 命令來生成新的 FastAPI 應用程式。

## 使用範例

生成一個新的 FastAPI 應用程式：

```bash
e04go create_app my_new_app
```
這將會在當前目錄下生成一個名為 my_new_app 的資料夾，裡面包含 FastAPI 應用程式的基本結構，包括 models/, views/, templates/ 等目錄。

## 生成的專案結構

生成後的 FastAPI 應用程式將會有如下結構：

```bash
my_new_app/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI 主應用程式
│   └── views/
│       └── home.py     # 基本視圖函數
├── models/
│   └── user.py         # 範例數據模型
├── templates/
│   └── home.html       # Jinja2 模板範例
```

生成後的 main.py 文件將會自動包含基本的路由和視圖函數，你可以根據需求進行擴展。

## 啟動應用程式

進入生成的應用程式目錄，並使用 Uvicorn 啟動 FastAPI 應用：

```bash
cd my_new_app
uvicorn app.main:app --reload
```
應用程式將運行在 http://127.0.0.1:8000/，你可以在瀏覽器中查看基本的首頁。

## 自行構建與部屬

如果你希望手動構建與部屬，可以按照以下步驟進行：

1. 克隆此專案至本地：
    ```bash
    git clone https://github.com/pisces860225/e04go.git
    ```
2. 安裝依賴項：
    ```bash
    poetry install
    ```
3. 構建應用：
    ```bash
    poetry build
    ```
4. 部屬至伺服器上，並使用 Uvicorn 啟動 FastAPI：
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## 未來發展與更新

1. 自動化模板生成：增加更多預設模板選項，讓開發者可以選擇不同的前端框架或視圖層實現。
2. 數據庫集成：支持自動生成數據庫模型並配置 ORM 工具。
3. API 文檔生成：增強 API 文檔生成能力，讓開發者能夠快速上手和測試 API。

## 貢獻指南

如果你有興趣參與此專案的開發，歡迎提交 PR 或 issue。在提交 PR 前，請確保你的代碼格式符合項目標準，並通過了所有單元測試。

1. Fork 此專案。
2. 創建分支 (git checkout -b feature/your-feature)。
3. 提交變更 (git commit -m 'Add some feature')。
4. 推送至分支 (git push origin feature/your-feature)。
5. 發送 Pull Request。

## 授權條款

此專案使用 MIT 授權條款。