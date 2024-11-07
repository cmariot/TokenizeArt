from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
import os


def get_filename(user, project_name, date, grade):
    path = os.path.join(settings.BASE_DIR, "static/nft/")
    return os.path.join(
        path, f"{user}_{project_name}_{date}_{grade}.png"
    ).replace(" ", "_")


def create_background_image(background_path: str, output_path, size=(500, 500)):

    # Charger l'image de fond
    try:
        background = Image.open(background_path)
    except IOError:
        raise Exception("Impossible de charger l'image de fond.")

    # Redimensionner l'image de fond
    if background.size != size:
        raise Exception(
            "La taille de l'image de fond ne correspond pas à la taille" +
            " spécifiée."
        )

    # Créer une image vide
    img = Image.new("RGB", size, (0, 0, 0))

    # Coller l'image de fond
    img.paste(background)

    # Sauvegarder l'image
    img.save(output_path)
    print(f"Image enregistrée sous {output_path}")


def insert_text(
    filename: str,
    font_path: str,
    color: str,
    text: str,
    font_size: int,
    x: int,
    y: int,
    align="left"
):

    # Charger l'image
    try:
        img = Image.open(filename)
    except IOError:
        raise Exception("Impossible de charger l'image.")

    # Charger la police
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        raise Exception("Impossible de charger la police.")

    # Dessiner le texte
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, font=font, fill=color, align=align)

    # Sauvegarder l'image
    img.save(filename)
    print(f"Texte inséré dans {filename}")


def generate_nft_image(user, project_name, date, grade, nft_number):

    # Convertir la date en format US
    date = date.strftime("%m-%d-%Y")
    filename = get_filename(user, project_name, date, grade)

    create_background_image(
        os.path.join(settings.BASE_DIR, "static/generate_nft/Base.png"),
        filename,
        (500, 500)
    )

    args = (
        (f"{project_name}", 22, 10, 305, 'left'),
        (f"finished by {user}", 16, 10, 330, 'left'),
        (f"with a grade of {grade}.", 14, 10, 350, 'left'),
        ("Each completed project at 42 School can be", 10, 10, 370, 'left'),
        ("awarded a unique NFT, serving as a digital", 10, 10, 385, 'left'),
        ("certificate of achievement.", 10, 10, 400, 'left'),
        ("This NFT verifies the student’s successful", 10, 10, 415, 'left'),
        ("completion, skills acquired, and serves as", 10, 10, 430, 'left'),
        ("an authentic, verifiable credential on the", 10, 10, 445, 'left'),
        ("blockchain.", 10, 10, 460, 'left'),

        # On the bottom right
        ("Project completion certificate", 10, 355, 430, 'right'),
        (f"NFT #{nft_number:03d}", 36, 335, 440, 'right'),
    )

    for arg in args:
        insert_text(
            filename,
            os.path.join(
                settings.BASE_DIR,
                "static/generate_nft/roboto/Roboto-Medium.ttf"
            ),
            color='#D0D0D0',
            text=arg[0],
            font_size=arg[1],
            x=arg[2],
            y=arg[3],
            align=arg[4]
        )

    return filename
