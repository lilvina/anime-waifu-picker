import json, random, hashlib, textwrap
from datetime import date

ANIME_LIST = [
    "Rem (Re:Zero)",
    "Asuna (SAO)",
    "Mikasa (AOT)",
    "Hinata (Naruto)",
    "Zero Two (Darling in the Franxx)",
    "Kakashi (Naruto) - husbando",
    "Levi (AOT) - husbando",
    "Tuxedo Mask (Sailor Moon) - husbando",
    "Gintoki (Gintama) - husbando",
    "Saber (Fate)"
]

HOROSCOPE_TEMPLATES = {
    "very_high": [
        "Starlight is on your side - sparks will fly. Take the lead and say something cute!",
        "Cosmic alignment: today feels like a 'meet-cute' in a rom-com. Embrace it."
    ],
    "high": [
        "The stars wink at you. A small compliment could make someone's day.",
        "Warm vibes surround you — be playful and honest."
    ],
    "mid": [
        "An ordinary day with a chance for small, meaningful moments. Stay open.",
        "Compatibility is balanced — patient, steady charm wins today."
    ],
    "low": [
        "Not the strongest day for romance — keep expectations low and enjoy the day.",
        "Small miscommunications possible. A light joke eases tension."
    ],
    "very_low": [
        "The cosmos advises rest and self-care over romance today.",
        "Best to be a friend today — deep sparks may need to wait."
    ]
}

def deterministic_score(name, when):
    s = f"{name}||{when.isoformat()}"
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    val = int(h[:8], 16)
    return val % 101

def choose_template(score):
    import random

    if score >= 85:
        group = "very_high"
    elif score >= 65:
        group = "high"
    elif score >= 40:
        group = "mid"
    elif score >= 20:
        group = "low"
    else:
        group = "very_low"
    return random.choice(HOROSCOPE_TEMPLATES[group])


def show_card(name, rating, compat, horoscope):
    border = "=" * 60
    print("\n" + border)
    print(f"PICKED: {name}")
    print("-" * 60)
    print(f"Rating (1-10): {rating}")
    print(f"Today's compatability: {compat}%")
    print("\nHoroscope:")
    print(textwrap.fill(horoscope, width=60))
    print(border + "\n")

today = date.today()
seed = int(today.strftime("%Y%m%d"))
random.seed(seed)

for i in range(3):
    picked = random.choice(ANIME_LIST)

    rating = random.randint(6, 10)
    compat = deterministic_score(picked, today)
    horoscope = choose_template(compat)
    show_card(picked, rating, compat, horoscope)

print("Demo complete. To use the interactive version, copy the full script provided earlier into waifu-picker.py and run `python3 waifu-picker.py` locally.")