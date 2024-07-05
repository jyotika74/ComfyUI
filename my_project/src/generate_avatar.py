from avatars.core.avatar import Avatar

def generate_avatar():
    try:
        # Create an instance of Avatar
        avatar = Avatar(name='Test Avatar')
        
        # Generate and save the avatar using the generate method
        avatar.generate(filename='avatar.png')
        print("Avatar generated and saved as avatar.png")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_avatar()
