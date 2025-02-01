#!/usr/bin/env python
# coding: utf-8

# In[5]:


import langid


# Function to detect the language
def detect_language(text):
    lang, confidence = langid.classify(text)
    return lang

# Detect language for different texts
text = input("Enter any language sentence: ")
print("This is:",detect_language(text))

