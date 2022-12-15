import argparse

from publisher import publish_to_reddit

parser = argparse.ArgumentParser()
parser.add_argument("-yt", "--youtube_link")

args = parser.parse_args()

if args.youtube:
    video = scrape_video_from_youtube(args.youtube_link)
    publish_to_reddit(video)
