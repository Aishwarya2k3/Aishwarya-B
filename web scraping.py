{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dd1ebfb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import bs4\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "61a88e22",
   "metadata": {},
   "outputs": [],
   "source": [
    "url='https://economictimes.indiatimes.com/markets/stocks/news'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2e9c7464",
   "metadata": {},
   "outputs": [],
   "source": [
    "headers ={ \n",
    "    'User-Agent':\"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "78b85cc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "r = requests.get(url,{'headers':headers})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3ce671c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = bs4.BeautifulSoup(r.text,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d8e10847",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Ahead of Market: 12 things that will decide D-Street action on Friday'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all('div',{'class':'eachStory'})[0].find_all('a')[-1].text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d128ab4e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
