{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "46fb0fa3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "276d5bd6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'country': ['france',\n",
       "  'spain',\n",
       "  'germany',\n",
       "  'spain',\n",
       "  'germany',\n",
       "  'france',\n",
       "  'spain',\n",
       "  'france',\n",
       "  'germany',\n",
       "  'france'],\n",
       " 'age': [44, 27, 30, 38, 40, 35, nan, 48, 50, 37],\n",
       " 'salary': [72000,\n",
       "  48000,\n",
       "  54000,\n",
       "  61000,\n",
       "  nan,\n",
       "  58000,\n",
       "  52000,\n",
       "  79000,\n",
       "  83000,\n",
       "  67000],\n",
       " 'purchased': ['no',\n",
       "  'yes',\n",
       "  'no',\n",
       "  'no',\n",
       "  'yes',\n",
       "  'yes',\n",
       "  'no',\n",
       "  'yes',\n",
       "  'no',\n",
       "  'yes']}"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d={'country':['france','spain','germany','spain','germany','france','spain','france','germany','france'],\n",
    "\n",
    "  'age':[44,27,30,38,40,35,np.nan,48,50,37],\n",
    "  'salary':[72000,48000,54000,61000,np.nan,58000,52000,79000,83000,67000],\n",
    "  'purchased':['no','yes','no','no','yes','yes','no','yes','no','yes']}\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "393d17c0",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mdf1\u001b[49m\u001b[38;5;241m.\u001b[39minfo()\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df1' is not defined"
     ]
    }
   ],
   "source": [
    "df1.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8aa62231",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mdf1\u001b[49m\u001b[38;5;241m.\u001b[39mhead()\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df1' is not defined"
     ]
    }
   ],
   "source": [
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a60d42ff",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'head'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[8], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43md\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhead\u001b[49m()\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'dict' object has no attribute 'head'"
     ]
    }
   ],
   "source": [
    "d.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2f8d7f24",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1=pd.DataFrame(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7b926bc7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>france</td>\n",
       "      <td>44.0</td>\n",
       "      <td>72000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>spain</td>\n",
       "      <td>27.0</td>\n",
       "      <td>48000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>germany</td>\n",
       "      <td>30.0</td>\n",
       "      <td>54000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>spain</td>\n",
       "      <td>38.0</td>\n",
       "      <td>61000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>germany</td>\n",
       "      <td>40.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>france</td>\n",
       "      <td>35.0</td>\n",
       "      <td>58000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>spain</td>\n",
       "      <td>NaN</td>\n",
       "      <td>52000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>france</td>\n",
       "      <td>48.0</td>\n",
       "      <td>79000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>germany</td>\n",
       "      <td>50.0</td>\n",
       "      <td>83000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>france</td>\n",
       "      <td>37.0</td>\n",
       "      <td>67000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   country   age   salary purchased\n",
       "0   france  44.0  72000.0        no\n",
       "1    spain  27.0  48000.0       yes\n",
       "2  germany  30.0  54000.0        no\n",
       "3    spain  38.0  61000.0        no\n",
       "4  germany  40.0      NaN       yes\n",
       "5   france  35.0  58000.0       yes\n",
       "6    spain   NaN  52000.0        no\n",
       "7   france  48.0  79000.0       yes\n",
       "8  germany  50.0  83000.0        no\n",
       "9   france  37.0  67000.0       yes"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e26d26f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country      False\n",
       "age           True\n",
       "salary        True\n",
       "purchased    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.isnull().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2ff5dfba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38.77777777777778"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['age'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a601ab7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38.0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['age'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "596a6f27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27.0"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['age'].mode()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "10e91f95",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1['age']=df1['age'].fillna(df1['age'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dee7da0e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d17a160",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4618c691",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>france</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>72000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>spain</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>48000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>germany</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>54000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>spain</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>61000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>germany</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>france</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>58000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>spain</td>\n",
       "      <td>38.777778</td>\n",
       "      <td>52000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>france</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>79000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>germany</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>83000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>france</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>67000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   country        age   salary purchased\n",
       "0   france  44.000000  72000.0        no\n",
       "1    spain  27.000000  48000.0       yes\n",
       "2  germany  30.000000  54000.0        no\n",
       "3    spain  38.000000  61000.0        no\n",
       "4  germany  40.000000      NaN       yes\n",
       "5   france  35.000000  58000.0       yes\n",
       "6    spain  38.777778  52000.0        no\n",
       "7   france  48.000000  79000.0       yes\n",
       "8  germany  50.000000  83000.0        no\n",
       "9   france  37.000000  67000.0       yes"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "400103ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "48000.0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['salary'].mode()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "fe49df5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1['salary']=df1['salary'].fillna(df1['salary'].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "79649abf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>france</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>72000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>spain</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>48000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>germany</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>54000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>spain</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>61000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>germany</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>48000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>france</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>58000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>spain</td>\n",
       "      <td>38.777778</td>\n",
       "      <td>52000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>france</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>79000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>germany</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>83000.0</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>france</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>67000.0</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   country        age   salary purchased\n",
       "0   france  44.000000  72000.0        no\n",
       "1    spain  27.000000  48000.0       yes\n",
       "2  germany  30.000000  54000.0        no\n",
       "3    spain  38.000000  61000.0        no\n",
       "4  germany  40.000000  48000.0       yes\n",
       "5   france  35.000000  58000.0       yes\n",
       "6    spain  38.777778  52000.0        no\n",
       "7   france  48.000000  79000.0       yes\n",
       "8  germany  50.000000  83000.0        no\n",
       "9   france  37.000000  67000.0       yes"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cb39fa1",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
