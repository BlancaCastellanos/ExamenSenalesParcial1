import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

#Grafica
import matplotlib.pyplot as plt

#Señal senoidal
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")

#Suma
Numero5= frecuencia770 + frecuencia1336
Numero8= frecuencia852 + frecuencia1336
Numero9= frecuencia852 + frecuencia1477
Numero6= frecuencia770 + frecuencia1477

wave_1 = Numero5.make_wave(duration=0.5, start=0, framerate=44100)
wave_2 = Numero8.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_3 = Numero9.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_4 = Numero6.make_wave(duration=0.5, start=1.5, framerate=44100)

#Suma
resultante = wave_1 + wave_2 + wave_3 + wave_4

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")

resultante.plot()

#Sonido
resultante.write("output.wav")

plt.show()