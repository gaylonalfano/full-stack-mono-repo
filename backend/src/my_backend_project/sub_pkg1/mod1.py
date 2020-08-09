"""
NOTES:
    - Even after adding __init__.py to both of my subpackages still ModuleNotFound
    - Even changing the import syntax (import vs. from my_backend_project import settings)
      it still doesn't work.
    - Yep, as long as 'my_backend_project' isn't installed as a package, none of the
      subpackages or modules can be recognized/imported.
    - I have NOT done the 'python -m pip install -e my_backend_project .' from ROOT (backend)
    - Gonna do the install -e and see... WORKS!

"""
# Let's test my settings import
# import my_backend_project.settings  # ModuleNotFound 'my_backend_project'
from my_backend_project import settings  # ModuleNotFound 'my_backend_project'


secret = settings.SECRET_FROM_SETTINGS
print(secret)  # works!
# # Let's see if secret and settings shows up in dir()
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'secret', 'settings']

# Let's try importing a sibling subpackage
from my_backend_project.sub_pkg2 import mod3  # ModuleNotFound 'my_backend_project'

print(mod3.baz())


def foo():
    print("[mod1] foo()")


class Foo:
    pass
