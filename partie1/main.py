
import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

from dog_api import get_breeds, get_dog_image
from game import generate_question
from scores import save_score, get_record
from comments import get_comment


TOTAL_ROUNDS = 10

score = 0
round_number = 0
answered = False
question_ready = False
correct = ""
options = []
pressed_label = None

breeds = get_breeds()

if len(breeds) < 4:
    print("Unable to retrieve dog breeds.")
    raise SystemExit


window = tk.Tk()
window.title("Dog Guesser")
window.geometry("650x800")

title = tk.Label(
    window,
    text="DOG GUESSER",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

progress_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
progress_label.pack(pady=5)

score_label = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=5)

record_label = tk.Label(
    window,
    text=f"High Score: {get_record()}",
    font=("Arial", 12, "bold")
)
record_label.pack(pady=5)

question_label = tk.Label(
    window,
    text="What breed is this dog?",
    font=("Arial", 16)
)
question_label.pack(pady=10)

image_label = tk.Label(window)
image_label.pack(pady=10)

buttons = []

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold")
)


# Check the selected answer
def check_answer(selected_breed):
    global score, answered

    if answered or not question_ready:
        return

    answered = True

    if selected_breed == correct:
        score += 100

    score_label.config(text=f"Score: {score}")

    for i in range(4):
        option = options[i]
        label = buttons[i]

        if option == correct:
            if selected_breed == correct:
                label.config(
                    text=option.capitalize() + "  +100",
                    bg="#4CAF50",
                    fg="white"
                )
            else:
                label.config(
                    text=option.capitalize() + "  ✓",
                    bg="#4CAF50",
                    fg="white"
                )

        elif option == selected_breed:
            label.config(
                text=option.capitalize() + "  +0",
                bg="#E53935",
                fg="white"
            )

        label.config(cursor="arrow")

    next_button.config(state="normal")


# Remember which answer was pressed
def on_answer_press(event):
    global pressed_label

    if answered or not question_ready:
        return

    pressed_label = event.widget
    pressed_label.config(relief="sunken")


# Confirm only when released inside the same answer
def on_answer_release(event):
    global pressed_label

    if pressed_label is None:
        return

    label = pressed_label
    pressed_label = None

    label.config(relief="raised")

    x = label.winfo_pointerx() - label.winfo_rootx()
    y = label.winfo_pointery() - label.winfo_rooty()

    inside = (
        0 <= x < label.winfo_width()
        and 0 <= y < label.winfo_height()
    )

    if not inside:
        return

    if answered or not question_ready:
        return

    for i in range(4):
        if buttons[i] == label:
            check_answer(options[i])
            return


# Load a dog image
def load_question():
    global round_number, answered, question_ready

    result_label.config(
        text="Loading image...",
        fg="black"
    )
    window.update_idletasks()

    try:
        image_url = get_dog_image(correct)

        if image_url is None:
            raise ValueError("Image URL unavailable")

        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        image.thumbnail((380, 230))

        photo = ImageTk.PhotoImage(image)

    except (requests.RequestException, OSError, ValueError) as error:
        print("Image error:", error)

        question_ready = False

        image_label.config(image="", text="Image unavailable")
        image_label.image = None

        result_label.config(
            text="Network error. Please try again.",
            fg="red"
        )

        retry_button.pack(pady=5)
        return

    round_number += 1
    answered = False
    question_ready = True

    progress_label.config(
        text=f"Question {round_number} / {TOTAL_ROUNDS}"
    )

    image_label.config(image=photo, text="")
    image_label.image = photo

    result_label.config(text="")
    retry_button.pack_forget()

    for i in range(4):
        buttons[i].config(
            text=options[i].capitalize(),
            bg="#F0F0F0",
            fg="black",
            relief="raised",
            cursor="hand2"
        )

    next_button.config(state="disabled")


# Prepare the next question
def next_question():
    global correct, options, question_ready, pressed_label

    if round_number >= TOTAL_ROUNDS:
        end_game()
        return

    pressed_label = None
    question_ready = False
    next_button.config(state="disabled")

    for label in buttons:
        label.config(cursor="arrow")

    correct, options = generate_question(breeds)
    load_question()


# Save the score and display final results
def end_game():
    previous_record = get_record()
    save_score(score)
    new_record = get_record()

    record_label.config(text=f"High Score: {new_record}")
    progress_label.config(text="Game Over!")

    question_label.config(
        text=f"Final Score: {score} / {TOTAL_ROUNDS * 100}"
    )

    image_label.config(image="", text="")
    image_label.image = None

    for label in buttons:
        label.pack_forget()

    next_button.pack_forget()
    retry_button.pack_forget()

    rank, comment = get_comment(score)

    result_label.config(
        text=f"{rank}\n\n{comment}",
        fg="#1565C0",
        font=("Arial", 16, "bold"),
        justify="center"
    )

    if score > previous_record:
        progress_label.config(text="NEW HIGH SCORE!")


# Create four clickable answer labels
for i in range(4):
    label = tk.Label(
        window,
        width=28,
        font=("Arial", 12),
        bg="#F0F0F0",
        fg="black",
        relief="raised",
        bd=2,
        pady=8,
        cursor="hand2"
    )

    label.pack(pady=4)

    label.bind("<ButtonPress-1>", on_answer_press)
    label.bind("<ButtonRelease-1>", on_answer_release)

    buttons.append(label)

result_label.pack(pady=8)

next_button = tk.Button(
    window,
    text="Next →",
    width=28,
    height=2,
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    state="disabled",
    command=next_question
)
next_button.pack(pady=8)

retry_button = tk.Button(
    window,
    text="Retry",
    width=22,
    command=load_question
)


next_question()
window.mainloop()
