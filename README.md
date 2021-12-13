# Video Split
* Creates a new video from a desired interval of the video.

## Project Layout
    video_split/   # folder containing files
        main.py    # python file where the video split takes place
        times.txt  # File containing the time period in which a new video was requested to be created.
        README.md
    
## Functions

    video_split/
        main.py
            def video_split()  # video splitting takes place.
## Function Descriptions
### video split
`def video_split(required_video_file,txt_file)`

txt file is read and the time interval to be split is taken.A video is created in the specified format using "ffmpeg_extract_subclip".

*ARGS*
* **required_video_file:** The original video path where the new video will be created.
* **txt_file:** txt file with time range of new video.

*EXAMPLE USAGE*

    video_split(
        required_video_file='',
        txt_file=''
    )
