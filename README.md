# NotShitClassCharts

A ~~replacement~~ alternative to the ClassCharts mobile app which isnt' complete crap.

## Building

**Requirements**
- Ubuntu 20.04 or later
- A phone running Android 5.0 or later
- Python 3

**Steps**

Install [Buildozer](https://github.com/kivy/buildozer)
```
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
cd ..
```

Clone the source from GitHub.

```
git clone https://github.com/sccreeper/ClasschartsApp.git
```

Install the project requirements

```
cd ClasschartsApp
pip install -r requirements.txt
```

Plug the phone into the computer and enable USB debugging.

Compile the app and deploy it.<sup>1</sup>
```
buildozer android debug deploy run
```

**Notes**

<sup>1</sup>For a release build, replace `debug` with `release`

## Credits

- [classcharts.py](https://github.com/NCPlayz/classcharts.py) - Helped a lot with making the API client.
- Kivy - Very useful crossplatform API library.
- KivyMD - Provides most of the UI widgets used in the app.