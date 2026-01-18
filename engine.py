import json
import random
import urllib.parse
from datetime import datetime
from typing import List, Dict, Optional

# =========================
# TREND CONFIGURATIONS
# =========================

TRENDS = [
    {"id": "streetwear", "name": "Streetwear", "emoji": "🖤", "desc": "Baggy / Oversized Era"},
    {"id": "y2k", "name": "Y2K Revival", "emoji": "💿", "desc": "Early 2000s Chaos"},
    {"id": "quiet", "name": "Quiet Luxury", "emoji": "🤍", "desc": "Old Money Energy"},
    {"id": "minimal", "name": "Model Off-Duty", "emoji": "😎", "desc": "Effortless Minimal"},
    {"id": "90s", "name": "90s Minimalism", "emoji": "🧥", "desc": "Timeless Classics"},
    {"id": "indie", "name": "Indie Sleaze", "emoji": "🖤", "desc": "Messy Cool"},
    {"id": "grunge", "name": "Grunge / Alt", "emoji": "🧱", "desc": "Emotional Support Fit"},
    {"id": "gorpcore", "name": "Gorpcore", "emoji": "🧭", "desc": "Utility Fashion"},
    {"id": "office", "name": "Office Siren", "emoji": "💼", "desc": "Corporate Baddie"},
    {"id": "mob", "name": "Mob Wife", "emoji": "💎", "desc": "Loud Luxury"},
    {"id": "athleisure", "name": "Athleisure", "emoji": "🏃", "desc": "Sporty Chic"},
    {"id": "workwear", "name": "Workwear", "emoji": "🛠", "desc": "Blue-Collar Chic"}
]

TREND_DETAILS = {
    "streetwear": {
        "pieces": ["Oversized hoodie", "Wide-leg cargo pants", "Chunky sneakers", "Boxy graphic tee"],
        "colors": ["Black", "Grey", "Olive", "Navy"],
        "vibe": "Gender-neutral comfort. Slouchy silhouettes, technical fabrics, street-ready."
    },
    "y2k": {
        "pieces": ["Low-rise jeans", "Baby tee", "Platform sneakers", "Baggy denim"],
        "colors": ["Pink", "Blue", "Silver", "Lime green"],
        "vibe": "Chaotic optimism. Early-2000s chaos is back."
    },
    "quiet": {
        "pieces": ["Cashmere crewneck", "Tailored trousers", "Leather loafers", "Structured blazer"],
        "colors": ["Cream", "Camel", "Navy", "Charcoal"],
        "vibe": "Wealth whispers. Clean lines, expensive fabrics."
    },
    "minimal": {
        "pieces": ["White t-shirt", "Straight jeans", "Clean sneakers", "Oversized sunglasses"],
        "colors": ["White", "Black", "Denim blue", "Grey"],
        "vibe": "Accidentally hot. Simple pieces, perfect fit."
    },
    "90s": {
        "pieces": ["Leather jacket", "Slip dress", "Straight jeans", "Plain knit sweater"],
        "colors": ["Black", "Brown", "Beige", "White"],
        "vibe": "Timeless minimalism."
    },
    "indie": {
        "pieces": ["Leather jacket", "Skinny jeans", "Vintage scarf", "Band tee"],
        "colors": ["Black", "Burgundy", "Dark grey"],
        "vibe": "Messy layers, intentional chaos."
    },
    "grunge": {
        "pieces": ["Flannel shirt", "Ripped jeans", "Combat boots", "Band tee"],
        "colors": ["Black", "Dark red", "Faded denim"],
        "vibe": "Emotional support outfit."
    },
    "gorpcore": {
        "pieces": ["Cargo pants", "Windbreaker", "Trail sneakers", "Technical vest"],
        "colors": ["Olive", "Orange", "Black"],
        "vibe": "Utility meets street."
    },
    "office": {
        "pieces": ["Sharp blazer", "Pencil skirt", "Silk blouse", "Fitted trousers"],
        "colors": ["Black", "White", "Navy"],
        "vibe": "Corporate but seductive."
    },
    "mob": {
        "pieces": ["Fur coat", "Gold jewelry", "Leather jacket", "Sunglasses"],
        "colors": ["Brown", "Gold", "Black"],
        "vibe": "Loud luxury."
    },
    "athleisure": {
        "pieces": ["Tech joggers", "Matching set", "White sneakers"],
        "colors": ["Black", "Grey", "White"],
        "vibe": "Gym fits worn everywhere."
    },
    "workwear": {
        "pieces": ["Chore jacket", "Denim jeans", "Work boots"],
        "colors": ["Navy", "Tan", "Olive"],
        "vibe": "Blue-collar chic."
    }
}

# =========================
# OUTFIT GENERATOR
# =========================

class OutfitGenerator:
    def __init__(self):
        self.saved_looks = []
        self.load_saved_looks()

    # ---------- AI LOGIC ----------
    def generate_styling_logic(self, trend_id, vibes, keywords):
        logic_map = {
            "streetwear": "Oversized silhouettes, relaxed fits, comfort-first styling.",
            "y2k": "Playful chaos, bold graphics, early-2000s nostalgia.",
            "quiet": "Clean tailoring, muted tones, premium fabrics.",
            "minimal": "Simple silhouettes, intentional fits, neutral palette.",
            "grunge": "Layered darkness, rugged textures, anti-polish energy.",
            "gorpcore": "Technical utility meets urban wearability.",
            "office": "Sharp tailoring with controlled sensuality.",
            "mob": "Maximalism, statement pieces, unapologetic confidence.",
            "athleisure": "Sporty silhouettes styled for daily wear.",
            "workwear": "Durable fabrics, structured layers, functional aesthetics."
        }

        logic = logic_map.get(trend_id, "Balance fit, color, and texture.")
        if vibes:
            logic += f" Vibe modifiers: {', '.join(vibes)}."
        if keywords:
            logic += f" Keyword influence: {', '.join(keywords)}."

        return logic
    
    def remix_outfit(self, pieces, colors):
        """
        Adds controlled randomness so outfits don't feel repetitive
        """
        random.shuffle(pieces)

        # Sometimes drop or add an accessory
        extras = [
            "Crossbody bag",
            "Silver chain",
            "Baseball cap",
            "Leather belt",
            "Sunglasses",
            "Beanie"
        ]

        if random.random() > 0.5:
            pieces.append(random.choice(extras))

        # Color remix
        if random.random() > 0.4:
            colors = random.sample(colors, min(len(colors), random.randint(2, 3)))

        return pieces, colors


    # ---------- MOODBOARD ----------
    def generate_moodboard(self, trend_name, keywords):
        """
        Guaranteed-to-render fashion images.
        No APIs. No redirects. No blocks.
        """

        # Hand-curated fashion/editorial images
        STATIC_FASHION_IMAGES = [
            "https://images.unsplash.com/photo-1520975916090-3105956dac38?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1520975661595-6453be3f7070?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1542060748-10c28b62716f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=800&q=80",
        ]

        return random.sample(STATIC_FASHION_IMAGES, 4)


    # ---------- OUTFIT ----------
    def generate_outfit(self, trend_id, gender="unisex", palette=None, vibes=None, keywords=None):
        trend = TREND_DETAILS[trend_id]
        trend_name = next(t["name"] for t in TRENDS if t["id"] == trend_id)

        pieces = random.sample(trend["pieces"], min(4, len(trend["pieces"])))
        colors = palette if palette else trend["colors"]

        pieces, colors = self.remix_outfit(pieces, colors)


        outfit = {
            "id": int(datetime.now().timestamp() * 1000),
            "trend": trend_name,
            "gender": gender,
            "pieces": pieces,
            "colors": colors,
            "description": trend["vibe"],
            "ai_logic": self.generate_styling_logic(trend_id, vibes or [], keywords or []),
            "vibes": vibes or [],
            "keywords": keywords or [],
            "moodboard": self.generate_moodboard(trend_name, keywords or []),
            "created_at": datetime.now().isoformat()
        }
        return outfit

    # ---------- STORAGE ----------
    def save_look(self, outfit):
        outfit["saved_at"] = datetime.now().isoformat()
        self.saved_looks.append(outfit)
        with open("saved_looks.json", "w") as f:
            json.dump(self.saved_looks, f, indent=2)

    def load_saved_looks(self):
        try:
            with open("saved_looks.json") as f:
                self.saved_looks = json.load(f)
        except:
            self.saved_looks = []

    # ---------- DISPLAY ----------
    def display_outfit(self, outfit):
        print("\n" + "=" * 60)
        print(f"🎨 {outfit['trend'].upper()} ({outfit['gender']})")
        print("=" * 60)
        print(f"\n📝 VIBE:\n  {outfit['description']}")
        print(f"\n🧠 AI LOGIC:\n  {outfit['ai_logic']}")
        print("\n👕 PIECES:")
        for p in outfit["pieces"]:
            print(f"  - {p}")
        print("\n🎨 COLORS:", ", ".join(outfit["colors"]))
        print("\n🖼️ MOODBOARD:")
        for url in outfit["moodboard"]:
            print(f"  {url}")
        print("=" * 60 + "\n")

# =========================
# RUN
# =========================

if __name__ == "__main__":
    gen = OutfitGenerator()
    outfit = gen.generate_outfit(
        trend_id="streetwear",
        vibes=["Edgy", "Monochrome"],
        keywords=["cargo", "oversized"]
    )
    gen.display_outfit(outfit)
    gen.save_look(outfit)
