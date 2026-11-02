# meng-ke.github.io v2

Static GitHub Pages package for Mengke Zhao's academic website. No build system is required: the site is plain HTML/CSS/JS.

## Pages

- `index.html` — homepage and six featured research programs
- `research.html` — expanded research stories
- `publications.html` — 2022–present papers where Mengke Zhao is among the first three authors
- `software.html` — software and method packages

## Local assets

### Portrait

The personal portrait is stored at:

`assets/images/mengke-zhao.jpg`

To update the portrait later, replace that file while keeping the same filename. A vertical 4:5 crop works best.

### CV

The current CV is stored at:

`assets/cv/Mengke_Zhao_CV.pdf`

All CV buttons across the site point to this path. To update the CV, replace the PDF while keeping the same filename.

### Paper figures

The six featured research figures are stored locally in:

`assets/images/papers/`

Expected filenames:

- `scaleaware-jepa-mhd-fig1.png`
- `scale-aware-xai-fig1.png`
- `volume-density-mapper-fig1.png`
- `unified-mhd-fig2a.png`
- `multi-fractal-orion-a-fig1.png`
- `scale-vector-alignment-fig1.png`

These are the publication figures currently used by the website. There is no figure-download setup step.

## Release check

Run:

```bash
python3 scripts/check_links.py
```

Then open `index.html`, `research.html`, `publications.html`, and `software.html` locally to inspect the layout.

## Deploying to GitHub Pages

1. Preserve any existing `CNAME` or repository-specific settings from the current `meng-ke.github.io` repository.
2. Copy these files into the publishing branch/repository root.
3. Commit and push.

The `.gitignore` excludes common macOS metadata files.

## Contact used on the site

- `mkzhao@nju.edu.cn`
- `mkzhao628@gmail.com`
- GitHub: https://github.com/meng-ke
- alphaXiv: https://www.alphaxiv.org/zh/@mengke-zhao
- Google Scholar: https://scholar.google.com/citations?user=EH9KucEAAAAJ
- ORCID: https://orcid.org/0000-0003-0596-6608
