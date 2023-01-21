from others.converter.usd_converter import *

if __name__ == '__main__':
    converter = usdConverter([], 0, [])

    converter.addExNis("nis")
    converter.addExYen("yen")
    converter.addExEuro("euro")

    converter.getEx("usd", "yen", 1)
    converter.getEx("yen", "usd", 1)
    converter.getEx("yen", "usd", 30000)
    print(converter)
    converter.getEx("usd", "yen", 134)
    converter.update("euro")
    print(converter)