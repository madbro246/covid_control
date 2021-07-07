from sim800l import SIM800L
sim800l=SIM800L('/dev/serial0')


def sms:
    sms="alert entry"
    sim800l.send_sms('7012611899',sms)