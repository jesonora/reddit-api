"""Endpoints for health check and getting version information"""
import logging
from typing import Any, Union

from fastapi import APIRouter, Query

from ..configs import get_settings
from .comments import get_comment_df

settings = get_settings()
logger = logging.getLogger(settings.PROJECT_SLUG)

base_router = APIRouter()


@base_router.get("/scores/{subreddit}")
async def get_scores(
    subreddit: str,
    after: Union[str, None] = Query(
        default=None,
        description="Return results after this date, Epoch value or Integer + 's,m,h,d' (i.e. 30d for 30 days)",
    ),
    before: Union[str, None] = Query(
        default=None,
        description="Return results before this date, Epoch value or Integer + 's,m,h,d' (i.e. 30d for 30 days)",
    ),
    sort_by: str = Query(
        default="created_utc",
        description="Sort by `created_utc` or `compound` (polarization score) descending.",
    ),
) -> Any:
    """
    Provide the top 25 comments of a subreddit with a polarization score, ordered by creation date.

    Returns a JSON with the following structure:
    ```
    [{'id': 1, 'body': 'Some comments', 'compound': 0.5 , 'class': 'Positive'},
     {'id': 2, 'body': 'Some comments of other', 'compound': -0.1 , 'class': 'Negative'}]
    ```
    """

    response = get_comment_df(
        subreddit=subreddit, after=after, before=before, sort_by=sort_by
    )

    if response is not None:
        return response
    else:
        return f"The subreddit {subreddit} does not have results"
