def cleanup_text(text):
    """Do naive text cleanup

    TODO: make this nicer/customisable
    """

    # Convert linebreaks to HTML breaks
    text = text.replace("\n", "<br>")

    # Remove '[CLICK]' actions
    text = text.replace("[CLICK]", "")

    return text
