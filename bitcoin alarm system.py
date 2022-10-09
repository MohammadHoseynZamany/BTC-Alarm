'''
In the name of GOD

creator: Mohammad Hoseyn Zamany
program name: bitcoin alarm system
'''












def btc():
    import cryptocompare
    from time import sleep
    from pygame import mixer
    from datetime import datetime
    from os import popen


    mixer.init()

    print('Wellcome to bitcoin alarm system')


    while True:
        mixer.music.load('wait.mp3')
        mixer.music.play()
        print('1 : Treshold alarm')
        print('2 : See the final price')
        print('3 : See the final data')
        print('4 : See historical price day')
        print('4 : See historical price hour')
        print('5 : Histoey of treshold alarm')
        print('0 : Exit')
        inp = input('----->>> ')


        if inp == '1':
            thresh_down = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
            threshold = int(input('Please Enter The Treshold : '))
            thresh_up = thresh_down + threshold       
            sleep_time = int(input('Please Enter The Sleep Time : '))
            time_long = int(input('Please Enter how many seccond do you want to run this alarm : '))
            run_alarm = time_long // sleep_time
            try:
                file_prices_time = open('prices_time.txt', 'r+')
            except:
                file_prices_time = open('prices_time.txt', 'w+')

            t = datetime.today()
            file_name = f'{t.year}_{t.month}_{t.day}.txt'                

            try:
                file_prices = open(file_name, 'r+')
            except:
                file_prices = open(file_name, 'w')
                lines = file_prices_time.readlines()
                value = True
                for i in lines:
                    if i == file_name:
                        value = False
                if value:
                    print(file_name, file = file_prices_time)
                    file_prices_time.close()                
            
            run = 0
            while run <= run_alarm:
                btc_price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
                if btc_price < thresh_down:
                    print('btc went low', btc_price)
                    print('btc went low', btc_price, file = file_prices)
                    file_prices.flush()
                    thresh_up -= threshold
                    thresh_down -= threshold
                    mixer.music.load('Low.mp3')
                    mixer.music.play()

                elif btc_price > thresh_up:
                    print('btc went high', btc_price)
                    print('btc went high', btc_price, file = file_prices)
                    file_prices.flush()
                    thresh_up += threshold
                    thresh_down += threshold
                    mixer.music.load('High.mp3')
                    mixer.music.play()

                else:
                    print(btc_price)
                    print(btc_price, file = file_prices)
                    file_prices.flush()

                run += 1
                sleep(sleep_time)
            file_prices.close()

        elif inp == '2':
            print('1 : in Dollar')
            print('2 : in Euro')
            inp1 = input('----->>> ')

            if inp1 == '1':
                price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
                print(f'\nprice of bitcoin now is {price} Dollar\n')
            
            elif inp1 == '2':
                price = cryptocompare.get_price('BTC')['BTC']
                print(f'\nprice of bitcoin now is {price} Euro\n')

            else:
                print('!!!  input is wrong !!!')

        elif inp == '3':
            for i in cryptocompare.get_historical_price_day('BTC'):
                 print(i)

        elif inp == '4':
            for i in cryptocompare.get_historical_price_hour('BTC'):
                 print(i)

        elif inp == '5':
            file_exists = True
            try:
                file_names = open('prices_time.txt', 'r')
            except:
                print('\n!!! There is no history !!!')
                file_exists = False

            if file_exists:
                read_lines = file_names.readlines()
                index = 0
                print('please select the date of history\n')
                for line in read_lines:
                    print(f'{index} : {line[:-5]}')
                    index += 1
                inp2 = int(input('----->>> '))
                popen(str(read_lines[inp2]))

        elif inp == '0':
            print('\nthank you for use our system')
            break

        else:
            print('!!!  input is wrong  !!!')


if __name__ == '__main__':
    btc()