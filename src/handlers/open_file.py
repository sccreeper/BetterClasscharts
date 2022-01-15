from kivy.utils import platform

import requests, os, threading

import globals

def open_file(tile, attachment_url, homework_id, attachment_name):
    
    #Files stored in apps data directory, for caching.

    #Start the progress bar
    tile.children[0].children[0].children[0].opacity = 1
    tile.children[0].children[0].children[0].start()

    #Backwards compatibility
    if not os.path.exists(os.path.join(globals.CONFIG_PATH, "homework_downloads")):
        os.mkdir(os.path.join(globals.CONFIG_PATH, "homework_downloads"))
    
    #Make a directory for the homework id
    if not os.path.exists(os.path.join(globals.CONFIG_PATH, "homework_downloads", str(homework_id))): #If not exists if we have already downloaded another attachment from the same piece of homework.
        os.mkdir(os.path.join(globals.CONFIG_PATH, "homework_downloads", str(homework_id)))
    
    threading.Thread(target=download_file, args=(attachment_url, os.path.join(globals.CONFIG_PATH, "homework_downloads", str(homework_id), attachment_name), tile, )).start()

    #download_file(attachment_url, os.path.join(globals.CONFIG_PATH, "homework_downloads", str(homework_id), attachment_name))


#Modifed from: https://stackoverflow.com/a/16696317
def download_file(url, filename, tile):
    
    local_filename = filename
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    

    tile.children[0].children[0].children[0].stop()
    tile.children[0].children[0].children[0].opacity = 0

    #Open file in preferred app. Modified from: https://stackoverflow.com/a/435669
    
    if platform == 'macosx': # macOS
        import subprocess 
        subprocess.call(('open', filename))
    elif platform == 'win':    # Windows
        import subprocess

        os.startfile(filename)
    elif platform == 'linux': # linux variants
        import subprocess

        subprocess.call(('xdg-open', filename))
    else: #android
        pass