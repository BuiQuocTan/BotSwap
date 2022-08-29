import time
import math
from web3 import Web3
import requests
import sys

token = '' #token sell 
banduoc = 1000
slippay = 1
gass =3000
my_pkey = '' #private key
# w4 =Web3(Web3.HTTPProvider('https://rpc1.ftm.tools/'))  
w4 = Web3(Web3.HTTPProvider('https://rpc.ftm.tools/'))

def lamtron(number:float, decimals:int=2): 
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)
    factor = 10 ** decimals
    return math.floor(number * factor) / factor

my_address = '' #my_address
contract_token = w4.eth.contract(address = w4.toChecksumAddress(token),abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
contract_router = w4.eth.contract(address='0x16327E3FbDaCA3bcF7E38F5Af2599D2DDc33aE52',abi ='[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')

def telegram_bot_sendtext3(bot_message):    
     bot_token = '1786278695:AAFkaIJv9bvsYrUS1r0OiMOcDL2wAJzc5z4'
     bot_chatID = '-526856728'
     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
     response = requests.get(send_text)
     return response.json()  
def token_name(address):
    contract_address = w4.eth.contract(address = w4.toChecksumAddress(address), abi ='[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"setBurner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    symbol = contract_address.functions.symbol().call()
    decimal = contract_address.functions.decimals().call()
    return {'name':symbol,
            'decimal':decimal}

coin = token_name(token)['name']
decimal = token_name(token)['decimal']
print('decimal: ',decimal)


def approve():
    tx = contract_token.functions.approve('0x10ED43C718714eb63d5aA57B78B54704E256024E',int(115792089237316195423570985008687907853269984665640564039457584007913129639935)).buildTransaction({"from": my_address,"value": int(0 * 10 ** 18),'gasPrice': int((6)*10**9),"gas": 400000,"nonce":w4.eth.getTransactionCount('0x8039f3Aa709FEC29fdC5f075449b23Ab609a6998') })
    signed_tx = w4.eth.account.sign_transaction(tx, private_key=my_pkey)
    tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(w4.toHex(tx_hash))

    while True:
        try:
            receipt = w4.eth.waitForTransactionReceipt(tx_hash, timeout=1000)
            eee=receipt['status']
            print(eee)
            if eee==0:
                telegram_bot_sendtext3(f'FAIL lenh ban {coin} pancake')
                print ("lenh BAN pancake da failed")
                sys.exit()
            else:
                print("lenh BAN pancake da khop")
                sys.exit()
        except Exception as e:
            print(e)
            receipt = w4.eth.waitForTransactionReceipt(tx_hash, timeout=2000)
            eee=receipt['status']
            print(eee)
            if eee==0:
               telegram_bot_sendtext3(f'FAIL lenh ban {coin} tren pancake ETH')
               print ("lenh BAN pancake da failed")
               sys.exit()
            else:
               print("lenh BAN pancake da khop")
               sys.exit()
# approve()
# sys.exit()  
def sell_spirit_fusdt():
    print(coin)
    balance = lamtron( contract_token.functions.balanceOf(my_address).call()/10**decimal,2)
    print('balance ',balance)
    aa =int(balance*10**decimal)
    print(aa)
    path = [w4.toChecksumAddress(token),'0x049d68029688eAbF473097a2fC38ef61633A3C7A'] #'0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    if balance > 0.5:
        time.sleep(0.5)
        quoter =round( contract_router.functions.getAmountsOut(aa,path).call()[1]/10**6,2)
        print(type(quoter))
        print('ban duocccccccccccccccccccccccccc ', quoter)
        if quoter > banduoc:
            noncee = w4.eth.getTransactionCount('0x8039f3Aa709FEC29fdC5f075449b23Ab609a6998')
            # print('nonceeeeee',noncee)
            deadline = int(time.time()) +1000
            fn = contract_router.functions.swapExactTokensForTokens(aa, int(quoter*0.997*10**6), path, my_address, deadline).buildTransaction(
                {
            "chainId":250,
            "from": my_address,
            "value": int(0 * 10 ** 18),
            'gasPrice': int(gass*10**9),
            "gas": 400000,
            "nonce":noncee })
            signed_tx = w4.eth.account.sign_transaction(fn, private_key=my_pkey)
            tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(w4.toHex(tx_hash))
            while True:
                try:
                    receipt = w4.eth.waitForTransactionReceipt(tx_hash, timeout=1000)
                    eee=receipt['status']
                    print(eee)
                    if eee==0:
                        telegram_bot_sendtext3(f'FAIL lenh ban {coin} SPIRIT')
                        print ("lenh BAN spirit da failed")
                        sell_spirit_fusdt()
                        sys.exit()
                    else:
                        telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren SPIRIT  {quoter}')
                        print("lenh BAN spirit da khop")
                        sys.exit()
                except Exception as e:
                    print(e)
                    receipt = w4.eth.waitForTransactionReceipt(tx_hash, timeout=2000)
                    eee=receipt['status']
                    print(eee)
                    if eee==0:
                       telegram_bot_sendtext3(f'FAIL lenh ban {coin} tren spirit bsc')
                       print ("lenh BAN spirit da failed")
                       sys.exit()
                    else:
                       telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren spirit  {quoter}')
                       print("lenh BAN spirit da khop")
                       sys.exit()
        else:
            print('-----------------')
            print("BAN BANG TAYYYYYYYYYYYYY")
    else:
        print("chua co so du, chua ban dc")
        time.sleep(0.5)
# approve()
def sell_spirit():
    print(coin)
    balance =lamtron( contract_token.functions.balanceOf(my_address).call()/10**decimal,2)
    print('balance ',balance)
    aa =int(balance*10**decimal)
    print(aa)
    path = [w4.toChecksumAddress(token),'0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83','0x049d68029688eAbF473097a2fC38ef61633A3C7A'] #'0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    if balance > 0.5:
        time.sleep(0.5)
        quoter =round( contract_router.functions.getAmountsOut(aa,path).call()[2]/10**6,2)
        print(type(quoter))
        print('ban duocccccccccccccccccccccccccc ', quoter)
        if quoter > banduoc:
            noncee = w4.eth.getTransactionCount('0x8039f3Aa709FEC29fdC5f075449b23Ab609a6998')
            # print('nonceeeeee',noncee)
            deadline = int(time.time()) +1000
            fn = contract_router.functions.swapExactTokensForTokens(aa, int(quoter*0.997*10**6), path, my_address, deadline).buildTransaction(
                {
            "chainId":250,
            "from": my_address,
            "value": int(0 * 10 ** 18),
            'gasPrice': int(gass*10**9),
            "gas": 400000,
            "nonce":noncee })
            signed_tx = w4.eth.account.sign_transaction(fn, private_key=my_pkey)
            tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(w4.toHex(tx_hash))
            while True:
                try:
                    receipt = w4.eth.waitForTransactionReceipt(tx_hash, timeout=1000)
                    eee=receipt['status']
                    print(eee)
                    if eee==0:
                        telegram_bot_sendtext3(f'FAIL lenh ban {coin} SPIRIT')
                        print ("lenh BAN spirit da failed")
                        sys.exit()
                    else:
                        telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren SPIRIT  {quoter}')
                        print("lenh BAN spirit da khop")
                        sys.exit()
                except Exception as e:
                    print(e)
                    receipt = w4.eth.waitForTransactionReceipt(tx_hash, timeout=2000)
                    eee=receipt['status']
                    print(eee)
                    if eee==0:
                       telegram_bot_sendtext3(f'FAIL lenh ban {coin} tren spirit bsc')
                       print ("lenh BAN spirit da failed")
                       sys.exit()
                    else:
                       telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren spirit  {quoter}')
                       print("lenh BAN spirit da khop")
                       sys.exit()
        else:
            print('-----------------')
            print("BAN BANG TAYYYYYYYYYYYYY")
    else:
        print("chua co so du, chua ban dc")
        time.sleep(0.5)
    
if __name__ == '__main__':
    while True:
        try:
            sell_spirit_fusdt()
            time.sleep(3)
            print('-----------')
        except Exception as e:
            print(e)
            if (str(e)) == 'execution reverted':
                sell_spirit()