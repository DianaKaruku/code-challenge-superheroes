from app.models import db, Hero, Power, HeroPower

# Seeding powers
print("🦸‍♀️ Seeding powers...")
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

powers = [Power(**data) for data in powers_data]
db.session.add_all(powers)
db.session.commit()

# Seeding heroes
print("🦸‍♀️ Seeding heroes...")
heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

heroes = [Hero(**data) for data in heroes_data]
db.session.add_all(heroes)
db.session.commit()

# Adding powers to heroes
print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]

for hero in Hero.query.all():
    for _ in range(1, 4):  # Assuming a hero can have 1 to 3 powers
        # get a random power
        power = Power.query.order_by(db.func.random()).first()

        hero_power = HeroPower(hero=hero, power=power, strength=strengths.pop(0))
        db.session.add(hero_power)

db.session.commit()

print("🦸‍♀️ Done seeding!")
