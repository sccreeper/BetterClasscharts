#Used to pull licenses from GitHub during build.

import requests

from src.util import write_file

#Variables

LICENSE_FILE = "src/res/licenses.txt"

LICENSES = [

    ["Python for Android", "https://raw.githubusercontent.com/kivy/python-for-android/develop/LICENSE"],
    ["pyjnius", "https://raw.githubusercontent.com/kivy/pyjnius/master/LICENSE"],
    ["Kivy", "https://raw.githubusercontent.com/kivy/kivy/master/LICENSE"],
    ["KivyMD", "https://raw.githubusercontent.com/kivymd/KivyMD/master/LICENSE"],
    ["requests", "https://raw.githubusercontent.com/psf/requests/main/LICENSE"],
    ["Python", "https://raw.githubusercontent.com/python/cpython/main/LICENSE"]

]

license_string = ""
count = 1

#Code

print(f"Downloading {len(LICENSES)} license(s)...")

for l in LICENSES:

    print(f"Pulling {count}/{len(LICENSES)}")

    text = f"""

    -----------------
    {l[0]}
    -----------------

    """

    text += "\n" + requests.get(l[1]).text

    license_string += "\n" + text

    count += 1

write_file(LICENSE_FILE, license_string)

print("Complete!")
