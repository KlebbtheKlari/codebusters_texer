# codebusters-texer

Tool to convert spreadsheet ([Template](https://docs.google.com/spreadsheets/d/1U-BpeRaxML1Sr2uRb8K0Zhr_6DGR3GwrMdIgSoa-3ac/edit?usp=sharing)) w/ questions to TeX for Codebusters.

To be used with this ([LaTeX Template](https://www.overleaf.com/read/rmkbhrwjkbht#18a3f8))[^1]. Make a copy!

Current usage[^2]:
1. Download sheet as `main.csv`
2. Upload `main.csv` to `/src` folder
3. Run `main.py`
4. Output will be in a file called `out.tex`
5. Copy-paste `out.tex` to `out.tex` in the Overleaf template
6. Move the timed question to `main.tex` just before the `\begin{questions}`
7. Copy and paste the answer key output `key.tex` to `key.tex` in the Overleaf template
8. Edit whatever you need to on the TeX template. Good luck!

[^1]: The TeX template may be fully here on Git in the future
[^2]: I will probably move this to cmd line in the future but this is easier for me to test with rn idk
