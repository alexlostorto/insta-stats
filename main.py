from src.statistics import getFollowers, getFollowings
from src.tables import createTable


def main():
    followersList = getFollowers()
    followingsList = getFollowings()
    dontFollowBack = [f for f in followingsList if f not in followersList]

    followers = createTable('Followers', followersList)
    followings = createTable('Followings', followingsList)
    nonFollowers = createTable('Non-Followers', dontFollowBack)

    followers.display()
    followings.display()
    nonFollowers.display()


if __name__ == '__main__':
    main()
