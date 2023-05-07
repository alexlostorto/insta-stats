from src.statistics import getFollowers, getFollowings
from src.tables import createTable


def main():
    followers_list = getFollowers()
    followings_list = getFollowings()
    dont_follow_back = []

    for following in followings_list:
        if following not in followers_list:
            dont_follow_back.append(following)

    followers = createTable('Followers', followers_list)
    followings = createTable('Followings', followings_list)
    non_followers = createTable('Non-Followers', dont_follow_back)

    followers.display()
    followings.display()
    non_followers.display()


if __name__ == '__main__':
    main()
