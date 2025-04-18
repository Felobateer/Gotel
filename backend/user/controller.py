import user.db as user_db
from user.interfaces import SignupRequest, LoginRequest, UserResponse, UserResponseWithToken


def signup(new_user: dict(SignupRequest)):
    """ Sign up a new user. """
    # Check if the user already exists
    if user_db.get_user_by_email(new_user['email']):
        return {"error": "User already exists"}, 400
    
    # Create the user
    user = user_db.create_user(new_user)
    if not user:
        return {"error": "Failed to create user"}, 500
    # Generate a token for the user
    token = user_db.generate_token(user['user_id'])
    if not token:
        return {"error": "Failed to generate token"}, 500
    
    # Return the user data and token
    user_response = UserResponseWithToken(
        user=UserResponse(
            user_id=user['user_id'],
            name=user['name'],
            email=user['email'],
            created_at=user['created_at']
        ),
        token=token,
        created_at=user['created_at']
    )
    return user_response, 201

