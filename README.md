# anime-waifu-picker

A full interactive script that:
- accepts a comma-separated list
- randomly picks a waifu/husbando
- shows a rating (1-10) and computes a deterministic today's compatability using a hash of the name & today's date so it changes each day but is stable within the day.
- produces a short horoscope-style message influenced by the compatability score.

A non-interactive demo run that prints three sample picks with ratings, compatability and horoscope messages.

How to use locally:
- copy the interactive script from the first executed cell into a file
- then, run it with python waifu-picker.py or python3 waifu-picker.py
- you can either paste your list or press Enter to use the default list
