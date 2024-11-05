from PIL import Image, ImageDraw, ImageFont


def create_pixel_text_image(
    text,
    output_path="output.png",
    font_path="path/to/pixel_font.ttf",
    font_size=16
):

    # Définir la couleur de fond et du texte
    background_color = (0, 0, 0)  # Noir
    text_color = (0, 255, 0)      # Vert style terminal

    # Charger une police pixelisée
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Police non trouvée, vérifiez le chemin du fichier de police.")
        return

    # Calculer la taille de l'image pour contenir le texte
    dummy_img = Image.new("RGB", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_img)
    text_bbox = dummy_draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    img_width, img_height = text_width + 20, text_height + 20  # Marges

    # Créer l'image
    img = Image.new("RGB", (img_width, img_height), background_color)
    draw = ImageDraw.Draw(img)

    # Dessiner le texte au centre de l'image
    text_x = (img_width - text_width) // 2
    text_y = (img_height - text_height) // 2
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Sauvegarder l'image
    img.save(output_path)
    print(f"Image enregistrée sous {output_path}")


create_pixel_text_image(
    """
Project Completion Certification
This certifies that [user] has successfully completed the project [project_name] with a grade of [project_grade].
This NFT recognizes the achievement of this project within the 42 school curriculum, reflecting [user]'s skills and dedication.
""",
    output_path="certif.png",
    font_path="font.ttf",
    font_size=42
)
