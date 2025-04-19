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

def login(login_request: dict(LoginRequest)):
    """ Log in a user. """
    # Check if the user exists
    user = user_db.get_user_by_email(login_request['email'])
    if not user:
        return {"error": "User not found"}, 404
    
    # Check if the password is correct
    if not user_db.check_password(user['user_id'], login_request['password']):
        return {"error": "Invalid password"}, 401
    
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
    return user_response, 200

def get_user(user_id: str):
    """ Get user data by user_id. """
    # Check if the user exists
    user = user_db.get_user_by_id(user_id)
    if not user:
        return {"error": "User not found"}, 404
    
    # Return the user data
    user_response = UserResponse(
        user_id=user['user_id'],
        name=user['name'],
        email=user['email'],
        created_at=user['created_at']
    )
    return user_response, 200

def get_all_users():
    """ Get all users. """
    # Get all users
    users = user_db.get_all_users()
    if not users:
        return {"error": "No users found"}, 404
    
    # Return the user data
    user_responses = [
        UserResponse(
            user_id=user['user_id'],
            name=user['name'],
            email=user['email'],
            created_at=user['created_at']
        ) for user in users
    ]
    return user_responses, 200

 