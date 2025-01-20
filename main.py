import json
import libs as lib
try:
    import eel
except ImportError:
    print("[MAIN/Err]: py \n Eel not installed: try enter in cmd `pip install eel`")
    exit(0)
import os

n = int(input("Change theme? <1/0> "))

pyprogrampath = os.path.join(os.environ.get('PYPROGRAMPATH'))


if not os.path.exists('cache.json'):
    with open('cache.json', 'w') as f:
        json.dump({
            "mod_list": [{"id": "std", "version": "1.0(1)"}],
            "is_dark": 0,
            "edition": "vanilla",
            "dependencies": [{"id": "launcher", "version": "2025.01"}]
        }, f, indent=4)
try:
    with open('cache.json', 'r') as file:
        cache = json.load(file)

    if n == 1:
        dark_mode = int(input("Write dark mode: 1 or 0: "))
    else:
        dark_mode = cache["is_dark"]

    cache["is_dark"] = dark_mode

    with open('cache.json', 'w') as f:
        json.dump(cache, f)

    with open('cache.json', 'r') as file:
        cache = json.load(file)
    app_package = (('files/script', 'main'), ('files/lib', 'lib'), ('pack/version', '1.0(1)'), ('pack/name', 'py'), ('pack/id', 'py'), ('pack/format', 1))
    if not (cache["is_dark"] == 1):
        eel.init(pyprogrampath); eel.start("/resources/index.html", size=(700, 700))
    else:
        eel.init(pyprogrampath); eel.start("/resources/dark/index.html", size=(700, 700))
except:
    print("Try remove `cache.json`")
    exit(1)






lib.Math.sum(1, 2, 3)