#!/bin/bash

LICENSE_FILE="src/res/licenses.txt"
BUILD_ID_FILE="src/res/build_id.txt"

declare -a LICENSE_URLS=("https://raw.githubusercontent.com/kivy/python-for-android/develop/LICENSE" "https://raw.githubusercontent.com/kivy/pyjnius/master/LICENSE" "https://raw.githubusercontent.com/kivy/kivy/master/LICENSE" "https://raw.githubusercontent.com/kivymd/KivyMD/master/LICENSE" "https://raw.githubusercontent.com/psf/requests/main/LICENSE" "https://raw.githubusercontent.com/python/cpython/main/LICENSE")
declare -a LICENSE_NAMES=("Python For Android" "pyjnius" "Kivy" "KivyMD" "requests" "Python")


echo -------------------
echo Build ID: $(git log -n 1 --pretty=format:"%H")
echo -------------------

echo $(git log -n 1 --pretty=format:"%H") > ${BUILD_ID_FILE}

echo -------------------
echo Pulling licenses...
echo -------------------

COUNT=0

#Clear license file
echo "" > ${LICENSE_FILE}

for I in "${LICENSE_URLS[@]}" 
do

    echo -en "\r\033[KPulling license $((COUNT+1))/${#LICENSE_URLS[@]}"

    echo -e "\n" >> ${LICENSE_FILE}
    echo -e "-------------\n" >> "${LICENSE_FILE}"
    echo -e "\n" >> ${LICENSE_FILE}
    
    echo -e "${LICENSE_NAMES[$COUNT]}\n" >> "${LICENSE_FILE}"

    echo -e "\n" >> ${LICENSE_FILE}
    echo -e "-------------\n" >> "${LICENSE_FILE}"
    echo -e "\n" >> ${LICENSE_FILE}

    echo "$(curl -s $I)\n" >> "${LICENSE_FILE}"

    ((COUNT++))

done

echo -e "\nDone!"


if [ "$1" == "res" ] 
then

    echo "Skipping APK build..."
    echo "Finished"
    exit
fi

echo -------------------
echo Building APK and deploying...
echo -------------------

if [ "$1" == "debug" ] 
then

    buildozer android debug deploy run

elif [ "$1" == "release" ] 
then

    if [[ ! -e "uber-apk-signer*.apk" ]]; then

        echo "Building release APK..."

        buildozer android release

        echo "Signing the APK(s)..."

        java -jar $(find ./ -name "uber-apk-signer*.jar" -print -quit) --apks ./bin/
    
    else

        echo "Unable to find uber-apk-signer!"
        exit
    fi

else

    echo "Invalid option '$1'"

fi

echo -------------------
echo Finished
echo -------------------
