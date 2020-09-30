import sys
import time

def callMe(name, number, keuze):
    print("&: Hallo, je spreekt met Bart.")
    time.sleep(1)
    print("&: Met wie spreek ik?")
    time.sleep(1)
    print("#: Je spreekt met " + name)
    time.sleep(1)
    print("&: Hallo "+ name + ", het spijt mij, ik ben druk op het moment. Zou je kunnen zeggen wat je nummer is?")
    time.sleep(1)
    print("#: Het is "+ number)
    time.sleep(1)
    print("&: Top! Kan ik jou vandaag terugbellen of niet?")
    time.sleep(1)
    print("#: " + keuze)
    time.sleep(1)
    print("&: Is goed, tot dan!")
    time.sleep(1)
    print("Klik!")

callMe(sys.argv[1], sys.argv[2], sys.argv[3])