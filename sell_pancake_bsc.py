from web3 import Web3
w4 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org/'))
import time
import math
import requests
import sys
import json



token = '' # address token
banduoc = 1 #gia mong muon ban duoc
slippage = 2
gass = 501
vi = '' #Myadress

banben = "pancake"    #pancake hay 1inch
supporting_fee = 0 

def router_address ():
    if banben =="pancake":
        return '0x10ED43C718714eb63d5aA57B78B54704E256024E' #pancake router
    elif banben =="1inch":
        return '0x11111112542D85B3EF69AE05771c2dCCff4fAa26' #1inch router
    elif banben =="ape":
        return '0xcF0feBd3f17CEf5b47b0cD257aCf6025c5BFf3b7'  #ape router
router_address = router_address()

c = json.dumps(token)
y = json.loads(c)
token =w4.toChecksumAddress(y['token_b'])
side = y['path_bsc']

contract_token = w4.eth.contract(address = w4.toChecksumAddress(token),abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
contract_router = w4.eth.contract(address=router_address,abi ='[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
def path():
    if side =="BUSD":
        return [token,'0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'] #BUSD_ADDRESS
    elif side =="USDT":
        return [token,'0x55d398326f99059fF775485246999027B3197955','0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56']
    elif side =="WBNB":
        return [token,'0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c','0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56']
def vitri():
    if side =="BUSD":
        return 1
    elif side =="BUSDT":
        return 2
    elif side =="WBNB":
        return 2
vitri = vitri()
path = path()
sl = 1-slippage/100
def privateKey():
    if vi==1:
        return '' #pkey theo tung vi tuong ung
    elif vi==2:
        return 
def my_address():
    if vi==1:
        return ''
    elif vi==2:
        return ''


my_address = my_address()
pkeyyyy = privateKey()


def lamtron(number:float, decimals:int=2):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)
    factor = 10 ** decimals
    return math.floor(number * factor) / factor

def telegram_bot_sendtext3(bot_message):    
     bot_token = '1786278695:AAFkaIJv9bvsYrUS1r0OiMOcDL2wAJzc5z4'
     bot_chatID = '-526856728'
     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
     response = requests.get(send_text)
     return response.json()  
def token_name(address):
    symbol = contract_token.functions.symbol().call()
    decimal = contract_token.functions.decimals().call()
    return {'name':symbol,
            'decimal':decimal}
coin = token_name(token)['name']
decimal = token_name(token)['decimal']
print('decimal: ',decimal)
def approve():
    noncee = w4.eth.getTransactionCount(my_address)
    a = contract_token.functions.approve(router_address,int(9900000000000000000000000000)).buildTransaction(
                {"chainId":56,
            "from": my_address,
            "value": int(0 * 10 ** 18),
            'gasPrice': int(gass*10**9),
            "gas": 400000,
            "nonce":noncee})
    signed_tx = w4.eth.account.sign_transaction(a, private_key=pkeyyyy)
    tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(w4.toHex(tx_hash))
    receipt = w4.eth.wait_for_transaction_receipt(tx_hash, timeout=1000)
    eee=receipt['status']
    print(eee)
    if eee==0:
        telegram_bot_sendtext3(f'FAIL lenh APPROVE {coin} tren {banben} VI {vi}')
        print (f'FAIL lenh APPROVE {coin} tren PANCAKE')
        sys.exit()
    else:
        telegram_bot_sendtext3(f'KHOP lenh APPROVE {coin} tren {banben} VI {vi}')
        print(f'KHOP lenh APPROVE {coin} tren PANCAKE')
def approve_check():
    a = contract_token.functions.allowance(my_address,router_address).call()
    if a ==0:
        print("CHUA APPROVE - CHUA BAN DC")
        approve()
    else:
        print('DA APPROVE - DANG BAN')
    print(a)
approve_check()
def sell_pancake():
    print(coin)
    balance =lamtron( contract_token.functions.balanceOf(my_address).call()/10**decimal,0)
    print('balance ',balance)
    aa =int(str(int(balance*1000)) + '0'*(decimal-3))
    print(aa)
    if balance > 0.1:
        time.sleep(0.5)
        quoter =round( contract_router.functions.getAmountsOut(aa,path).call()[vitri]/10**18,2)
        print(type(quoter))
        print('ban duocccccccccccccccccccccccccccc ', quoter)
        if quoter > banduoc:
            noncee = w4.eth.getTransactionCount(my_address)
            # print('nonceeeeee',noncee)
            deadline = int(time.time()) +1000
            fn = contract_router.functions.swapExactTokensForTokens(aa, int(quoter*sl*10**18), path, my_address, deadline).buildTransaction(
                {"chainId":56,
            "from": my_address,
            "value": int(0 * 10 ** 18),
            'gasPrice': int(gass*10**9),
            "gas": 400000,
            "nonce":noncee })
            signed_tx = w4.eth.account.sign_transaction(fn, private_key=pkeyyyy)
            tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(w4.toHex(tx_hash))
            receipt = w4.eth.wait_for_transaction_receipt(tx_hash, timeout=1000)
            eee=receipt['status']
            print(eee)
            if eee==0:
                telegram_bot_sendtext3(f'FAIL lenh ban {coin} tren PANCAKE VI {vi}')
                print ("FAILED lenh BAN PANCAKE da failed")
                sys.exit()
            else:
                telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren PANCAKE {quoter} VI {vi}')
                print("KHOP lenh BAN PANCAKE da khop")
                sys.exit()
        else:
            print('-----------------')
            print("BAN BANG TAYYYY")
            time.sleep(1)
    else:
        print("chua co so du, chua ban dc")
        time.sleep(0.5)
def sell_pancake_withfee():
    print(coin)
    balance =lamtron( contract_token.functions.balanceOf(my_address).call()/10**decimal,0)
    print('balance ',balance)
    aa =int(str(int(balance*1000)) + '0'*(decimal-3))
    print(aa)
    if balance > 0.1:
        time.sleep(0.5)
        quoter =round( contract_router.functions.getAmountsOut(aa,path).call()[vitri]/10**18,2)
        print(type(quoter))
        print('ban duocccccccccccccccccccccccccccc ', quoter)
        if quoter > banduoc:
            noncee = w4.eth.getTransactionCount(my_address)
            # print('nonceeeeee',noncee)
            deadline = int(time.time()) +1000
            fn = contract_router.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(aa, int(quoter*sl*10**18), path, my_address, deadline).buildTransaction(
                {"chainId":56,
            "from": my_address,
            "value": int(0 * 10 ** 18),
            'gasPrice': int(gass*10**9),
            "gas": 400000,
            "nonce":noncee })
            signed_tx = w4.eth.account.sign_transaction(fn, private_key=pkeyyyy)
            tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(w4.toHex(tx_hash))
            receipt = w4.eth.wait_for_transaction_receipt(tx_hash, timeout=1000)
            eee=receipt['status']
            print(eee)
            if eee==0:
                telegram_bot_sendtext3(f'FAIL lenh ban {coin} tren PANCAKE VI {vi}')
                print ("FAILED lenh BAN PANCAKE da failed")
                sys.exit()
            else:
                telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren PANCAKE {quoter} VI {vi}')
                print("KHOP lenh BAN PANCAKE da khop")
                sys.exit()
        else:
            print('-----------------')
            print("BAN BANG TAYYYY")
            time.sleep(1)
    else:
        print("chua co so du, chua ban dc")
        time.sleep(0.5)
def sell_oneinch():
    print(coin)
    bb =lamtron(contract_token.functions.balanceOf(my_address).call()/10**decimal,0)
    print("SO DU",bb)
    cc=lamtron(bb,3)
    # print("cc",cc)
    aa =int(str(int(bb*1000)) + '0'*(decimal-3))
    print("aa", aa)
    time.sleep(1)
    if float (cc)>0.1:
        time.sleep(0.1)
        url = f'https://api.1inch.exchange/v3.0/56/swap?fromTokenAddress={token}&toTokenAddress=0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56&amount={aa}&fromAddress={my_address}&slippage={slippage}'
        r = requests.get(url)
        print(r)
        p = r.json()
        b=p['toTokenAmount']
        c = p['tx']['data']
        print("BAN DUOCccccccccccccccc ", float(b)/10**18)
        if float(b)> banduoc*10**18:
           tx ={"from": my_address,
                "to": "0x11111112542D85B3EF69AE05771c2dCCff4fAa26",
                "data": c,
                "value": int(0 * 10 ** 18),
                "gasPrice": int(gass*10**9),
                "gas": 700000,
                "nonce": w4.eth.getTransactionCount(my_address)}
           signed_tx = w4.eth.account.sign_transaction(tx, private_key=pkeyyyy)
           tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
           print(w4.toHex(tx_hash))
           receipt = w4.eth.wait_for_transaction_receipt(tx_hash, timeout=2000)
           eee=receipt['status']
           print(eee)
           if eee==0:
                telegram_bot_sendtext3(f'FAIL lenh ban {coin} tren 1inchBSC VI {vi}')
                print ("lenh BAN PANCAKE da failed")
                time.sleep(1)
           else:
                telegram_bot_sendtext3(f'KHOP lenh ban {coin} tren 1inchBSC { float(b)/10**18} VI {vi}')
                print("lenh BAN 1INCH da khop")
                sys.exit()
        
        else:
            print("BAN BANG TAY")
            time.sleep(0.5)
    else:
        print("chua co so du, chua ban dc")
        time.sleep(0.5)
if __name__ == '__main__':
    while True:
        try:
            if banben == 'pancake' and supporting_fee == 0:
                sell_pancake()
                print('-----------')
            if banben == 'ape' and supporting_fee == 0:
                sell_pancake()
                print('-----------')
            elif banben == 'pancake' and supporting_fee == 1:
                sell_pancake_withfee()
                print('-----------')
            elif banben == '1inch':
                sell_oneinch()
        except Exception as e:
            print(e)
            time.sleep(1)