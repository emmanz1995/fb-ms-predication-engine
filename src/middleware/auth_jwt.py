from fastapi import Request, HTTPException
# import jwt
# import os

# I just need a way to extract jwt token from request header
def auth_jwt(request: Request) -> str:
  # public_key = os.environ.get("AUTH_PUBLIC_KEY")
  
  authorization = request.headers.get("Authorization")
  
  if not authorization:
    raise HTTPException(
      status_code=401,
      detail="Failed due to missing authorization header"
    )
  
  separate_bearer = authorization.split("Bearer ")
  
  if len(separate_bearer) < 2:
    raise HTTPException(
      status_code=401,
      detail="Failed to get Bearer token"
    )
  
  token = separate_bearer[-1]
  
  
  # try:
  #   decode_token = jwt.decode(
  #     token, 
  #     public_key.replace("\\n", "\n"),
  #     algorithms=["RS256"],
  #     issuer=os.environ.get("JWT_ISSUER"),
  #     audience=os.environ.get("JWT_AUDIENCE")
  #   )
    
  # except jwt.InvalidTokenError as e:
  #   raise HTTPException(
  #     status_code=401, 
  #     detail="Failed to extract token"
  #   ) from e
    
  
  request.state.token = token
  
  return token
  