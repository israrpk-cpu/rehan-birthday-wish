# Rehan Birthday Wish Project

This repository contains multiple versions of a birthday wish for Rehan:

- Python desktop version with a nice UI, optional music, and optional photo support.
- Modern web version in HTML/CSS/JS with fireworks and glowing effects.

## Files

- `birthday_rehan.py` – Python desktop app
- `web/index.html` – web birthday page
- `web/style.css` – styling for the web version
- `web/script.js` – fireworks animation and interaction
- `assets/README.md` – where to place a photo and optional music file

## Run the Python version

```bash
python birthday_rehan.py
```

Optional file support:

- Add a profile picture as `assets/rehan.jpg` or `assets/rehan.png`
- Add a birthday song as `assets/rehan_birthday_song.mp3` or `assets/song.mp3`

## Run the web version

Open `web/index.html` in a browser, or serve the folder locally:

```bash
cd web
python -m http.server 8000
```

Then visit: `http://localhost:8000`

## Birthday message included

The app includes the birthday wishes you provided for Rehan, with a warm and cheerful design.
