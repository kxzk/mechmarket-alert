import re
from functools import reduce
from operator import or_
from typing import Optional, Set


def contains_any(post: str, keywords: Set[str]) -> bool:
    if post := extract_selling(post):
        keywords_ = {keyword.upper() for keyword in keywords}
        return reduce(or_, map(post.upper().__contains__, keywords_))
    else:
        return False


def extract_selling(post: str) -> Optional[str]:
    if match := re.search("(\[H\])([^;]*)(\[W\])", post):
        return match.group(0)
