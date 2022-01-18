# Better ClassCharts <!-- omit in toc -->

**Contents**


- [Information](#information)
- [Supported Platforms](#supported-platforms)
- [Building](#building)
- [Notes](#notes)

## Information

**What is this?**

A alternative to the ClassCharts mobile app.

**Why did I do it?**

Originally started as a joke to add dark theme to the original app, then turned into an excuse to reverse engineer an API and use Kivy on Android.

**What libraries were used in the making of it?**

- [classcharts.py](https://github.com/NCPlayz/classcharts.py) - Helped with reverse engineering the API and making the client.
- [The Kivy Project](https://github.com/kivy) - Very useful crossplatform UI + API library.
- [KivyMD](https://github.com/kivymd/KivyMD/) - Provides most of the UI widgets used in the app.
- [requests](https://github.com/psf/requests) - The backbone of the API client.

## Supported Platforms

- Linux
- Android - **Intended platform**
- Windows (in theory not tested)
- Mac (in theory not tested)

## Building

These are the instructions for building for Android. 

For other platforms see the [Kivy docs](https://kivy.org/doc/stable/guide/packaging.html).

**Requirements**
- Ubuntu 20.04 or later<sup>1</sup>
- A phone running Android 5.0 or later
- Python 3.9<sup>2</sup>

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

Compile the app and deploy it.<sup>3</sup>
```
buildozer android debug deploy run
```

## Notes

<sup>1</sup>Any system that uses the `apt` package manager should work.

<sup>2</sup>Until [this](https://github.com/kivy/kivy/issues/7747) issue is fixed.

<sup>3</sup>For a release build, replace `debug` with `release`
