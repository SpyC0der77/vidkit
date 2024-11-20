from PIL import Image, ImageDraw, ImageFont
import os

def wrap_text(draw, text, font, max_width):
    """
    Function to wrap text so it fits within the specified width.
    """
    print(f"Wrapping text with max width {max_width}")
    lines = []
    words = text.split(' ')
    current_line = words[0]

    # Loop through words to wrap text
    for index, word in enumerate(words[1:], start=1):
        current_line_with_word = current_line + ' ' + word
        # Using textbbox to get the bounding box of the text
        text_bbox = draw.textbbox((0, 0), current_line_with_word, font=font)
        width = text_bbox[2] - text_bbox[0]
        print(f"Iteration {index}: Checking line: '{current_line_with_word}' with width {width}")

        # If adding the new word exceeds the max_width, push current_line to lines
        if width <= max_width:
            current_line = current_line_with_word
            print(f"Iteration {index}: Current line fits within max width. New current line: '{current_line}'")
        else:
            print(f"Iteration {index}: Current line exceeds max width. Adding line: '{current_line}'")
            lines.append(current_line)
            current_line = word  # Start a new line with the current word
            print(f"Iteration {index}: Starting new line with word: '{word}'")

    # Always add the final line
    if current_line:
        lines.append(current_line)
        print(f"Adding final line: '{current_line}'")
    
    print(f"Final wrapped lines: {lines}")
    return lines

def render_lyric_frame(lyric, font_path, background_path, output_image, opacity=1.0):
    """
    Function to render a lyric frame with text on a background image and save it using file handling.
    """
    # Check if the background and font files exist
    if not os.path.exists(background_path):
        print(f"Error: Background image '{background_path}' does not exist.")
        return

    if not os.path.exists(font_path):
        print(f"Error: Font file '{font_path}' does not exist.")
        return

    try:
        # Load the background image
        print(f"Loading background image from {background_path}")
        background = Image.open(background_path).convert("RGBA")
        print(f"Background image loaded successfully")
    except Exception as e:
        print(f"Error loading background image from {background_path}: {e}")
        return

    canvas_width, canvas_height = background.size
    print(f"Original canvas size: width={canvas_width}, height={canvas_height}")
    canvas_width = 1920  # Limit the canvas width for wrapping purposes
    background = background.resize((canvas_width, canvas_height))
    print(f"Resized canvas size: width={canvas_width}, height={canvas_height}")

    try:
        # Load the font
        print(f"Loading font from {font_path}")
        font_size = 100
        font = ImageFont.truetype(font_path, font_size)
        print(f"Font loaded successfully with size {font_size}")
    except Exception as e:
        print(f"Error loading font from {font_path}: {e}")
        return

    # Create a new layer for the text
    text_layer = Image.new("RGBA", background.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_layer)
    print("Text layer created successfully")

    # Define max width for text wrapping (90% of the canvas width)
    max_width = int(canvas_width * 0.9)
    print(f"Max text width for wrapping: {max_width}")
    
    # Wrap the text based on the max width
    lines = wrap_text(draw, lyric, font, max_width)
    
    # Calculate line height and starting Y position to center the text vertically
    line_height = font_size + 10  # Adjust line height as needed
    total_text_height = len(lines) * line_height
    start_y = (canvas_height - total_text_height) // 2
    print(f"Total text height: {total_text_height}, Starting Y position: {start_y}")

    # Set text properties
    fill_color = (255, 255, 255, int(255 * opacity))  # White color with opacity

    # Draw each line of text centered horizontally
    for i, line in enumerate(lines):
        text_bbox = draw.textbbox((0, 0), line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x_position = (canvas_width - text_width) // 2
        y_position = start_y + i * line_height
        print(f"Drawing line {i + 1}: '{line}' at position (x={x_position}, y={y_position})")
        draw.text((x_position, y_position), line, font=font, fill=fill_color)

    # Combine the text layer with the background
    print("Combining text layer with background image")
    combined = Image.alpha_composite(background, text_layer)

    try:
        # Save the image using open() and file write
        print(f"Saving image to {output_image}")
        combined.save(output_image)
        print(f"Image successfully saved as {output_image}")
    except Exception as e:
        print(f"Error saving image to {output_image}: {e}")

# Usage Example
lyric_text = "This is a sample lyric text that will be wrapped and centered."
font_file = "font.ttf"  # Path to your custom font
background_image = "background.jpg"  # Path to your background image
output_image = "output_frame.png"  # Path to save the generated image

# Render the image with the lyric text
render_lyric_frame(lyric_text, font_file, background_image, output_image)
