import os
import time
from pytube import YouTube
from pytubefix import YouTube # This is solution
import logging

logging.basicConfig(
    filename='download_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Custom log function
def log(message, level='info'):
    """
    Custom logging function to simplify logging calls.
    
    Parameters:
        message (str): The log message.
        level (str): The log level (default is 'info'). Can be 'info', 'error', 'warning', etc.
    """
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'debug':
        logging.debug(message)
    else:
        logging.info(message)  # Default to info if an unknown level is provided

def get_video_link_from_console():
    link = input("Enter YouTube video URL: ")
    return link

def get_download_folder():
    working_directory = os.getcwd()  # Get current working directory
    downloads_folder = os.path.join(working_directory, 'downloads')
    
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)  # Create 'downloads' folder if it doesn't exist

    return downloads_folder

def download_video(link, downloads_folder):
    try:
        yt = YouTube(link)
        log(f"Started downloading: {yt.title}")
        yd = yt.streams.get_highest_resolution()
        yd.download(downloads_folder)
        log(f"Download complete: {yt.title}")

    except Exception as e:
        log(f"An error occurred: {e}")
        time.sleep(5)  # Wait for 5 seconds before potentially retry
        
def get_video_links_from_file(filename="links.txt"):
    links = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Ignore lines that are empty or start with '#' (comments)
                if line.strip() and not line.startswith('#'):
                    links.append(line.strip())  # Add valid links to the list
        log(f"Read {len(links)} links from {filename}")  # Log the number of valid links read
        return links
    except FileNotFoundError:
        log(f"File {filename} not found.", level='error')  # Log error if file is not found
        return []

def download_videos(links, downloads_folder):
    for link in links:
        download_video(link, downloads_folder)  
        
def choose_download_option():
    print("Select download option:")
    print("1. Download a single video")
    print("2. Download videos from links.txt")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        return 'single'
    elif choice == '2':
        return 'multiple'
    else:
        print("Invalid choice, defaulting to single video.")
        return 'single'  

def main():
    downloads_folder = get_download_folder() # Define the working directory and create a 'downloads' folder if it doesn't exist

    
    download_option = choose_download_option()

    if download_option == 'single':
        link = get_video_link_from_console()  # Get a single YouTube video URL
        download_video(link, downloads_folder)  # Download the video
    
    elif download_option == 'multiple':
        links = get_video_links_from_file()  # Get video links from file
        if links:
            download_videos(links, downloads_folder)  # Download all videos from the file
# Run the main function
if __name__ == "__main__":
    main()