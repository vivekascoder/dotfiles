
import json
import os

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def get_theme(theme_name: str) -> dict:
	theme_folder = os.path.expanduser("~/.config/qtile/themes/")
	themes = os.listdir(theme_folder)
	if f"{theme_name}.json" in themes:
		with open(os.path.join(theme_folder, f"{theme_name}.json")) as th:
			data = json.load(th)
		return data

	return False
