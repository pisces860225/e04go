from setuptools import setup, find_packages

setup(
    name="e04go",  # 專案名稱
    version="0.0.1.003",  # 版本號
    packages=find_packages(where="app"),  # 找到 app 資料夾中的所有包
    package_dir={"": "app"},  # 設定包目錄為 app
    include_package_data=True,  # 包含包中的非 Python 文件
    description="一個基於 FastAPI 的 MTV 架構生成器",  # 簡短描述
    long_description=open("README.md").read(),  # 從 README.md 中讀取長描述
    long_description_content_type="text/markdown",  # README.md 的格式
    author="QQ",
    author_email="jeremy55688@icloud.com",
    url="https://github.com/pisces860225/e04go",  # GitHub 地址
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "fastapi",
        "uvicorn",
        "jinja2",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "e04go=e04go.E04master:main",  # 指向 app.E04master
        ],
    },
    python_requires=">=3.11",  # Python 版本要求
)
