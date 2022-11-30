from django.shortcuts import render
from django.shortcuts import render, redirect
from accounts.models import userRegistration
from alice_blue import *
from django.http import HttpResponse, JsonResponse
import requests
import websocket
import time
import json
from .helper import placeBuyOrder, placeSellOrder, getOrderDetails
from .models import chatLogs, userChatLogs, systemChatLogs
import pandas as pd
from asgiref.sync import sync_to_async, async_to_sync
import asyncio


def index(request):
    chatLogContext = list(chatLogs.objects.values().filter(username = request.user.username))
    return render(request, 'index.html', {'chatLogContext': chatLogContext})

def brokerDetails(request):
    if request.user.is_authenticated:
        data_json = {
        'status': 'success',
        'brokerUserId': userRegistration.objects.get(username = request.user.username).brokerUserId,
        'brokerPwd': userRegistration.objects.get(username = request.user.username).brokerPwd,
        'brokerSecretKey': userRegistration.objects.get(username = request.user.username).brokerSecretKey,
        'brokerAppId': userRegistration.objects.get(username = request.user.username).brokerAppId,
        'brokerTwoFA': userRegistration.objects.get(username = request.user.username).brokerTwoFA
        }
        return data_json
    else:
        err_data_json = {
        'status': 'failed',
        'reason': 'invalid user'
        }
        return err_data_json


@sync_to_async
def placeOrder(request):
    if request.method == 'POST':
        orderCode = request.POST['orderCode']
        print(orderCode)

        # Order Code Structure:
        # TYPE SYMBOL QTY PRICE
        # Eg: BUY SBIN 50 520

        orderCodeToList = orderCode.split(' ')
        print(orderCodeToList)
        while True:
            time.sleep(2)
            # url = 'http://127.0.0.1:8000/chatLogsJson'
            # r = requests.get(url)
            # data_json = r.json()
            system_chat = symbol = oms_id = price = product = quantity = filled_quantity = order_status = rejection_reason = type = ''
            if orderCodeToList[0] == 'BUY':
                orderPlaced = placeBuyOrder(orderCodeToList[1], int(orderCodeToList[2]), float(orderCodeToList[3]))
                oms_order_id = orderPlaced['data']['oms_order_id']
                orderDetails = getOrderDetails(oms_order_id)
                symbol = orderDetails['data'][0]['trading_symbol']
                type = 'Buy'
                oms_id = orderDetails['data'][0]['oms_order_id']
                price = orderDetails['data'][0]['price_to_fill']
                product = orderDetails['data'][0]['product']
                quantity = orderDetails['data'][0]['quantity']
                filled_quantity = orderDetails['data'][0]['filled_quantity']
                order_status = orderDetails['data'][0]['order_status']
                rejection_reason = orderDetails['data'][0]['rejection_reason']
                print(orderDetails)
                system_chat = f'Bought {orderCodeToList[2]} stocks of {orderCodeToList[1]} at Rs. {float(orderCodeToList[3])}'
            elif orderCodeToList[0] == 'SELL':
                orderPlaced = placeSellOrder(orderCodeToList[1], int(orderCodeToList[2]), float(orderCodeToList[3]))
                oms_order_id = orderPlaced['data']['oms_order_id']
                orderDetails = getOrderDetails(oms_order_id)
                symbol = orderDetails['data'][0]['trading_symbol']
                type = 'Sell'
                oms_id = orderDetails['data'][0]['oms_order_id']
                price = orderDetails['data'][0]['price_to_fill']
                product = orderDetails['data'][0]['product']
                quantity = orderDetails['data'][0]['quantity']
                filled_quantity = orderDetails['data'][0]['filled_quantity']
                order_status = orderDetails['data'][0]['order_status']
                rejection_reason = orderDetails['data'][0]['rejection_reason']
                # print(orderDetails)
                system_chat = f'Sold {orderCodeToList[2]} stocks of {orderCodeToList[1]} at Rs. {float(orderCodeToList[3])}'

            userChatLogs.objects.create(username = request.user.username,
                                        user_chat = orderCode)
            systemChatLogs.objects.create(username = request.user.username,
                                        system_chat = system_chat,
                                        symbol = symbol,
                                        type = type,
                                        oms_order_id = oms_id,
                                        price = price,
                                        product = product,
                                        quantity = quantity,
                                        filled_quantity = filled_quantity,
                                        order_status = order_status,
                                        rejection_reason = rejection_reason)

            chatLogs.objects.create(username = request.user.username,
            user_chat = orderCode,
            system_chat = system_chat,
            symbol = symbol,
            type = type,
            oms_order_id = oms_id,
            price = price,
            product = product,
            quantity = quantity,
            filled_quantity = filled_quantity,
            order_status = order_status,
            rejection_reason = rejection_reason)

        return redirect('/')

# async_function = sync_to_async(placeOrder, thread_sensitive=False)

# ws = websocket.WebSocket()
# ws.connect('ws://127.0.0.1:8000/ws/polData/')

# def dbSocketTest():
#     while True:
#         data_json = list(chatLogs.objects.values().filter(username = request.user.username))
#         ws.send(json.dumps(data_json))
#         time.sleep(2)

# dbSocketTest()

def chatLogsJson(request):
    data_json = list(chatLogs.objects.values().filter(username = request.user.username))
    return JsonResponse(data_json, safe = False)

def userChatLogsJson(request):
    data_json = list(userChatLogs.objects.values().filter(username = request.user.username))
    return JsonResponse(data_json, safe = False)

def systemChatLogsJson(request):
    data_json = list(systemChatLogs.objects.values().filter(username = request.user.username))
    return JsonResponse(data_json, safe = False)

def chatApp(request):
    while True:
        time.sleep(2)
        url = 'http://127.0.0.1:5000/chatLogsJson'
        r = requests.get(url)
        data_json = r.json()
        # return redirect('/chatApp')
        return render(request, 'chat.html')

def realTime(request):
    return render(request, 'realtime.html')


def dataBackup(request):
    dataObj = list(chatLogs.objects.values().all())
    return JsonResponse(dataObj, safe = False)
    # print(dataObj)
    # df = pd.DataFrame(data=dataObj)
    # df = (df.T)
    # df.to_excel('dict4.xlsx')

def fetchDataTest():
    url = 'http://127.0.0.1:8000/dataBackup'
    r = requests.get(url)
    api_data = r.json()
    return api_data


def userData(request):
    username = request.user.username
    data_json = {
    'username': username
    }

    return JsonResponse(data_json, safe = False)
