# YouTube Video Downloader

This Python script allows you to download YouTube videos, either individually or from a list of URLs provided in a text file. It utilizes the `pytube` and `pytubefix` libraries for video downloading and includes robust logging to track the download process.

## Prerequisites

Before running the script, ensure you have the following installed:

* Python 3.x
* `pytube` and `pytubefix`:
    ```bash
    pip install pytube pytubefix
    ```

## Installation

1.  Clone the repository (or download the script directly):

    ```bash
    git clone [repository URL] # If you have a repository
    cd [script directory]
    ```

## Usage

1.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

2.  **Choose Download Option:**

    * The script will prompt you to select a download option:
        * `1`: Download a single video.
        * `2`: Download videos from `links.txt`.
    * If you select option 1, you will be prompted to enter a YouTube video URL.
    * If you select option 2, the script will read video URLs from a file named `links.txt` in the same directory.

3.  **`links.txt` File (for multiple downloads):**

    * Create a file named `links.txt` in the same directory as the script.
    * Add one YouTube video URL per line.
    * You can add comments by starting a line with `#`. Empty lines will be ignored.
    * Example `links.txt` content:
        ```
        [https://www.youtube.com/watch?v=VIDEO_ID_1](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DVIDEO_ID_1)
        [https://www.youtube.com/watch?v=VIDEO_ID_2](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DVIDEO_ID_2)
        # This is a comment
        [https://www.youtube.com/watch?v=VIDEO_ID_3](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3DVIDEO_ID_3)
        ```

4.  **Download Location:**

    * The downloaded videos will be saved in a folder named `downloads` within the script's working directory. If the folder doesn't exist, it will be created automatically.

5.  **Logging:**

    * The script logs all download activity and any errors to a file named `download_log.txt`.

## Script Details

* **`download_video(link, downloads_folder)`:** Downloads a single video from the given URL to the specified folder.
* **`get_video_links_from_file(filename="links.txt")`:** Reads video URLs from the `links.txt` file.
* **`get_download_folder()`:** Creates the `downloads` folder if it doesn't exist.
* **`get_video_link_from_console()`:** Prompts the user to enter a YouTube video URL.
* **`download_videos(links, downloads_folder)`:** Downloads all videos from the provided list of links.
* **`choose_download_option()`:** Prompts the user to choose between single and multiple video downloads.
* **`log(message, level='info')`:** Custom logging function that writes to `download_log.txt`.

## Error Handling

* The script includes error handling to catch exceptions during the download process.
* It logs all errors to `download_log.txt`.

## Notes

* The script uses `pytubefix` to help mitigate some issues that may arise with the base `pytube` library.
* Ensure you have a stable internet connection for successful downloads.
* Be mindful of YouTube's terms of service regarding downloading videos.
* The script downloads the highest resolution stream available.
* The script downloads the highest resolution stream available.