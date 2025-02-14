"""
    Single point of entry for any post-processing required on the output of the Azure hosted ML model.
    This module creates a separation between post-processing and the API logic.
"""


def process_model_output(model_output: int) -> int:
    # Placeholder for complex logic
    rescaled_output = rescale_by_user(model_output)
    save_rating_to_db(rescaled_output)
    return rescaled_output


def rescale_by_user(output: int) -> int:
    """Rescales the user's rating, based on how they rate on average"""
    pass
    return output


def save_rating_to_db(data: int) -> None:
    """Saves the scaled rating to the DB (maybe should be in a separate DB module)"""
    # Save to DB
    # Update average rating using rescaled review
    pass
