#Libraries 

from io import open
import sys
import numpy as np
import pandas as pd
import json
import twint 

# Set users info
users = ("mustafa_mfa",	"acarumut",	"ahmetakifoktay",	"alibaris_ulusoy",	"alikemalaydin12",	"mbasceri",	
"ar_akinci",	"kaptaderya",	"atilayersan",	"avniaksoy",	"aylinsekizkk",	"ayshehilal",	"bestesun",	"akcapar",	
"cemkahyaoglu1",	"cmlttnaydin",	"ceylan117",	"cerginay",	"cerciyes",	"dehaerpek",	"deniz__cakar",	"orsdarya",	
"ihakkimusa",	"h_yavuz07",	"turkoz64",	"eceozturkcil",	"ulgenelif",	"arikanengin",	"enginyrr2",	"iscanerdogan",
"ersin_ercin",	"esen_altug",	"frkkymkc",	"fatihyildiz_mfa",	"fazlicorman",	"ferhatalkana",	"firatsunel",	
"hakkiakil",	"hamiaksoy2",	"hsnsasn",	"hulusikilictr",	"hmuftuoglu",	"ilhansaygili",	"ineziroglu",	"kerimuras",
"korkarakoc",	"leventsalim",	"lgumrukcu",	"lutfullahgoktas",	"meminkiraz",	"mfcarikci",	"mksakalli",	
"mskartal58",	"mkaralar_mfa",	"bemithatrende",	"muratkaragoz10",	"mkbasa1",	"nacikoru",	"nursagman",	
"olganbekar",	"oilhansener",	"omerfarukdogan_",	"orhunmr",	"belentepeserdar",	"serdarkilic9",	"snnysldg",	
"_sgokce",	"tanjubilgic",	"togan_oral",	"turhandilmac",	"tulinerkalkara",	"umityardim1961",	"vehbietensel",	
"yagmurguldere",	"zaferates1975",	"kandemirzerrin")

#Get user info through twit in json formats 
config = twint.Config()
config.Username = users
config.Store_json = True
config.Output = "diplomats.json"
twint.run.Search(config)


#read tweets json file
data = pd.read_json('diplomats.json', orient = "records", lines = "True")

# save data as csv file 
with open('diplomats.txt', 'w') as f:
    i = 1
    for item in data["tweet"]:
        text = str(i) + "--" + item + " \n "
        i +=1
        f.write(text)
        
