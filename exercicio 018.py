from math import sin,cos,tan, radians
ang = int(input('Me diga ai bb qual que é o teu angulo:'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O valor do seu grau:{:.2f} tem como correspondente; sen:{:.2f}; cos:{:.2f}; tan:{:.2f}'.format(ang, sen, cos, tan))