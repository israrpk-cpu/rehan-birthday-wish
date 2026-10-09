import os
import random
import sys
import tkinter as tk
from tkinter import font

try:
    import pygame
except Exception:
    pygame = None

try:
    from PIL import Image, ImageTk
except Exception:
    Image = None
    ImageTk = None


MESSAGE = """Happy Birthday, Rehan! 🎉🎂

To my best friend, the man who turns ordinary moments into unforgettable memories and makes life way more fun even when nothing is going right — happy birthday, my brother!

You are not just a friend to me, you are a whole comedy show, a mood booster, and my go-to person for laughter, nonsense, and good vibes. Your jokes are so funny that even your silence feels like a punchline. You have that rare gift of making everyone around you smile, even on the worst days. Honestly, life would be boring without you.

May your birthday be full of:
- laughter that makes your stomach hurt,
- cake that tastes better than your excuses,
- surprises that make you smile,
- and memories that stay with you forever.

And now the serious part: May Allah bless you with a long, happy, and successful life. May He give you health, peace, wisdom, and success in every step of your life. May He protect you from every hardship, fill your heart with happiness, and guide you always on the right path. May your dreams come true, your prayers be accepted, and your life be full of barakah.

You deserve all the happiness in the world, Rehan. Keep smiling, keep shining, keep being the amazing person you are, and never stop being yourself — because that is what makes you so special.

Enjoy your day, celebrate like a king, eat like a champion, and don’t forget: growing older is mandatory, but growing wiser and funnier is optional… and you are already winning at both. 😄

Happy Birthday again, Rehan — may your life always be filled with joy, laughter, love, and success. Ameen.

With love and best wishes,
[Your Name]
"""


class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Happy Birthday, Rehan")
        self.root.geometry("1100x860")
        self.root.configure(bg="#130d1d")
        self.root.resizable(False, False)

        self.music_enabled = False
        self.music_handle = None

        self.canvas = tk.Canvas(root, width=1100, height=860, bg="#130d1d", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.confetti = []
        self.load_background()
        self.create_card()
        self.create_photo_frame()
        self.create_message()
        self.create_button()
        self.create_confetti()
        self.animate_confetti()
        self.start_music_if_available()

    def load_background(self):
        for i in range(16):
            color = self.interpolate_color("#120d1b", "#20162f", i / 15)
            self.canvas.create_rectangle(0, i * 55, 1100, (i + 1) * 55 + 10, fill=color, outline="")

    def interpolate_color(self, hex1, hex2, ratio):
        def hex_to_rgb(h):
            h = h.lstrip("#")
            return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

        def rgb_to_hex(rgb):
            return "#" + "".join(f"{max(0, min(255, int(v))):02X}" for v in rgb)

        r1, g1, b1 = hex_to_rgb(hex1)
        r2, g2, b2 = hex_to_rgb(hex2)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        return rgb_to_hex((r, g, b))

    def create_card(self):
        self.canvas.create_oval(120, 70, 260, 205, fill="#ffb703", outline="")
        self.canvas.create_oval(840, 65, 980, 200, fill="#ff7eb6", outline="")
        self.canvas.create_oval(470, 35, 630, 175, fill="#8ecae6", outline="")

        card_x, card_y = 120, 120
        card_w, card_h = 860, 640
        self.card_bg = "#fff8f0"
        self.canvas.create_rectangle(card_x, card_y, card_x + card_w, card_y + card_h,
                                     fill=self.card_bg, outline="", width=0)

        shadow = self.canvas.create_rectangle(card_x + 18, card_y + 18, card_x + card_w + 18, card_y + card_h + 18,
                                              fill="#f4d8ff", outline="")
        self.canvas.tag_lower(shadow)

        title_font = ("Segoe Print", 28, "bold")
        self.canvas.create_text(550, 175, text="Happy Birthday, Rehan! 🎉🎂",
                               fill="#ff4d8d", font=title_font)

        subtitle_font = ("Segoe UI", 13, "italic")
        self.canvas.create_text(550, 210,
                                text="To my best friend, my brother, and my forever smile-maker...",
                                fill="#2d1b38", font=subtitle_font)

    def create_photo_frame(self):
        x0, y0 = 160, 235
        w, h = 180, 180
        self.canvas.create_rectangle(x0 - 8, y0 - 8, x0 + w + 8, y0 + h + 8,
                                     fill="#ffd166", outline="")

        photo_path = self.find_photo_path()
        if photo_path:
            try:
                if Image and ImageTk:
                    img = Image.open(photo_path)
                    img = img.resize((170, 170), Image.Resampling.LANCZOS)
                    img_tk = ImageTk.PhotoImage(img)
                    self.photo_image = img_tk
                    self.canvas.create_image(x0 + 85, y0 + 85, image=img_tk)
                    return
            except Exception:
                pass

        self.canvas.create_text(x0 + 85, y0 + 85, text="Rehan\n🎂", fill="#ff4d8d",
                               font=("Segoe UI", 28, "bold"))

    def find_photo_path(self):
        candidates = [
            "assets/rehan.jpg",
            "assets/rehan.png",
            "assets/rehan.jpeg",
            "assets/rehan.webp",
            "rehan.jpg",
            "rehan.png",
        ]
        for path in candidates:
            if os.path.exists(path):
                return path
        return None

    def create_message(self):
        text_frame_x = 370
        text_frame_y = 250
        text_frame_w = 560
        text_frame_h = 380

        self.canvas.create_rectangle(text_frame_x, text_frame_y, text_frame_x + text_frame_w,
                                     text_frame_y + text_frame_h, fill="#fffaf5", outline="#ffd166", width=2)

        message = tk.Text(self.root, wrap=tk.WORD, bg="#fffaf5", fg="#2d1b38",
                          font=("Segoe UI", 11), bd=0, highlightthickness=0, padx=18, pady=18,
                          width=52, height=16)
        message.insert(tk.END, MESSAGE)
        message.configure(state="disabled")
        message.place(x=text_frame_x + 8, y=text_frame_y + 8, width=text_frame_w - 16, height=text_frame_h - 16)

    def create_button(self):
        self.button = tk.Button(
            self.root,
            text="Celebrate Rehan 🎉",
            font=("Segoe UI", 14, "bold"),
            bg="#ff4d8d",
            fg="white",
            padx=22,
            pady=10,
            bd=0,
            cursor="hand2",
            command=self.trigger_confetti
        )
        self.button.place(x=465, y=685)

    def create_confetti(self):
        for i in range(100):
            x = random.randint(100, 1000)
            y = random.randint(-300, 120)
            s = random.randint(3, 8)
            color = random.choice(["#ff4d8d", "#ffd166", "#56ccf2", "#7ae582", "#a78bfa", "#ff8fab"])
            self.confetti.append({"x": x, "y": y, "speed": s, "color": color, "drift": random.randint(-2, 2), "w": random.randint(8, 16), "h": random.randint(16, 32)})

    def animate_confetti(self):
        self.canvas.delete("confetti")
        for piece in self.confetti:
            piece["y"] += piece["speed"]
            piece["x"] += piece["drift"]
            if piece["y"] > 860:
                piece["y"] = -30
                piece["x"] = random.randint(100, 1000)
            if piece["x"] < 60 or piece["x"] > 1040:
                piece["x"] = random.randint(100, 1000)

            self.canvas.create_rectangle(piece["x"], piece["y"], piece["x"] + piece["w"], piece["y"] + piece["h"],
                                         fill=piece["color"], outline="", tags="confetti")

        self.root.after(30, self.animate_confetti)

    def trigger_confetti(self):
        self.button.config(text="Wishing You Joy! ✨")
        self.root.after(800, lambda: self.button.config(text="Celebrate Rehan 🎉"))
        self.create_confetti()

    def start_music_if_available(self):
        try:
            music_path = self.find_music_path()
            if not music_path:
                return
            if pygame is not None:
                pygame.mixer.init()
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(-1)
                self.music_enabled = True
                self.music_handle = music_path
        except Exception:
            pass

    def find_music_path(self):
        candidates = [
            "assets/rehan_birthday_song.mp3",
            "assets/song.mp3",
            "assets/birthday_song.mp3",
            "birthday_song.mp3",
            "song.mp3",
        ]
        for path in candidates:
            if os.path.exists(path):
                return path
        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayApp(root)
    root.mainloop()
