from src.response import makeRequest


options = {
    'followers': {
        'hash': 'c76146de99bb02f6415203be841dd25a',
        'path': 'edge_followed_by'
    },
    'following': {
        'hash': 'd04b0a864b4b54837c0d870b0e77e076',
        'path': 'edge_follow'
    }
}


def convert(iterable):
    return [iterable['node']['username'], iterable['node']['full_name']]


def getFollowers():
    return list(map(convert, makeRequest(options['followers'])))


def getFollowings():
    return list(map(convert, makeRequest(options['following'])))
