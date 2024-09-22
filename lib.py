import os
import shutil
from modules import scripts

def detect_webui_version():
    """
    檢測當前 WebUI 版本，通過檢查當前工作目錄下是否存在特定的子目錄。
    
    Returns:
        str: 返回 'forge' 或 'automatic'
    """
    if os.path.exists(os.path.join(os.getcwd(), 'modules_forge')):
        return 'forge'
    else:
        return 'automatic'


def clean_pycache():
    print("[TensorRT Enhanced] Cleaning __pycache__ folder...")
    """
    遞迴地刪除指定目錄下所有名為 `__pycache__` 的資料夾。
    
    Args:
        base_dir (str): 基本目錄的路徑
    """
    for root, dirs, files in os.walk(scripts.basedir()):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                print(f"Deleting: {dir_path}")
                shutil.rmtree(dir_path)
    print("[TensorRT Enhanced] Cleaned __pycache__ folder.")