[app]
title = Minha App
package.name = minhaapp
package.domain = com.exemplo
source.dir = .
source.include_exts = py,png,jpg,mp3,txt,wav,json
version = 1.0.0
requirements = python3,kivy

# Configurações Universais para Android
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
