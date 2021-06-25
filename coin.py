from binance.client import Client
import config, urllib3, time, os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

green = "\033[1;32m"
red = "\033[1;31m"
blue = "\033[1;34m"
white = "\033[1;97m"

def relogio(segundos):
    for i in range(segundos, 0, -1):
        time.sleep(1)
        timer = red + str(i) + white
        print('%sxxxx' % timer, end='\r')
def main():
    stop = 0
    cc = input(f"{white}Moeda:{blue}")
    porcent = input(f"{white}Porcentagem:{red}")
    porcent = float(porcent)/100
    loops = input(f"{white}LOOPS:{red}")
    while stop < int(loops):
        try:
            stop +=1
            #os.system('cls')
            os.system('clear')
            print(f"{white}MOEDA:{blue}{cc}{white}")
            print(f"{white}PORCENTAGEM:{red}{porcent}{white}")
            print(f"{white}LOOP:{red}{stop}{white}")
            client = Client(config.api_key, config.api_secret)
            info = client.get_account()
            info = info['balances']
            for data in info:
                valores = data.pop('free')
                moedas = data.pop('asset')
                if valores == '0.00000000':
                    pass
                else:
                    print(f'{white}{moedas}: {green}{valores}{white}')
            print('')
            print(white + f'  MOEDA      VALOR      BAIXA      ALTA      %       {blue}C{white}/{red}V{white}')
            for data in client.get_ticker():
                price = data.pop('lastPrice')
                moeda = data.pop('symbol')
                h24 = data.pop('highPrice')
                l24 = data.pop('lowPrice')
                change = data.pop('priceChangePercent')
                obs = ''
                if cc in moeda:
                    if float(price) - (float(price) * float(porcent)) < float(l24):
                        obs = f"  OBS:{blue}COMPRAR{white}"
                        if float(change) == 0:
                            obs = f"  OBS:{green}N/D/A{white}"
                    elif float(price) + (float(price) * float(porcent)) > float(h24)  and float(change) > 0:
                        obs = f"  OBS:{red}VENDER{white}"
                    else:
                        obs = f"  OBS:{green}N/D/A{white}"
                    if f'{cc}BTC' == str(moeda):
                        print(f'{blue}{moeda:^10}{white} {price[0:8]}   {red}{l24[0:8]}   {green}{h24[0:8]}  {red}{change[0:4]}{white} {obs}')
                        print('')
                    elif f'BTC{cc}' == str(moeda):
                        print(f'{blue}{moeda:^10}{white} {price[0:8]}   {red}{l24[0:8]}   {green}{h24[0:8]}  {red}{change[0:4]}{white} {obs}')
                        print('')
                    painel = f'{blue}{moeda:^10}{white} {price[0:8]}   {red}{l24[0:8]}   {green}{h24[0:8]}  {red}{change[0:4]}{white} {obs}'
                    if 'COMPRAR' in obs:
                        print(painel)
                    if 'VENDER' in obs:
                        print(painel)
            print('\n')
            relogio(12)
        except KeyboardInterrupt:
            print(f"{red} STOP {white}")
            break
if __name__ == '__main__':
    main()
