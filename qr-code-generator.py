import qrcode

link = 'https://mx.farmasi.com/gabrielaitzurysaavedra'
#https://mx.farmasi.com/gabrielaitzurysaavedra/register/beautyinfluencer
#https://mx.farmasi.com/gabrielaitzurysaavedra

img = qrcode.make(link)

img.save('MyStore.png')