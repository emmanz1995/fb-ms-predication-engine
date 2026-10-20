from fastapi import Request, HTTPException

def token_extractor(request: Request) -> str:
  """
  This helper function is used to extract
  the access token from the authorization header
  """
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
  
  return token