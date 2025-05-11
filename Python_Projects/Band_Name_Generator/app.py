{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26f90e0f-2ba5-40f5-8caa-85e4e1c10601",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app.py\n",
    "import streamlit as st\n",
    "import random\n",
    "\n",
    "st.title(\"🎸 Band Name Generator\")\n",
    "\n",
    "city_list = [\"Neon\", \"Electric\", \"Shadow\", \"Mystic\", \"Crimson\", \"Silver\"]\n",
    "animal_list = [\"Tigers\", \"Wolves\", \"Dragons\", \"Penguins\", \"Panthers\", \"Eagles\"]\n",
    "\n",
    "user_city = st.text_input(\"What is the name of your city?\")\n",
    "user_animal = st.text_input(\"What is your favorite animal?\")\n",
    "\n",
    "if st.button(\"Generate Band Names\"):\n",
    "    if user_city and user_animal:\n",
    "        random_city = random.choice(city_list)\n",
    "        random_animal = random.choice(animal_list)\n",
    "\n",
    "        band_name_1 = f\"{user_city} {random_animal}\"\n",
    "        band_name_2 = f\"{random_city} {user_animal}\"\n",
    "        band_name_3 = f\"{random_city} {random_animal}\"\n",
    "\n",
    "        st.subheader(\"🎤 Your Band Name Ideas:\")\n",
    "        st.write(f\"1. {band_name_1}\")\n",
    "        st.write(f\"2. {band_name_2}\")\n",
    "        st.write(f\"3. {band_name_3}\")\n",
    "    else:\n",
    "        st.warning(\"Please enter both your city and favorite animal.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
