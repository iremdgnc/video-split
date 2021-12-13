from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def video_split(required_video_file,txt_file):
    with open(txt_file) as f:
        times = f.readlines()

    times = [x.strip() for x in times]

    for time in times:
        start_time = int(time.split("-")[0])
        end_time = int(time.split("-")[1])
        ffmpeg_extract_subclip(required_video_file, start_time, end_time, targetname=str(times.index(time) + 1) + ".mp4")


if __name__ == '__main__':
    video_split(
        required_video_file='',
        txt_file=''
    )

