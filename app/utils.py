# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import xmltodict

def omim_from_entrez():
    """Return a dictionary mapping NCBI GeneIDs to OMIM IDs
    Returns 17,126 entries from an original 26,371.
    """
    fp = './data/mim2gene.txt' # https://www.omim.org/static/omim/data/mim2gene.txt
    df = pd.read_csv(fp, skiprows=4, sep='\t',
                    usecols=['# MIM Number', 'Entrez Gene ID (NCBI)'])
    df.columns = ['omim', 'ncbi'] # rename columns
    df = df[np.isfinite(df['ncbi'])] # remove NaN's from ncbi
    df['ncbi'] = df['ncbi'].astype(int) # recast ncbi as int
    ncbi_to_omim = dict(zip(df.ncbi,df.omim)) # create dict