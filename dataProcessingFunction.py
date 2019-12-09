{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/ausaafnabi/MyExampleCodes/blob/master/dataProcessingFunction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "93zTDnBYyld6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "import hashlib\n",
        "\n",
        "def split_train_test(data , test_ratio):\n",
        "    shuffled_indices = np.random.permutaions(len(data))\n",
        "    test_set_size = int(len(data) * test_ratio)\n",
        "    test_indices = shuffled_indices[:test_set_size]\n",
        "    train_indices = shuffled_indices[test_set_size:]\n",
        "    return data.iloc[train_indices], data.iloc[test_indices]\n",
        "\n",
        "def test_set_check(identifier, test_ratio , hash):\n",
        "  return hash(np.int64(identifier)).digest()[-1]<256*test_ratio\n",
        "\n",
        "def split_train_test_by_id(data,test_ratio,id_column,hash =hashlib.md5):\n",
        "  ids =data[id_column]\n",
        "  in_test_set = ids.apply(lambda id:test_set_chech(id_, test_ratio,hash))\n",
        "  return data.loc[~in_test_set], data.loc[in_test_set]"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}