import requests
from alice_blue import *
from django.http import HttpResponse, JsonResponse
from accounts.models import userRegistration

# user = '213802'
# pwd = 'Password@12345'
# # secret = 'i4aY6DGMZjVOaLTnO7gKqull6npwCL3uhGtbKPJE7v5RJgsKPUO918eGCQUvwepg'
# secret = '56HdDOWnRcBXgp1xe7mHKywXEMXYeWXHiOlg9YLI9eufpkOwToJp8at9OVWnNf8a'
# # appid = 'cOJykqaaG4'
# appid = 'DPkcLHmCWB'
# access_token = AliceBlue.login_and_get_access_token(username=user, password=pwd, twoFA='1973', api_secret=secret, app_id=appid)
# alice = AliceBlue(username=user, password=pwd, access_token=access_token)

### Place BUY order subroutine
def placeBuyOrder(symbol, qty, prc):
    return alice.place_order(transaction_type = TransactionType.Buy,
                     instrument = alice.get_instrument_by_symbol('NSE', symbol),
                     quantity = qty,
                     order_type = OrderType.Market,
                     product_type = ProductType.Intraday,
                     price = prc,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)


def placeSellOrder(symbol, qty, prc):
    return alice.place_order(transaction_type = TransactionType.Sell,
                     instrument = alice.get_instrument_by_symbol('NSE', symbol),
                     quantity = qty,
                     order_type = OrderType.Market,
                     product_type = ProductType.Intraday,
                     price = prc,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)

def getOrderDetails(oms_order_id):
    return alice.get_order_history(oms_order_id)
