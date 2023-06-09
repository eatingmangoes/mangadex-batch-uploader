A very simple script to batch upload chapters to mangadex using python.

Update lines 8,9,17,19,23
If using a mac, edit line 33 and 36

Optional : If there's a volume number, change None to the volume number in line 39

have the chapters in the directory with the folder names being the chapter number. eg: 73 and 74 are the chapter numbers

```.
├── batchuploader.py
└── Directory_in_line_25
    ├── 73
    │   ├── 001.png
    │   ├── 002.jpg
    │   ├── 003.jpg
    │   ├── 004.jpg
    │   ├── 005.jpg
    │   ├── 006.jpg
    │   ├── 007.jpg
    │   ├── 008.jpg
    │   ├── 009.jpg
    │   ├── 010.jpg
    │   ├── 011.jpg
    │   ├── 012.jpg
    │   ├── 013.jpg
    │   ├── 014.jpg
    │   ├── 015.png
    │   └── 016.png
    └── 74
        ├── 001.png
        ├── 002.jpg
        ├── 003.jpg
        ├── 004.jpg
        ├── 005.jpg
        ├── 006.jpg
        ├── 007.jpg
        ├── 008.jpg
        ├── 009.jpg
        ├── 010.jpg
        ├── 011.jpg
        ├── 012.jpg
        ├── 013.jpg
        ├── 014.png
        └── 015.png
 ```
Changelog:
09/06/2023 : Added Auto image slicing for long webtoons.