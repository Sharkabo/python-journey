from typing import Any, Callable
from functools import wraps

CURRENT_USER_ROLE: str = "guest"

def admin_required(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if CURRENT_USER_ROLE == 'admin':
            result: Any = func(*args, **kwargs)
            return result
        else:
            print('Access Denied')
            return None
    return wrapper

@admin_required
def nuke_system() -> None:
    print('Launching Nukes')

nuke_system(CURRENT_USER_ROLE)
CURRENT_USER_ROLE = "admin"
nuke_system(CURRENT_USER_ROLE)