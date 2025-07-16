#!/usr/bin/env python3
import instaloader
import getpass
import sys

def download_instagram_posts():
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    
    # Login
    username = "srtbgb"
    password = getpass.getpass(f"Enter Instagram password for {username}: ")
    
    try:
        L.login(username, password)
        print(f"Successfully logged in as {username}")
        
        # Download posts from wrap_my_ride_
        print("Downloading posts from wrap_my_ride_...")
        profile = instaloader.Profile.from_username(L.context, "wrap_my_ride_")
        
        # Download all posts
        for post in profile.get_posts():
            L.download_post(post, target="wrap_my_ride_posts")
            
        print("Download completed!")
        
    except instaloader.exceptions.InvalidArgumentException:
        print("Invalid username or password")
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_instagram_posts()