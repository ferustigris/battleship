Battleship is based on kivy framework.

Is based on kivy framework: http://kivy.org

## Build

Build application in release mode:

    $ buildozer android release

Add your digest:

    $ jarsigner -keystore ~/Dropbox/gplay_code bin/Battleship-0.0.2-release-unsigned.apk ferus.tigris

And optimaze it:

    $ zipalign 4 bin/Battleship-0.0.2-release-unsigned.apk  bin/Battleship-0.0.2-release.apk
