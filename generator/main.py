from PIL import Image, ImageDraw, ImageFont


def get_filename(user, project_name, date, grade):
    return f"{user}_{project_name}_{date}_{grade}"


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


if __name__ == "__main__":

    try:

        user = "John Doe"
        project_name = "Project Name"
        date = "01_01_2021"
        grade = "A"
        nft_number = 1

        filename = get_filename(user, project_name, date, grade)

        create_background_image(
            "Base.png",
            f"{filename}.png",
            (500, 500)
        )

        args = (
            (f"{project_name}", 22, 10, 290, 'left'),
            (f"finished by {user}", 16, 10, 315, 'left'),
            (f"on {date}", 14, 10, 335, 'left'),
            ("Each completed project at 42 School can be", 10, 10, 355, 'left'),
            ("awarded a unique NFT, serving as a digital", 10, 10, 370, 'left'),
            ("certificate of achievement.", 10, 10, 385, 'left'),
            ("This NFT verifies the student’s successful", 10, 10, 400, 'left'),
            ("completion, skills acquired, and serves as", 10, 10, 415, 'left'),
            ("an authentic, verifiable credential on the", 10, 10, 430, 'left'),
            ("blockchain.", 10, 10, 445, 'left'),

            # On the bottom right
            ("Project completion certificate", 10, 355, 415, 'right'),
            (f"NFT #{nft_number:03d}", 36, 335, 425, 'right'),
        )

        args = [
            (text, size, x, y + 30, align)
            for text, size, x, y, align in args
        ]

        for arg in args:
            insert_text(
                f"{filename}.png", "roboto/Roboto-Medium.ttf", '#D0D0D0',
                arg[0], arg[1], arg[2], arg[3], arg[4]
            )

    except Exception as e:

        print(f"Erreur : {e}")
        exit(1)
