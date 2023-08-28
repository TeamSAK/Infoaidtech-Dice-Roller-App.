import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        self.dice_images = [
            Image.open(f"dice_{i}.png") for i in range(1, 7)
        ]

        self.dice_label = tk.Label(root)
        self.dice_label.pack(pady=100)

        self.dice_count_label = tk.Label(root, text="Number of Dice:")
        self.dice_count_label.pack()

        self.dice_count_entry = tk.Entry(root,width=60)
        self.dice_count_entry.pack(padx=50)

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def roll_dice(self):
        try:
            dice_count = int(self.dice_count_entry.get())
            if dice_count <= 0:
                messagebox.showerror("Invalid Input", "Please enter a valid number of dice.")
                return

            results = [random.randint(1, 6) for _ in range(dice_count)]

            dice_images = [self.dice_images[result - 1] for result in results]
            dice_photos = [ImageTk.PhotoImage(dice_image) for dice_image in dice_images]

            combined_image = Image.new('RGBA', (dice_images[0].width * dice_count, dice_images[0].height))
            for i, dice_image in enumerate(dice_images):
                combined_image.paste(dice_image, (i * dice_image.width, 0))
            combined_photo = ImageTk.PhotoImage(combined_image)

            self.dice_label.configure(image=combined_photo)
            self.dice_label.image = combined_photo

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.geometry("1000x800")  # Set initial window size
    root.mainloop()
