

from django.core.cache import cache


def is_logged() -> bool:
  """
  check if an user is logged.\n
  @return is_logged: bool
  """
  try:
    print("Xd", cache.get('member_id'))
    if(cache.get('member_id') is not None):
      return True
    return False
  except:
    return False