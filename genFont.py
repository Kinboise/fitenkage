# 读码表
def readCodeMap(nameFile):
    with open(nameFile) as f:
        lines = f.readlines()
    codeMap = {}
    for line in lines:
        line = line.split(' ')
        codeMap[line[0]] = line[1].strip('\n')
        # codeMap[line[1]] = int(line[0], 16)
        # maxCode = int(line[0], 16)
    return codeMap

# 生成

def batchGen(codeMap):
    import subprocess as sp
    for i in codeMap:
        path = 'svg/' + i + '.svg'
        lat = codeMap[i]
        if int(i, 16) % 16 == 0:
            print(path)
        sp.run(['node','index.js', path, lat])

# 导入

def makeFont(fontFile):
    import fontforge as ff
    # font = ff.open(fontFile)
    font = ff.font()
    import os
    svgs = os.listdir('svg/')

    for svg in svgs:
        glyph = font.createChar(int(svg[0:-4], 16))
        glyph.importOutlines('svg/' + svg)
        glyph.removeOverlap()
        glyph.correctDirection()
        glyph.addExtrema('all')
    font.save(fontFile)