# Ahmed Tolan's student hub

Lab materials for the first semester of 2026/2027.

**Student link:** https://ahmedtolan2019.github.io/student-hub/

- [DSA](https://ahmedtolan2019.github.io/student-hub/dsa/): weeks 1, 2 and 3
- [ECE122](https://ahmedtolan2019.github.io/student-hub/ece122/): weeks 1, 2 and 3
- [GEN241](https://ahmedtolan2019.github.io/student-hub/gen241/): weeks 1–5

Students can open slides, guides and sheets online, download individual formats,
or download a week or whole course as a ZIP. Extract a ZIP and keep its files
together. HTML contains the interactive activities. PDFs are included where already
available. DSA Week 2 includes starter files, individually and as a ZIP.

DSA Week 3 uses one interactive whiteboard as the lesson and practice guide. In the
offline classroom, students create one Python file and type the displayed code and
tests; no ZIP or supplied files are required. The downloadable kit is for later review.
Its reviewed eleven-file bundle contains the whiteboard, a minimal Python readiness
check, setup instructions, worked Python examples and incomplete practice tasks. The week/course ZIPs
keep `code/` and `practice/` beside the HTML so the links work offline. There
is no separate Week 3 sheet. Private presenter notes, solutions, book sources
and QA files are excluded. The existing DSA course link stays the same.

## Update the student link

This phrase means: publish the latest completed student materials to this same site.
Keep the existing site, course and week URLs. A request to prepare a lesson alone
does not publish unfinished material. When asked to update the student link, carry
the update through rebuilding, checking, pushing and checking the live deployment.

The site repository sits beside these private teaching folders on the maintainer's machine:

```
2026-2027-1st/
  DSA-data-structures-and-algorithms/
  ECE122-computer-programming-1/
  GEN241-computer-language-and-applications/
  student-hub/
```

1. Finish and verify the relevant week's source materials using its course workflow.
2. Refresh its student exports. DSA Week 1 uses `student/make-deliverables.py`;
   DSA Week 2 uses `build-support.py` and its PDF/package steps; ECE122 uses
   `python3 export-student.py NN`. GEN241 slides are generated directly from the
   current source by this publisher using the same student export conventions;
   refresh its guide PDF using the course exporter if the guide changed.
3. Add a completed new week to `catalog.json`, listing exact student files. Do not
   publish every file found in a course folder. Include the appropriate sheet even
   when two lab weeks share one sheet. Preserve existing destination filenames.
4. From this repository, run:

   ```sh
   python3 scripts/build.py
   python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
   ```

5. Open the changed course in a browser. Check a slide interaction, a guide, a sheet,
   file downloads and the week/course ZIPs. Check a phone viewport after layout edits.
   The build checks local links and ZIP integrity and stops on stale student HTML.
6. Review `git diff --stat` and the publication file list. Commit and push to `main`.
   GitHub Pages publishes `main:/docs`. Wait for the Pages deployment to succeed,
   then verify the changed live course and downloads before reporting completion.

## Publication boundary

`catalog.json` is the explicit source allowlist. The build publishes only those
student files, generated indexes and ZIPs. Never copy whole course folders into
this repository. Instructor solutions, presenter scripts, review notes, source
textbooks, internal plans, recordings and development files are not publication inputs.
Worked examples intentionally present in student slides and guides stay intact.

GEN241 source slides contain a Week 1 textbook button. The publisher omits that
button and never embeds or copies the full textbook. Approved sheet, lecture and
submission-rule PDF buttons remain embedded in the HTML for standalone downloads.
GEN241 presenter timing labels are hidden in the exported student copy.

The original course materials are not modified by the site build. Existing verified
guide PDFs are copied; the publisher does not regenerate their content. Local source
folders are needed only for updates, not for hosting or using the published site.

## Implementation

Each course index is a complete HTML5 file with inline layout styles and SVG icons.
Tailwind CSS 4.3.3 loads from the jsDelivr CDN. The inline styles also cover the layout
when that CDN is unavailable. There is no application framework, database, account
system or analytics. All file formats are exposed as ordinary links and downloads,
and all navigation works without JavaScript. A small inline script highlights the
current week in the sidebar as students scroll. Interactive lesson materials retain
their own scripts.

The hub self-hosts Inter and JetBrains Mono with their OFL licenses in `assets/fonts/`.
The fonts fall back to system fonts. Some older lesson materials request optional web
fonts and fall back to local fonts offline. Edit `assets/style.css` and
`assets/navigation.js` to update the inline layout and week-highlighting script; the
builder embeds them in every index. The course and file URL paths stay unchanged.

The builder uses Python's standard library. ZIP metadata is deterministic, and
`docs/checksums.json` records the SHA-256 of every published file except itself.
Treat `docs/` as generated output and change `assets/`, `catalog.json` or the builder
instead. The public source files are sufficient to maintain the hub layout; the
private teaching folders supply the lesson exports during the maintainer's build.

## Introduction to Basic Computer

The static reference at [computer-basics/](https://ahmedtolan2019.github.io/student-hub/computer-basics/)
is separate from the taught-course catalog. It has a global navigation link and
prominent help cards on ECE122 and GEN241; DSA has no beginner help card. It covers
file basics, folders, copy/move, renaming and extensions, hub downloads, Dev-C++ and
PyCharm saving, Windows/Mac ZIP creation and extraction, optional 7-Zip, and a final
submission check. Instructions use simple Egyptian Arabic with English UI labels.

Edit `scripts/computer_basics.py` for the content and diagrams. Each task has an
anchor, a zoomable SVG illustration, readable steps, and relevant official-source
links. All content works without JavaScript. Illustrations are explicitly labeled
and do not claim to be actual screenshots. `assets/basics/files-and-folders.png` is
an AI-generated overview made for this guide; the build generates the precise SVG
diagrams from authored text. No instructor files are added to the publication
allowlist, and course ZIPs contain the same course materials as before.

When updating this reference, verify Windows/Mac instructions against official
documentation, keep platform differences visible, and verify the guide at desktop
and phone sizes. Existing course file URLs and download behavior must stay intact.

## GEN241 Sheet 2 workbook

Weeks 2 and 3 also link the completed bilingual student workbook. Its reviewed
75-file allowlist is `courses[].workbooks.sheet-02.files` in `catalog.json`,
sourced only from `student-workbooks/sheet-02/public`. The workbook has original
question images, illustrated foundations, student-authorized worked examples,
recorded C++ traces, and local progress/JSON backups. Never add the adjacent
private `review/`, `src/`, `build/`, or instructor preparation folders.

The builder keeps the workbook folder intact in both week ZIPs and the course ZIP,
and generates `downloads/GEN241-sheet-02-Workbook.zip` for a workbook-only download.
The existing slides, guides, PDF and week links stay unchanged.

## ECE122 Sheets 2 and 3

Weeks 2 and 3 publish the completed learning kit using the explicit
`bundles.sheets-02-03.files` allowlist. Its source is only
`ECE122-computer-programming-1/learning-kit/public`. The interactive whiteboard
deck builds questions, comparisons and decisions one step at a time. The Guides
cover all 25 questions with source highlights, visual explanations, plans,
progressive code, recorded execution and independent practice. The original
Lecture 4 handout is included unchanged.

Each week opens its own Guide and original sheet. Both ZIPs keep the complete
kit together so relative links work offline. HTML download actions supply that
ZIP because the Guides need their companion files. The course ZIP includes
both weeks. Existing course, week, Guide and slide URLs are preserved.

The code files under the public kit are the student worked examples linked
from the Guides. Original reference archives, instructor reviews, presenter
notes, authoring scripts and QA records are excluded.

## GEN241 Sheet 3

Week 4 publishes the six-part bilingual whiteboard and a separate complete study
Guide for all ten questions. The Guide includes prerequisite explanations, diagrams,
five-line plans, practice with feedback, reference code and recorded outputs.
The programs were built and checked on macOS with Apple Clang in C++98 mode.
C++ blocks include syntax colors and step-based line focus; the loop trace and
pentagon visit marker move with the learner’s navigation. The Guide explains the
supplied reference methods, including nested loops and equivalent alternatives.

The six-file allowlist is `courses[].bundles.sheet-03.files`, sourced only from
`GEN241-computer-language-and-applications/week-04-loops/student`. Original Sheet 3
and Lecture 5 PDFs are included unchanged. The week and course ZIPs keep both HTML
files and PDFs together. Authoring files, compiler binaries, QA reports and private
execution records are excluded. Existing week and course URLs remain unchanged.

## GEN241 Sheet 4

Week 5 publishes a newly authored single-page question Guide, its printable PDF,
and the unchanged Sheet 4 and Lecture 6 PDFs. Each question has its original image,
background explanation, C++ walkthrough, alternative method, recorded results and
common mistakes. This week has no slide deck. The four-file allowlist is
`courses[].bundles.sheet-04.files`, sourced only from
`GEN241-computer-language-and-applications/week-05-repeating-structures/student`.

The Guide embeds its styles, interactions and question images. Its companion PDF
links work when the week ZIP stays together. The new guide-only format uses a
reviewed Playwright print export because the course's older exporter assumes a
slide deck. Instructor videos, professor solution files, private code and review
notes are excluded. Worked code inside the student Guide is intentionally included.
