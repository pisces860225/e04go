import argparse
from pathlib import Path


def create_app(name: str = "."):
    """
    創建一個新的 FastAPI 應用程式結構，使用 MTV 模式 (Model-Template-View)。

    :param name: [str] 應用程式的名稱。如果為 '.'，將在當前目錄下創建 'app' 資料夾。否則，會在指定的目錄下建立 'app' 目錄結構。
    """

    if name == ".":
        base_path = Path(".") / "app"
    else:
        base_path = Path(name) / "app"

    # Create base app directory
    base_path.mkdir(parents=True, exist_ok=True)

    # Creating subdirectories
    (base_path / "models").mkdir(exist_ok=True)
    (base_path / "views").mkdir(exist_ok=True)
    (base_path / "templates").mkdir(exist_ok=True)

    # Creating main.py file
    with open(base_path / "main.py", "w") as f:
        f.write(
            f"""
from fastapi import FastAPI

app = FastAPI()

# Import views
from .views import home

@app.get("/")
def read_root():
    return {{"message": "Hello, FastAPI"}}
        """
        )

    # Creating a sample view
    with open(base_path / "views/home.py", "w") as f:
        f.write(
            """
from fastapi import APIRouter

router = APIRouter()

@router.get("/home")
def home_page():
    return {"message": "This is the home page"}
        """
        )

    # Creating a sample model
    with open(base_path / "models/user.py", "w") as f:
        f.write(
            """
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
        """
        )

    # Creating a sample template (for future HTML rendering)
    with open(base_path / "templates/home.html", "w") as f:
        f.write(
            """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
        """
        )

    print(f"FastAPI MTV project created at '{base_path}'!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="管理 FastAPI 項目的工具，支援 MTV 架構生成"
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=".",
        help="應用程式的名稱。如果為 '.'，將在當前目錄下創建 'app' 資料夾。",
    )

    args = parser.parse_args()
    create_app(args.name)
