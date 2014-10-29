Battleship is based on kivy framework.

Is based on kivy framework: http://kivy.org

## Build

Build application in release mode:

    $ buildozer android release

Add your digest:

    $ jarsigner -keystore <gplay_code file> bin/Battleship-<version>-release-unsigned.apk <Your name>

And optimaze it:

    $ zipalign 4 bin/Battleship-<version>-release-unsigned.apk  bin/Battleship-<version>.apk
