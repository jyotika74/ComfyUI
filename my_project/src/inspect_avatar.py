from avatars.core.avatar import Avatar

def inspect_avatar_class():
    avatar = Avatar()
    print("Available methods in Avatar class:")
    for method in dir(avatar):
        if callable(getattr(avatar, method)):
            print(method)

if __name__ == "__main__":
    inspect_avatar_class()
