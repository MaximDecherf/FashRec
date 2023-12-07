import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.data.fashion_images import FashionImagesDataset
from src.data.likingsystem import LikingSystem


def show_image_rating_window(root, data_dir):
    # Create a new window for image rating
    rating_window = tk.Toplevel(root)
    dataset = FashionImagesDataset(data_dir)

    likes = LikingSystem(dataset)
    show_image(rating_window, dataset, 0, likes)


# clears rating window and presents the new image
def show_image(rating_window, dataset, id, liking_system):
    def on_key_press(event):
        if event.keysym == "Right":
            like_image()
        if event.keysym == "Left":
            dislike_image()

    def like_image():
        liking_system.like(id)
        show_next_image()

    def dislike_image():
        liking_system.dislike(id)
        show_next_image()

    def show_next_image():
        show_image(rating_window, dataset, id + 1, liking_system)

    for widget in rating_window.winfo_children():
        widget.destroy()

    rating_window.title("Image Rating")

    rating_window.bind('<KeyPress>', on_key_press)

    image_path = dataset.get_image_path(id)
    print(image_path)

    image = Image.open(image_path)
    image = image.resize((image.width * 3, image.height * 3))
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(rating_window, image=image)
    image_label.image = image  # Keep a reference to prevent garbage collection
    image_label.pack(padx=20, pady=20)

    # Like button
    like_button = tk.Button(rating_window, text="Like", command=like_image)
    like_button.pack(side=tk.LEFT, padx=20)

    # Dislike button
    dislike_button = tk.Button(rating_window, text="Dislike", command=dislike_image)
    dislike_button.pack(side=tk.RIGHT, padx=20)

    for likes in liking_system.get_likes():
        label = tk.Label(rating_window, text=likes["productDisplayName"], font=("Helvetica", 11), foreground="green")
        label.pack()

    for dislikes in liking_system.get_dislikes():
        label = tk.Label(rating_window, text=dislikes["productDisplayName"], font=("Helvetica", 11),foreground="red")
        label.pack()


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")

    # Specify the path to your image
    image_path = ""  # Adjust the path accordingly

    # Function to show the image rating window
    show_image_rating_window(root, image_path)
    # Run the Tkinter event loop
    root.mainloop()
