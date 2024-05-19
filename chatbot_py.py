{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKwCWqH7PwiY2E4a7F/21C",
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
        "<a href=\"https://colab.research.google.com/github/lonkanithin/Sentiment_Analysis_Bot/blob/main/chatbot_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_WKE_vSxFwuN",
        "outputId": "0e514c24-e105-42a1-f395-a8291a6d0768"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers/punkt.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "import nltk\n",
        "from textblob import TextBlob\n",
        "\n",
        "nltk.download('punkt')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def preprocess_text(text):\n",
        "    words = nltk.word_tokenize(text)\n",
        "    words = [word.lower() for word in words if word.isalnum()]\n",
        "    return \" \".join(words)"
      ],
      "metadata": {
        "id": "4xynLv3DF9X_"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_sentiment(text):\n",
        "    text = preprocess_text(text)\n",
        "    analysis = TextBlob(text)\n",
        "    if analysis.sentiment.polarity > 0:\n",
        "        return \"+ve\"\n",
        "    elif analysis.sentiment.polarity < 0:\n",
        "        return \"-ve\"\n",
        "    else:\n",
        "        return \"neutral\""
      ],
      "metadata": {
        "id": "vQztoP2GGBO6"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def chatbot():\n",
        "    print(\"Chatbot: Hi! How can I assist you today?\")\n",
        "\n",
        "    while True:\n",
        "        text_input = input(\"You: \")\n",
        "\n",
        "        if text_input.lower() == \"exit\":\n",
        "            print(\"Chatbot: Goodbye!\")\n",
        "            break\n",
        "\n",
        "        sentiment = get_sentiment(text_input)\n",
        "\n",
        "        if sentiment == \"+ve\":\n",
        "            print(\"Positive\")\n",
        "        elif sentiment == \"-ve\":\n",
        "            print(\"Negative\")\n",
        "        else:\n",
        "            print(\"Neutral\")"
      ],
      "metadata": {
        "id": "ny3SnVo0GFzv"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chatbot()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_NoShZhDGM22",
        "outputId": "ce0a4d1d-7a1c-4c8e-a829-34bc2f5812d2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Chatbot: Hi! How can I assist you today?\n",
            "You: how are you\n",
            "Neutral\n",
            "You: i am not bad\n",
            "Positive\n",
            "You: i am bad\n",
            "Negative\n",
            "You: i am awesome \n",
            "Positive\n",
            "You: who are you\n",
            "Neutral\n",
            "You: exit\n",
            "Chatbot: Goodbye!\n"
          ]
        }
      ]
    }
  ]
}