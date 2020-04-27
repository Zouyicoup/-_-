#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Correctdateformat(A_date):
    if len(A_date) == 10:
        return A_date
    elif len(A_date) == 9:  
        if A_date[6] == '-':
            return A_date.replace('-','-0',1)
        else:
            return A_date[0:8] + '0' + A_date[-1]     
    elif len(A_date) == 8: 
        return A_date.replace('-','-0',2)

