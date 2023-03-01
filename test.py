{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (45163445.py, line 52)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 52\u001b[1;36m\u001b[0m\n\u001b[1;33m    arr[]\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#import numpy as np\n",
    "# num=int(input(\"Enter the number: \"))\n",
    "# class Define:\n",
    "#     def positive:\n",
    "#         if num > 0\n",
    "#         return (\"number is positive\")\n",
    "#     def negative:\n",
    "#         if num < 0:\n",
    "#             return(\"Number is negative\")\n",
    "#     def zero:\n",
    "#         if num ==0:\n",
    "#             return(\"number is zero\")\n",
    "        \n",
    "        \n",
    "        \n",
    "        \n",
    "        \n",
    "# class Number:\n",
    "#     def __init__(self, num):\n",
    "#         self.num = num\n",
    "\n",
    "#     def check(self):\n",
    "#         if self.num > 0:\n",
    "#             print(\"Positive\")\n",
    "#         elif self.num == 0:\n",
    "#             print(\"Zero\")\n",
    "#         else:\n",
    "#             print(\"Negative\")\n",
    "\n",
    "# # Create an object of the Number class\n",
    "# num = Number(int(input(\"Enter number: \")))\n",
    "\n",
    "# # Call the check method to determine if the number is positive, negative, or zero\n",
    "# num.check()\n",
    "\n",
    "class DuplicateCounter:\n",
    "    def __init__(self, lst):\n",
    "        self.lst = lst\n",
    "\n",
    "    def count_duplicates(self):\n",
    "        duplicates = {}\n",
    "        for i in self.lst:\n",
    "            if i in duplicates:\n",
    "                duplicates[i] += 1\n",
    "            else:\n",
    "                duplicates[i] = 1\n",
    "        count = 0\n",
    "        for key, value in duplicates.items():\n",
    "            if value > 1:\n",
    "                count += 1\n",
    "        return count\n",
    "arr[]\n",
    "for i in range(10):\n",
    "   arr.append(input(\"Enter element: \")) \n",
    "\n",
    "my_list =arr[] \n",
    "counter = DuplicateCounter(my_list)\n",
    "print(counter.count_duplicates())  # Output: 6"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.11.2"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "0c1f23ac049957226e7b345e10847a716b305f01fb5ea588599021a8042b7bd0"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
