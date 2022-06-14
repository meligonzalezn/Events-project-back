

from urllib.request import Request


def is_logged(request: Request):
  """
  check if an user is logged.\n
  @return is_logged: bool
  """
  try:
    if(request.session.get('member_id') is not None):
      print("member_id", request.session.get('member_id'))
      return True
  except:
    return False