name: ساخت APK

on:
  push:
  workflow_dispatch:

jobs:
  build-android:
    runs-on: ubuntu-latest
    steps:
      - name: گرفتن کدها
        uses: actions/checkout@v3

      - name: ساخت با Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        id: buildozer
        with:
          command: buildozer android debug
          workdir: .

      - name: آپلود APK
        uses: actions/upload-artifact@v4
        with:
          name: my-pdf-app
          path: bin/*.apk
