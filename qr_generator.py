import qrcode as qr
img= qr.make("https://open.spotify.com/playlist/3pvb8Idh6z5Qq8Acqvchq0")
img.save("playlist.png")