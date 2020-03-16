from datetime import date
import logging

# import dotenv

from twitter import ManageTwitter


class MakeTweet:
    START_DATE = date.fromisoformat('2020-04-27')

    def calc_remaining_days(self):
        today = date.today()
        remaining = self.START_DATE - today
        return remaining.days

    def get_tweet_text(self):
        remaining_days = self.calc_remaining_days()
        tweet_text = '「約1ヶ月後に始まる授業」\n'\
            f'授業まであと{remaining_days}日'
        return tweet_text


def main():
    # log_fmt = '%(asctime)s  :%(message)s'
    # logging.basicConfig(
    #     filename='../log/logger.log',
    #     format=log_fmt,
    #     level=logging.INFO
    # )
    # logging.info('start')
    print('start')

    make_tweet = MakeTweet()
    tweet_text = make_tweet.get_tweet_text()
    print(tweet_text)

    manage_twitter = ManageTwitter()
    manage_twitter.post_tweet(tweet_text)

    # logging.info('finish')
    print('start')


if __name__ == "__main__":
    main()
