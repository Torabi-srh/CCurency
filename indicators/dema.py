

def sma(candles):
    length = len(candles)
    ret = sum(candles)
    return ret / length


def ema(candles):
    length = len(candles)
    multiplier = (2 / (length + 1))

    ret = list()
    ret.append(candles[0] / length)

    for i in range(1, length):
        # (price * multiplier) + (EMAp * (1 - multiplier))
        ret.append((candles[i] * multiplier) + (candles[i-1] * (1 - multiplier)))

    return ret


def ema2(candles):
    ema_list = ema(candles)
    length = len(candles)
    multiplier = (2 / (length + 1))

    ret = list()
    ret.append(sma(ema_list))

    for i in range(1, length):
        # (EMA * multiplier) + (EMA(EMA)p * (1 - multiplier))
        ret.append(ema_list[i] * multiplier + (ret[i-1] * (1 - multiplier)))

    return ret


def dema(candles):
    ret = list()
    length = len(candles)
    ema_list = ema(candles)
    ema2_list = ema2(candles)

    for i in range(length):
        # DEMA = 2*EMA – EMA(EMA)
        ret.append((2 * ema_list[i]) - ema2_list[i])

    return ret
