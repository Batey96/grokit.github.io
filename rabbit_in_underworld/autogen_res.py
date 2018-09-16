#!/usr/bin/python3
jsSrc = """
// This class is autogenerated by __file__.
class AssetsList
{
    static list(){
        let assets = new Array();
__insert__
        return assets;
    }
}
""".replace('__file__', __file__)

import json
import os 

line = '        assets.push("__item__");'

dirs = ['./gfx', './levels']
exts = ['.png', '.json']

resList = []
for dr in dirs:
    resList += [os.path.join(dr, f) for f in os.listdir(dr) if len(f) >= 4 and '.' in f and '.' + f.split('.')[-1] in exts]
    
# Remove './' prefix.
resList = [f.split('./')[1] for f in resList]

lines = []
for res in resList:
    lines.append(line.replace('__item__', res))

data = jsSrc.replace('__insert__', "\n".join(lines))
open('./src/AssetsList.js','w').write(data)

