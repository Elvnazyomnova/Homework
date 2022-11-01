{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5XkPanjJJHwdkJDp4b/lq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Elvnazyomnova/Homework/blob/main/Untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WmFwJ9wTB9M6",
        "outputId": "37d98d84-0b55-4eb0-8633-289b50715b36"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "введите количество символов8\n",
            "Пароль: psSc/8WY\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "from random import sample\n",
        "simvol = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'\n",
        "try:\n",
        "   dlina = int(input('введите количество символов'))\n",
        "except TypeError:\n",
        "   print('Ошибка ввода длины пароля')\n",
        "parol = sample(simvol, dlina)\n",
        "print('Пароль:', ''.join(parol))\n",
        "\n"
      ]
    }
  ]
}