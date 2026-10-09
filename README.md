# Ahmed Tolan's student hub

Lab materials for the first semester of 2026/2027.

**Student link:** https://ahmedtolan2019.github.io/student-hub/

- [DSA](https://ahmedtolan2019.github.io/student-hub/dsa/): weeks 1 and 2
- [ECE122](https://ahmedtolan2019.github.io/student-hub/ece122/): week 1
- [GEN241](https://ahmedtolan2019.github.io/student-hub/gen241/): weeks 1, 2 and 3

Students can open slides, guides and sheets online, download individual formats,
or download a week or whole course as a ZIP. Extract a ZIP and keep its files
together. HTML contains the interactive activities. PDFs are included where already
available. DSA Week 2 includes starter files, individually and as a ZIP.

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
