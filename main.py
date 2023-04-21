from src.statistics import getFollowers, getFollowings
from src.tables import createTable


def main():
    followers = createTable('Followers', getFollowers())
    followings = createTable('Followings', getFollowings())

    followers.display()
    followings.display()


if __name__ == '__main__':
    main()
