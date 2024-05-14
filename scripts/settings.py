import modules.scripts as scripts
import gradio as gr
import os

from modules import shared
from modules import script_callbacks

def on_ui_settings():
    exporter = ('tensorrt_enhanced_exporter', "Exporter")
    rtdebug = ('tensorrt_enhanced_debug', "TensorRT Debug")
    from modules.options import categories
    # 註冊分類
    categories.register_category("tensorrt_enhanced", "TensorRT Enhanced")
    cat_id = "tensorrt_enhanced"
    # 選項
    # Exporter Options
    shared.opts.add_option(
        "self_check_update",
        shared.OptionInfo(
            True,
            "Enable self check update",
            section=exporter,
            **({'category_id': cat_id})
        ).info("Disable this option it will not check the update of the TensorRT Enhanced Plugin")
    )

script_callbacks.on_ui_settings(on_ui_settings)