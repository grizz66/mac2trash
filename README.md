# mac2trash 🗑️

**Un-Apple your files.**  
Because your Linux friends are tired of `.DS_Store`.

mac2trash is a command-line tool that removes Apple-specific metadata and junk files from folders and zip archives.

---

## 🚀 Installation

Clone the repo and install with pip:

```bash
git clone https://github.com/grizz66/mac2trash
cd mac2trash
pip install .
```

---

## 🛠️ Usage

Clean up a directory:

```bash
mac2trash my-folder/
```

Clean up a zip archive:

```bash
mac2trash archive.zip
```

You'll get a cleaned directory or a new zip file like `archive_clean.zip`.

---

## 🧼 What It Removes

- `.DS_Store`
- `__MACOSX/`
- `._*` AppleDouble files
- `Icon\r`, `.VolumeIcon.icns`
- `.fseventsd`, `.Spotlight-V100`
- Other Finder and metadata trash

---

## 📀 Why Use It?

Because zip files from macOS don't need to smell like macOS.  
Because `.DS_Store` is not your cross-platform friend.  
Because `__MACOSX` deserves the incinerator.

---

## 🧠 More Info

For more tips, snark, and Mac workarounds, visit [macintrash.org](https://macintrash.org)

Pull requests and issues welcome. Unless you're trying to defend `.DS_Store`.

---

🧑‍💻 Brought to life with a few keystrokes and a lot of snark by [Troy](https://github.com/grizz66),  
with technical assistance (and fancy icons) from ChatGPT.

© 2025 [macintrash.org](https://macintrash.org)
