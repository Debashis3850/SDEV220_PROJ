import multiprocessing
import multiprocessing.process

def nor(seconds):
        from datetime import datetime
        from time import sleep
        sleep(seconds)
        print('Wait', seconds, 'seconds, time is', datetime.utcnow())


if _name_ == '_main_':
        import random
        for n in range(3):
                seconds = random.random()
                proc = multiprocessing.process(trarget=now, args=(seconds,))
                proc.start()               