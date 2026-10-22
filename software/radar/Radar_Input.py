import serial


def las_matning(port):
    
    try:

        rad = port.readline()

        delar = rad.decode("utf-8").strip().split(";")

        if len(delar) != 2:
            print("Fel antal delar:")
            return None
                
        
        distans = float(delar[0])
        vinkel = int(delar[1])
        
        return distans, vinkel

    except ValueError:
        print("Kunde inte tolka raden:")


def main():
    with serial.Serial("COM3", 9600, timeout = 1) as port:
        matning = las_matning(port)
        if matning != None:
            distans, vinkel = matning
            print(matning)


if __name__ == "__main__":
    main()