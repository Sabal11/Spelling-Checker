from textblob import TextBlob
def spell_checker_function(input_text):
    try:
        # Create a TextBlob object
        blob = TextBlob(input_text)

        # Correct spelling for each word in the text
        corrected_words = [word.correct() for word in blob.words]

        # Combine corrected words into a sentence
        corrected_text = ' '.join(corrected_words)

        return corrected_text

    except Exception as e:
        # Handle exceptions and return an error message
        return f"Error during spelling correction: {str(e)}"