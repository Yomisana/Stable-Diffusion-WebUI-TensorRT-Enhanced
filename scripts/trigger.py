from lib import detect_webui_version, clean_pycache

# get webui version
webui_version = detect_webui_version()
print(f"[TensorRT Enhanced] WebUI version: {webui_version}")
# clean this extension inside whole __pycache__ folder
clean_pycache()

####################
# This is Yomisana create custom trigger script
# Right now are just test are get trigger and try detect webui version
####################