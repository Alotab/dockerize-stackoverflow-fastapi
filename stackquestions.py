#!/usr/bin/env python
import fire
from soflogic.stackoverflow import get_questions, fetch_users

if __name__ == "__main__":
    fire.Fire(get_questions)
    fire.Fire(fetch_users)
