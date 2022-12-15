from praw import Reddit

from floripa_chess_hustlers import secrets
from floripa_chess_hustlers.models import Youtube


def publish_to_reddit(post: Youtube) -> None:
    reddit = Reddit(
        client_id=secrets.REDDIT_CLIENT_ID,
        client_secret=secrets.REDDIT_CLIENT_SECRET,
        password=secrets.REDDIT_CLIENT_PASSWORD,
        user_agent=f"testscript by u/{secrets.REDDIT_USERNAME}",
        username=secrets.REDDIT_USERNAME
    )

    subreddit = reddit.subreddit("xadrez")
    subreddit.submit(title=post.title, url=post.url)
