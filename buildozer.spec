[app]
title = IncidentApp
package.name = incidentapp
package.domain = org.yourdomain
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy==2.3.1,requests
orientation = portrait
version = 1.0.0

[buildozer]
log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin

[android]
android.api = 31
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
fullscreen = 0
android.accept_sdk_license = True
android.skip_update = True
#android.sdk_path = $HOME/android-sdk
#android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r21d

