from jumper import Jumper

jumper = Jumper()

jumper_print = jumper.get_jumper()

for i in jumper_print:
    print(i)

jumper.take_life()
jumper.take_life()
jumper.take_life()

for i in jumper.get_jumper():
    print(i)
