import streamlit as st
from BladesInTheDarkRoller.roller import Roller


st.markdown(
    """<svg class="bitd-logo--large" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 357.9 175.3" style="enable-background:new 0 0 357.9 175.3;" xml:space="preserve">
      <style type="text/css">
      	.st0{fill:#FFFFFF;}
      </style>
      <g>
      	<path class="st0" d="M179.1,60.9l-5.4-9.1L160.5,0h-16.1l2.8,8.9l-12.1,42.8l-5.4,9.1H149l-3.6-9.1l0.5-2.2h13.7l0.5,2.2l-3.5,9.1
      		H179.1z M152.8,23.4l4.3,16.5h-8.7L152.8,23.4z M94.3,0l4.5,9.1v42.6l-4.5,9.1h37V46.8l-9,4.7l0.2-0.1h-11l0.6-1.5l0.1-40.7
      		l4.5-9.1H94.3z"></path>
      	<path class="st0" d="M241,97.7l5.8,11.6v54.3l-5.8,11.6h29.1l-5.7-11.6v-26.5l14.7,26.5l-1.9,11.6h30.6l-10.5-11.9v0.1l-17.6-36.4
      		l9.6-17.3l13.6-12h-22.2l-16.2,29.6v-18l6-11.6H241z M212.9,163.9l5.8,11.4h17.6l-5.8-11.5v-15l-3.9-6.9l-7.5-4l8.3-4.2l3-6.5v-18
      		l-5.8-11.5h-52.3l5.8,11.6v54.4l-5.8,11.5h23.4V144h15.6l1.5,2.9V163.9z M195.7,112.9l-1.4-3h16.8l1.8,3.6v15.2l-1.7,3h-15.5V112.9
      		z M171.6,175.3l-7.1-11.6l-17.2-65.9h-20.9l3.6,11.4l-15.6,54.6l-7.1,11.6h25.1l-4.7-11.6l0.7-2.8h17.7l0.7,2.8l-4.6,11.6H171.6z
      		 M137.4,127.5l5.5,21.1h-11.4L137.4,127.5z M100.3,175.3l5.8-11.5v-54.6l-5.8-11.5H48.1l5.8,11.6v54.4l-5.8,11.5H100.3z
      		 M88.5,160.2l-1.5,2.9H70.3l1.2-2.6v-47.5l-1.5-3h16.8l1.8,3.6V160.2z"></path>
      </g>
      <g>
      	<path class="st0" d="M78.9,24.6l1.3-2.6v-9.6l-1.4-2.8H66.8L68,12v12.6H78.9z M79,51.3l1.2-2.3V36.4L79,34.1H68v15.1l-1,2.1H79z
      		 M122.5,51.3L122.5,51.3l-0.2,0.1L122.5,51.3z M209,51.3l1.2-2.3V12.4l-1.4-2.8h-12.9l1.2,2.4v37.3l-1,2.1H209z M257.7,51.3
      		L257.7,51.3l-0.2,0.1L257.7,51.3z M305.7,51.8l-4.5,9.1h-31.4V46.6l8.7,4.7h14.7l1.4-2.6v-7.2l-1.3-2.3l-19.2-6.8l-4.4-8.9V9.1
      		l4.4-9.1H304v14.2l-8.7-4.7H282l-1.2,2.6v5l1.1,2.3l19.4,6.9l4.4,8.9V51.8z M266.4,60.9h-38.7l4.5-9.1V9.1L227.7,0h38.7v14.2
      		l-8.7-4.7h-12.8l0.9,1.7v13.3h3.6l8.7-4.5v18.6l-8.7-4.6h-3.6v15.7l-0.7,1.5h12.7l8.8-4.6V60.9z M223.7,51.9l-4.5,9h-40.2l4.5-9
      		V9.1L179.1,0h40.2l4.5,9V51.9z M92.8,51.9l-4.5,9H50l4.5-9V9.1L50,0h38.4l4.5,9v12l-2.2,5.1l-6.5,3.3l6,3.2l2.8,5.4V51.9z
      		 M126.5,87.3V71.1l-2.3-4.3h11.9l-2.4,4.3v16.1l2.3,4.3h-11.8L126.5,87.3z M151.5,78v-6.9l-2.4-4.3h10.7l-2.4,4.3v20.4h-5.4
      		L145,80.8v6.5l2.3,4.3h-10.5l2.4-4.3V71.1l-2.4-4.3h7.8L151.5,78z M173.5,71.8v1.4l-5.1,2.2v-8.5h18.1v8.5l-5.1-2.2v-1.4h-0.4v15.5
      		l2.3,4.3h-12l2.4-4.3V71.8H173.5z M202.3,76.3v-5.2l-2.4-4.3h11.7l-2.4,4.3v16.2l2.3,4.3h-11.6l2.4-4.3v-6h-5.4v6l2.3,4.3h-11.7
      		l2.4-4.3V71.1l-2.4-4.3h11.8l-2.4,4.3v5.2H202.3z M222.2,81.3v5.4h4.4l4.7-2.1v7.1h-18.7l2.4-4.3V71.1l-2.4-4.3h18.7V74l-4.7-2.2
      		h-4.4v4.5h0.7l4.7-2.1v9.2l-4.7-2.1H222.2z"></path>
      </g>
      <polygon class="st0" points="278.6,69.2 276,71 239.4,71 239.4,88.8 242.5,90.3 247.4,82.6 276,82.6 287.3,89.2 343.2,83.9
      	357.9,69.2 "></polygon>
      <polygon class="st0" points="0,69.2 14.7,83.9 70.6,89.2 82,82.6 110.5,82.6 115.4,90.3 118.5,88.8 118.5,71 82,71 79.3,69.2 "></polygon>
      <g>
      	<path class="st0" d="M234.3,109.3C234.5,109.5,234.2,109.1,234.3,109.3"></path>
      </g>
    </svg>""",
    unsafe_allow_html=True,
)


r = Roller()

roll_types = ["Action", "Resistance", "Engagement", "Fortune"]
label = "Let’s roll…"

selected_roll = st.selectbox(
    label="What kind of roll are you making?",
    options=roll_types,
)

## action dice
if selected_roll == roll_types[0]:
    action_rating = st.selectbox(label="How many dice?", options=range(0, 7))

# Resistance dice
if selected_roll == roll_types[1]:
    resist_rating = st.selectbox(label="How many dice?", options=range(0, 7))

# Fortune dice
if selected_roll == roll_types[3]:
    advantageDice = st.selectbox(
        label="How many major advantages?", options=range(0, 4)
    )
    disadvantageDice = st.selectbox(
        label="How many major disadvantages?", options=range(0, 4)
    )
    fortune_dice = 1 + advantageDice - disadvantageDice
    st.markdown(
        f"The number of dice is {fortune_dice}. Hit the **{label}** button when you are ready."
    )

# Engagement dice
if selected_roll == roll_types[2]:
    engagementDice = 1
    bold = st.checkbox("This operation particularly bold or daring.")
    if bold:
        engagementDice += 1
        st.markdown("+1 advantage dice.")
    complex = st.checkbox(
        "This operation overly complex or contingent on many factors."
    )
    if complex:
        engagementDice -= 1
        st.markdown("-1 advantage dice.")
    vulnerable = st.checkbox(
        "The plan's detail expose a vulnerability of the target or hit them where they're weakest."
    )
    if vulnerable:
        engagementDice += 1
        st.markdown("+1 advantage dice.")
    defended = st.checkbox(
        "The target strongest against this approach, or they have particular defenses or special defenses or special preparations. "
    )
    if defended:
        engagementDice -= 1
        st.markdown("-1 advantage dice.")
    aid = st.checkbox(
        "Some friends or contacts provide aid or insight for this operation."
    )
    if aid:
        engagementDice += 1
        st.markdown("+1 advantage dice.")
    interference = st.checkbox("Enemies or rivals are interfering in the operation.")
    if interference:
        engagementDice -= 1
        st.markdown("-1 advantage dice.")
    otherFactors = st.selectbox(
        "Is there any other factor to consider? Input 0, or a positive/negative number for advantage / disadvantage respectively. ",
        options=range(-2, 3),
        index=2,
    )
    engagementDice += otherFactors

    st.markdown(
        f"The dice pool is **{engagementDice}**. Hit the **{label}** button when you are ready."
    )
# action roll
if selected_roll == roll_types[0] and st.button(label=label):
    result, pool = r.actionRoll(action_rating)
    st.image([f"img/{die}.png" for die in pool])
    st.markdown(result)

# Resistance roll
if selected_roll == roll_types[1] and st.button(label=label):
    result, pool = r.resistanceRoll(resist_rating)
    st.image([f"img/{die}.png" for die in pool])
    st.markdown(result)

# Engagement roll
if selected_roll == roll_types[2] and st.button(label=label):
    result, pool = r.engagementRoll(engagementDice)
    st.image([f"img/{die}.png" for die in pool])
    st.markdown(result)

# Fortune roll
if selected_roll == roll_types[3] and st.button(label=label):
    result, pool = r.fortuneRoll(fortune_dice)
    st.image([f"img/{die}.png" for die in pool])
    st.markdown(result)