from datetime import datetime, date, timedelta, timezone
import pytz
import logging

# import dotenv

from twitter import ManageTwitter


class MakeTweet:
    def __init__(self):
        self.START_DATE = date.fromisoformat('2020-04-27')
        self.JST = pytz.timezone('Asia/Tokyo')

    def calc_remaining_days(self):
        today = datetime.now()
        today.astimezone(self.JST)
        remaining = self.START_DATE - today.date()
        return remaining.days

    def get_tweet_text(self):
        remaining_days = self.calc_remaining_days()
        tweet_text = '「約1ヶ月後に始まる授業」\n'\
            f'授業まであと{remaining_days}日'
        return tweet_text


def main():
    log_fmt = '%(asctime)s  :%(message)s'
    logging.basicConfig(
        filename='../log/logger.log',
        format=log_fmt,
        level=logging.INFO
    )
    logging.info('start')

    make_tweet = MakeTweet()
    tweet_text = make_tweet.get_tweet_text()

    manage_twitter = ManageTwitter()
    manage_twitter.post_tweet(tweet_text)

    logging.info('finish')


if __name__ == "__main__":
    main()
