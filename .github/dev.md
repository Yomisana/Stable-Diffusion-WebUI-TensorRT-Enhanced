# 檔案表查詢
- trt.py
> Hello world!
- ui_trt
  - 引用 model_helper
  - 引用 exporter
  - 引用 model_manager
  - 引用 datastructures
- utilities
  - 就只有被 trt.py 引用
- model_manager
  - 引用了 datastructures
- datastructures
  - 就只有被 trt.py 引用
- scripts/lora
  - 就只有被 trt.py 引用
# 流程
1. stable diffusion webui 載入 install.py
2. stable diffusion webui 載入 scripts/ 下的所有檔案
3. scripts/trt.py 再去加載其他檔案
    - ui_trt
      - 引用 model_helper
      - 引用 exporter
      - 引用 model_manager
      - 引用 datastructures
    - utilities
      - 就只有被 trt.py 引用
    - model_manager
      - 引用了 datastructures
    - datastructures
      - 就只有被 trt.py 引用
    - scripts/lora
      - 就只有被 trt.py 引用
4. scripts/trigger.py 僅嘗試引用 lib.py 測試

# support forge 需要注意的問題
> forge 為何不能使用的問題...
1. 匯出 checkpoint 檔案? 
2. 匯出 lora 檔案?
3. 讀取 checkpoint 檔案並且輸出圖片? 可以但是從 automatic1111 匯出的
4. 讀取 lora 檔案並且輸出圖片?