from camlib import response


@response()
def notice_order_finish(_):
    return {
        "errorItems": [0],
        "message": "woohoo",
        "available": 0,
        "fixOrderText": "Your order is finished congratulations omg",
        "messageBoardText": "YEAHHH",
    }
