# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:48:26 2019

@author: Oliver
"""
from random import randint
import pandas as pd
import numpy as np
from scipy.stats import chisquare, chi2_contingency, norm

sd = pd.read_csv("responses cleaned final.csv", index_col=0)
sd.columns = ["current age", "country", "gender", "HHGG age", "obtained", "other obtained", "influence", "aspect"]
def to_float(x):
    number = float(x)
    return number

#proportion standard error
def prop_sem(prop, n):
    sem = np.sqrt((prop*(1-prop))/n)
    return sem

#t-test comparing two seperate population averages, after udacity's inferential statistics course 
#and rumsey, statistics for dummies
def test_statistic(a, b):
    diff = a.mean() - b.mean()
    sta = ((a.std()**2) / len(a))
    stb = ((b.std()**2) / len(b))
    stderror = np.sqrt( sta + stb )
    degfree = len(a) + len(b) - 2
    return "The test statistic is: {} , with {} degrees of freedom".format(diff / stderror, degfree)
#comparing two population proportions

def get_wisdom(influence=True, aspect = True):
    #more changes of wisdom if we take two
    i = randint(0, len(sd))
    a = randint(0, len(sd))
    inf = sd["influence"].iloc[i]
    asp = sd["aspect"].iloc[a]
    if influence == True:
        print("Influence the book had on respondent {}: {}".format(i, inf))
    if aspect == True:
        print("\n \nAspect respondent {} found the most interesting: {}".format(a, asp))
    return
        
#z-test for proportions after statistics for dummies, deborah rumsey 2011
def p_ztest(pobs, pexp, n, one_tailed=True):
    difference = pobs- pexp
    serror = np.sqrt((pexp*(1-pexp)) / n)
    z = difference / serror
    if one_tailed:
        return "P-Value: {}, Z = {}".format(norm.sf(abs(z)) / 2, z)
    else:
        return "P-Value: {}, Z = {}".format(norm.sf(abs(z)), z)