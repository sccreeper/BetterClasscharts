#Modifed from: https://github.com/kivy/python-for-android/issues/846#issuecomment-252922667

from kivy.utils import platform
import webbrowser

if platform == 'android':
    from jinus import autoclass, cast

def launch_webbrowser(instance, url):
    
    if platform == 'android':
        
        def open_url(url):
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            browserIntent = Intent()
            browserIntent.setAction(Intent.ACTION_VIEW)
            browserIntent.setData(Uri.parse(url))
            currentActivity = cast('android.app.Activity', activity)
            currentActivity.startActivity(browserIntent)

        # Web browser support.
        class AndroidBrowser(object):
            def open(self, url, new=0, autoraise=True):
                open_url(url)
            def open_new(self, url):
                open_url(url)
            def open_new_tab(self, url):
                open_url(url)

        webbrowser.register('android', AndroidBrowser, None, -1)
    

    webbrowser.open(url)

