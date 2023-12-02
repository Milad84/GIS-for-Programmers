import pandas as pd

fileExcel = pd.read_excel("Ozone.xlsx")

dframe = pd.DataFrame( fileExcel, columns= ['FID',    "OBJECTID",
    "SITE_CD", "SITE_NAME",
    "SAMPLER_ID,    OCCUR_CD",
    "TYP_NAME",    "CONT_FLG",
    "IND_FLG",    "COLLOC_FLG",
    "AGE_YR_NUM",    "CAT_TXT",
    "SITE_ID",    "SAMP_PLTFM",
    "NETWORK_CD,    NAME", "PGM_NAME",   
"TYP_NAME0",    "Lat",    "Long" ])    #A

print(dframe)
#A Data frame creation by including the name of columns (heading)
