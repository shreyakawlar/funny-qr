import qrcode
from PIL import Image, ImageDraw, ImageFont

# List of funny jokes
jokes = [
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why don’t eggs tell jokes? They’d crack each other up!",
    "What do you call cheese that isn’t yours? Nacho cheese!",
    "Why did the math book look sad? Because it had too many problems!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don’t some couples go to the gym? Because some relationships don’t work out!",
    "What do you call a fish wearing a bowtie? Sofishticated!"
]

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add a URL or text to the QR code
qr.add_data("https://your-website.com/funny.html")  # Replace with your hosted URL
qr.make(fit=True)

# Create an image with pastel colors
img = qr.make_image(fill_color="#FF9AA2", back_color="#B5EAD7")  # Pastel pink and green

# Add a funny sticker (emoji) and text
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()  # Use default font
draw.text((10, 10), "😂", font=font, fill="#6B5B95")  # Pastel purple emoji
draw.text((50, 10), "Made by 1st years", font=font, fill="#6B5B95")  # Pastel purple text

# Save the QR code
img.save("funny_qr.png")
print("QR code generated and saved as 'funny_qr.png'")