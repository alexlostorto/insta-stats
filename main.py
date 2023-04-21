from src.statistics import getFollowers, getFollowings
from src.tables import createTable


def main():
    followers = createTable('Followers', getFollowers())
    following = createTable('Followings', getFollowings())

    following.display()


if __name__ == '__main__':
    main()
