from ebaysdk.finding import Connection
from polls.twitterPositivity import *

def search(searchQuery):
    api = Connection(config_file='polls/templatetags/ebay.yaml', debug=True, siteid = "EBAY-IN")

    #searchQuery = 'pillows'
    request = {
        'keywords': str(searchQuery),
        'paginationInput': {
            'entriesPerPage': 10,
            'pageNumber': 1
        },

    }

    response = api.execute('findItemsByKeywords', request)

    products = []
    for item in response.reply.searchResult.item:
        eachProduct = {}
        eachProduct["title"] = item.title
        eachProduct['TweetRate'] = twitterRating(item.title)
        eachProduct["price"] = item.sellingStatus.currentPrice.value
        eachProduct["imgURL"] = item.galleryURL
        eachProduct["productURL"] = item.viewItemURL
        products.append(eachProduct)

    return products
