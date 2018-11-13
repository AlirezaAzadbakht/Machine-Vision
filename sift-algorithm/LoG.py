import ImageIO as io
DoG = []

def calculateLoG(octaves):
    for octave in octaves:
        DoG.append(octave[1] - octave[0])
        DoG.append(octave[2] - octave[1])
        DoG.append(octave[3] - octave[2])
        DoG.append(octave[4] - octave[3])
    for i in DoG:
        io.showImage(i)
