import streamlit as st
import random
import nltk
from nltk.corpus import words

nltk.download('words')

# Difficulty filter
def filter_words(diff, safety):
    word_list = words.words()
    if safety == 'on':
        if diff == 'Easy':
            return [i for i in word_list if 4 <= len(i) < 5]
        elif diff == 'Med':
            return [i for i in word_list if 4 <= len(i) < 7]
        elif diff == 'Hard':
            return [i for i in word_list if 4 <= len(i) < 9]
    else:
        if diff == 'Easy':
            return [i for i in word_list if len(i) < 5]
        elif diff == 'Med':
            return [i for i in word_list if len(i) < 7]
        elif diff == 'Hard':
            return [i for i in word_list if len(i) < 9]

# Hangman visuals
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========
6 More Chances
''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
5 More Chances
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
4 More Chances
''', 
               r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
3 More Chances
''', 
               r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
2 More Chances
''', 
               r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
1 More Chance
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
HANGED MAN
'''
              ]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.diff = st.selectbox("Select Difficulty", ['Easy', 'Med', 'Hard'])
    st.session_state.safety = st.radio("Safety Filter", ['on', 'off'])
    word_list = filter_words(st.session_state.diff, st.session_state.safety)
    st.session_state.word = random.choice(word_list).lower()
    st.session_state.score = ['_'] * len(st.session_state.word)
    st.session_state.wrong_guess = []
    st.session_state.chances = 6

# Game display
st.title("🎯 Hangman Game")
st.markdown(f"**Word:** {' '.join(st.session_state.score)}")
st.markdown(f"**Wrong guesses:** {', '.join(st.session_state.wrong_guess)}")
st.code(HANGMANPICS[6 - st.session_state.chances], language="")

# Guess input section with control
with st.form("guess_form", clear_on_submit=True):
    guess = st.text_input("Enter a letter").lower()
    submit = st.form_submit_button("Submit Guess")

if submit and guess:
    guess = guess[0]  # Take only first character
    if guess in st.session_state.word:
        for i in range(len(st.session_state.word)):
            if st.session_state.word[i] == guess:
                st.session_state.score[i] = guess
    else:
        if guess not in st.session_state.wrong_guess:
            st.session_state.wrong_guess.append(guess)
            st.session_state.chances -= 1
    st.rerun()

# Game result
if '_' not in st.session_state.score:
    st.success(f"You won! The word was: {st.session_state.word}")
elif st.session_state.chances == 0:
    st.error(f"You lost! The word was: {st.session_state.word}")

# Restart button
if st.button("Restart Game"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
