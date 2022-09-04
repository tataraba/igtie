# Define interface for all user actions/behaviors related to authentication


async def get():
    """Returns user based on given user id."""
    pass


async def get_by_email():
    """Return user based on user's email."""
    pass


async def create_user():
    """Create a new igtie user."""
    pass


async def get_or_create_user():
    """Gets existing user, if one not found, creates a new one."""
    pass


async def update_user():
    """Update user info."""
    pass
