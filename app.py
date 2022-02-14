from email.policy import default
from tkinter import Button
import streamlit as st
from burningwheel import roll, assess_difficulty

rolls = []

st.markdown("# Burning Wheel Dice Roller")
## Shade

shade = st.selectbox(
    label="What is the shade of the ability, attribute or skill rolled?",
    options=["Black", "Gray", "White"],
)

## Dice

dice = st.selectbox(
    label="How many dice are you rolling? Your exponent +1 for each character helping you +1 for each FoRK",
    options=range(0, 13),
)

## Obstacle

obstacle = st.selectbox(
    label="What is the obstacle?",
    options=range(0, 14),
)

## Open Ended

open_ended = st.selectbox(label="Is the roll open_ended ?", options=[False, True])

label = "Let’s roll…"

# Basic roll
if st.button(label=label):
    last_roll, result = roll(
        shade=shade, dice=dice, obstacle=obstacle, open_ended=open_ended
    )
    st.image([f"img/{die}.png" for die in last_roll])
    st.markdown(result)


# Offer Luck
rolls = last_roll.copy()
st.markdown(f"{rolls=}")
if 6 in rolls and st.button(
    label="Do you want to spend 1 Fate to make the roll open-ended?"
):

    st.markdown("rerolling…")
    new_rolls, new_result = roll(
        shade=shade, obstacle=obstacle, last_roll=last_roll, luck=True
    )
    st.image([f"img/{die}.png" for die in new_rolls])
    st.markdown(new_result)
