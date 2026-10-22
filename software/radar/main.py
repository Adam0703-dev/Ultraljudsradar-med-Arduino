import pygame
import serial
import Radar_Grafik
import Radar_Input

PORT = "COM3"
BAUD = 9600
FPS = 60
KVARTID_MS = 1200
MAX_DISTANS = 200


def main():
    pygame.init()
    try:
        skarm = pygame.display.set_mode((800, 600))
        klocka = pygame.time.Clock()
        slutpunkt = Radar_Grafik.START
        matpunkter = []
        kor = True

        with serial.Serial(PORT, BAUD, timeout=1) as port:
            while kor:
                for handelse in pygame.event.get():
                    if handelse.type == pygame.QUIT:
                        kor = False
                if not kor:
                    break

                nu = pygame.time.get_ticks()
                matpunkter = [punkt for punkt in matpunkter if nu - punkt[2] < KVARTID_MS]

                if port.in_waiting > 0:
                    matning = Radar_Input.las_matning(port)
                    if matning is not None:
                        distans, vinkel = matning
                        slutpunkt = Radar_Grafik.koordinater(MAX_DISTANS, vinkel)
                        if 3 < distans <= MAX_DISTANS and not matpunkter:
                            x, y = Radar_Grafik.koordinater(distans, vinkel)
                            matpunkter.append((x, y, pygame.time.get_ticks()))

                Radar_Grafik.rita_bild(skarm, slutpunkt, matpunkter, pygame.time.get_ticks())
                pygame.display.flip()
                klocka.tick(FPS)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
