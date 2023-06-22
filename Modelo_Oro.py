{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+fbg4MFDaZmM9DWt5XxeL",
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
        "<a href=\"https://colab.research.google.com/github/cesarlongart101/Modelo_Oro/blob/main/Modelo_Oro.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OnYQ2IVM4-sb"
      },
      "outputs": [],
      "source": [
        "pip list"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "\n",
        "anos = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]\n",
        "\n",
        "# web = \"https://www.usagold.com/daily-gold-price-history/?ddYears=2000\"\n",
        "# web = \"https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022\"\n",
        "# respuesta = requests.get(web)\n",
        "# print(respuesta.text)\n",
        "\n",
        "# todo = pd.read_html(io = \"https://www.usagold.com/daily-gold-price-history/?ddYears=2000\", attrs = {'id': 'pricehistorytable'}, flavor = 'bs4')\n",
        "# # todo = pd.read_html(\"https://es.wikipedia.org/wiki/National_Basketball_Association\")\n",
        "# len(todo)\n",
        "# print(todo)\n",
        "\n",
        "url = \"https://www.usagold.com/daily-gold-price-history/?ddYears=2000\"\n",
        "\n",
        "data = requests.get(url).text\n",
        "\n",
        "print(data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BTbbaTeV5G7B",
        "outputId": "c0946ee7-d229-4ccd-8cab-ac5282b91e13"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<HTML>\n",
            "<HEAD>\n",
            "<TITLE>403 Forbidden</TITLE>\n",
            "</HEAD>\n",
            "<BODY>\n",
            "<H1>Forbidden</H1>\n",
            "You do not have permission to access this document.\n",
            "<P>\n",
            "<HR>\n",
            "<ADDRESS>\n",
            "Web Server at usagold.com\n",
            "</ADDRESS>\n",
            "</BODY>\n",
            "</HTML>\n",
            "\n",
            "<!--\n",
            "   - Unfortunately, Microsoft has added a clever new\n",
            "   - \"feature\" to Internet Explorer. If the text of\n",
            "   - an error's message is \"too small\", specifically\n",
            "   - less than 512 bytes, Internet Explorer returns\n",
            "   - its own error message. You can turn that off,\n",
            "   - but it's pretty tricky to find switch called\n",
            "   - \"smart error messages\". That means, of course,\n",
            "   - that short error messages are censored by default.\n",
            "   - IIS always returns error messages that are long\n",
            "   - enough to make Internet Explorer happy. The\n",
            "   - workaround is pretty simple: pad the error\n",
            "   - message with a big comment like this to push it\n",
            "   - over the five hundred and twelve bytes minimum.\n",
            "   - Of course, that's exactly what you're reading\n",
            "   - right now.\n",
            "   -->\n",
            "\n"
          ]
        }
      ]
    }
  ]
}