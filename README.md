# ms-word-chinese-translator
Translate a Microsoft Word file between Simplify Chinese and Traditional Chinese

## How to use
1. Upload target MS Word doc
2. Choose translating direction
3. Open output Word doc and resave

~~Note: It is normal to see the following message on the first time openning the output doc. Select `Yes` and save it again will resolve the issue.~~ Fixed by using python-docx library

## How to generate executable file
1. Update `pathex` to project root in `pyinstaller_bundle.spec` (line 6)
2. Run `pyinstaller pyinstaller_bundle.spec` from project root