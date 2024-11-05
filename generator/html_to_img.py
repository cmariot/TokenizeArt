# from html2image import Html2Image

# hti = Html2Image(browser='firefox', output_path='.', disable_logging=True)
# hti.screenshot(html_file='file.html', save_as='page_image.png')


from selenium import webdriver

# # Configurez le navigateur pour être en mode sans interface graphique (headless)
# options = webdriver.FirefoxOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1200x800')  # Définissez la taille de la fenêtre si nécessaire

# Chemin vers le driver de Chrome
driver = webdriver.Firefox(executable_path='./geckodriver')

# Chargez la page HTML (cela peut être un fichier ou une URL)
html_file = './file.html'  # Ou utilisez une URL
driver.get(html_file)

# Capturez l'image et enregistrez-la
driver.save_screenshot("page_image.png")

# Fermez le navigateur
driver.quit()
