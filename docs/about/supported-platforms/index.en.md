---
title: Supported Platforms
---

Platforms supported by the latest version of **Naruto Senki: V2**：

| Platform | System Requirements | Tested                    |
| -------- | ------------------- | ------------------------- |
| Android  | Minimum Android 4.4 | Android 12.0              |
| Windows  | 64-bit              | Windows 11 64-bit         |
| Linux    | 64-bit              | Manjaro Linux 5.17 64-bit |
| iOS      | comming soon        |                           |
| macOS    | 64-bit              | macOS 12.1 64-bit         |


!!! hint "Android user"

    `armeabi-v7a` and `arm64-v8a` architectures are supported.

!!! hint "Windows user"

    1. If you don't have any vc redist package installed,
    you should download and install the latest version of `MSVBCRT.AIO`.

        [:material-download: MSVBCRT.AIO](https://ghpym.lanzoui.com/b00ze15ab){ .md-button }

    1. If you already have the old redist package installed,
    you can just download the following packages.

        `For windows 64-bit, it's recommended to install both of the following.`

        [:material-download: vc redist 64-bit](https://aka.ms/vs/17/release/vc_redist.x64.exe){ .md-button }

        [:material-download: vc redist 32-bit](https://aka.ms/vs/17/release/vc_redist.x86.exe){ .md-button }

!!! hint "Linux user"

    requires `gtk3`.

    Maybe some Linux distributions don't use `PulseAudio` to play audio,
    then you should install `PulseAudio` manually.

    If you cannot run the game, please run the command `ldd ./NarutoSenki` in game root directory
    to display all dependencies and install all missing dependencies manually.

!!! hint "iOS user"

    Jailbreak required.
