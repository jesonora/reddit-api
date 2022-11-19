import requests
import pandas as pd
import numpy as np

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_pushshift_data(**kwargs):
    """
    Gets data from the pushshift api.

    data_type can be 'comment' or 'submission'
    The rest of the args are interpreted as payload.

    Read more: https://github.com/pushshift/api
    """

    base_url = "https://api.pushshift.io/reddit/search/comment/"
    payload = kwargs
    print(payload)
    request = requests.get(base_url, params=payload)
    return request.json()


def sentiment_scores(*sentence):
    """
    Gets polarization score using VADER (Valence Aware Dictionary
    and Sentiment Reasoner)

    Read more: https://github.com/cjhutto/vaderSentiment

    :param sentence: content to add score
    """

    obj = SentimentIntensityAnalyzer()

    return [obj.polarity_scores(sente)["compound"] for sente in sentence]


def get_comment_df(
    subreddit: str,
    size: int = 25,
    after: str = None,
    before: str = None,
    sort_by: str = "created_utc",
):
    """
    Given a set of comments, it returns the polarization score and the
    class of the comment, positive or negative.

    :param subreddit: subreddit name
    :param size: number of comments to return
    :param after: Return results after this date
    :param before: Return results before this date
    :param sort_by: sort by date or by score
    """

    data = get_pushshift_data(
        size=size,
        subreddit=subreddit,
        sort_type="created_utc",
        sort="desc",
        after=after,
        before=before,
    )

    if len(data["data"]) > 0:
        df = pd.DataFrame.from_records(data["data"])
        df = df[["id", "author", "created_utc", "body"]]

        df["created_utc"] = pd.to_datetime(
            df["created_utc"], unit="s", utc=True
        ).dt.tz_convert("Europe/Berlin")

        df["compound"] = sentiment_scores(*df["body"].values)
        df["class"] = np.where(df["compound"] > 0, "Positive", "Negative")

        df.sort_values(by=sort_by, ascending=False, inplace=True)

        df = df[["id", "body", "compound", "class"]]

        return df.to_dict("records")

    else:
        return None
