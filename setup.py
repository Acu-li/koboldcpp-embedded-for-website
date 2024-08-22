from setuptools import setup

APP = ['koboldcpp.py']
DATA_FILES = [
    'koboldcpp_default.so',
    'kcpp_adapters',
    'klite.embd',
    'kcpp_docs.embd',
    'kcpp_sdui.embd',
    'taesd.embd',
    'taesd_xl.embd',
    'rwkv_vocab.embd',
    'rwkv_world_vocab.embd'
]
OPTIONS = {
    'argv_emulation': True,
    'includes': ['customtkinter', 'psutil'],
    'packages': [],
    'plist': {
        'CFBundleName': 'Koboldcpp',
        'CFBundleDisplayName': 'Koboldcpp',
        'CFBundleIdentifier': 'com.yourdomain.koboldcpp',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
