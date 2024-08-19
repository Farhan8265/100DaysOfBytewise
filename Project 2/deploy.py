{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 48,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0UThXQUB2V2Y",
        "outputId": "f4ff2128-0400-4320-8303-2139ca4f3e76"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.37.1)\n",
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.10/dist-packages (7.2.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.1.4)\n",
            "Collecting pandas\n",
            "  Downloading pandas-2.2.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (2.32.3)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.4.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: watchdog<5,>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.0.2)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests) (2024.7.4)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Downloading pandas-2.2.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.0/13.0 MB\u001b[0m \u001b[31m83.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pandas\n",
            "  Attempting uninstall: pandas\n",
            "    Found existing installation: pandas 2.1.4\n",
            "    Uninstalling pandas-2.1.4:\n",
            "      Successfully uninstalled pandas-2.1.4\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "cudf-cu12 24.4.1 requires pandas<2.2.2dev0,>=2.0, but you have pandas 2.2.2 which is incompatible.\n",
            "google-colab 1.0.0 requires pandas==2.1.4, but you have pandas 2.2.2 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed pandas-2.2.2\n"
          ]
        }
      ],
      "source": [
        "!pip install --upgrade streamlit pyngrok pandas requests"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 107
        },
        "id": "M0wvmMxD8U0N",
        "outputId": "80b9b055-4bac-48fa-fe85-6241a62fef84"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-0218cb89-ce5c-4ede-8241-4b2be57b9e71\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-0218cb89-ce5c-4ede-8241-4b2be57b9e71\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving movies.pkl to movies.pkl\n",
            "Saving similarity.pkl to similarity.pkl\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "print(os.listdir('/content'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YscU7kxIWijw",
        "outputId": "aedf32e2-b22b-4a92-ad99-50a02ad7aeff"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['.config', 'app.py', 'similarity.pkl', 'bg.jpg', 'movies.pkl', 'sample_data']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import requests\n",
        "\n",
        "# CSS for Netflix-style background and fonts\n",
        "bg_img = '''\n",
        "<style>\n",
        "[data-testid=\"stAppViewContainer\"] {\n",
        "    background-image: url(\"https://wallpapers.com/images/hd/netflix-background-gs7hjuwvv2g0e9fj.jpg\");\n",
        "    background-size: cover;\n",
        "}\n",
        "\n",
        "h1 {\n",
        "    color: red;\n",
        "    font-family: Helvetica, Arial, sans-serif;\n",
        "}\n",
        "\n",
        "h2, .stMarkdown, .stSelectbox, .stButton>button {\n",
        "    color: white;\n",
        "    font-family: Helvetica, Arial, sans-serif;\n",
        "}\n",
        "\n",
        ".stButton>button {\n",
        "    background-color: #e50914;\n",
        "    color: white;\n",
        "    border: none;\n",
        "    border-radius: 4px;\n",
        "    padding: 10px;\n",
        "    font-size: 16px;\n",
        "    font-weight: bold;\n",
        "    cursor: pointer;\n",
        "}\n",
        "\n",
        ".stButton>button:hover {\n",
        "    background-color: #f40612;\n",
        "}\n",
        "\n",
        "label {\n",
        "    color: white;\n",
        "}\n",
        "\n",
        ".stSelectbox {\n",
        "    color: white;\n",
        "}\n",
        "\n",
        "\n",
        "[data-testid=\"stSelectbox\"] label {\n",
        "    color: white;\n",
        "}\n",
        "\n",
        "\n",
        "</style>\n",
        "'''\n",
        "st.markdown(bg_img, unsafe_allow_html=True)\n",
        "\n",
        "def fetch_poster(movie_id):\n",
        "    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1567e54c5f3a5de2b7d2d7a97e3383c3&language=en-US'.format(movie_id))\n",
        "    data = response.json()\n",
        "    return \"https://image.tmdb.org/t/p/w500/\" + data['poster_path']\n",
        "\n",
        "def recommend(movie):\n",
        "    movies_index = df[df['title'] == movie].index[0]\n",
        "    distances = similar[movies_index]\n",
        "    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])\n",
        "\n",
        "    recommended_movies = []\n",
        "    recommended_movie_posters = []\n",
        "    for i in movies_list[1:6]:\n",
        "        movie_id = df.iloc[i[0]].movie_id\n",
        "\n",
        "        recommended_movies.append(df.iloc[i[0]].title)\n",
        "        # Fetching movie posters from API\n",
        "        recommended_movie_posters.append(fetch_poster(movie_id))\n",
        "        colored_titles = [f'<span style=\"color:white\">{title}</span>' for title in recommended_movies]\n",
        "\n",
        "    return colored_titles, recommended_movie_posters\n",
        "\n",
        "df = pd.read_pickle('/content/movies.pkl')\n",
        "similar = pd.read_pickle('/content/similarity.pkl')\n",
        "\n",
        "st.title(\"Netflix Movies\")\n",
        "st.write(\"Welcome to the Netflix Movies!\")\n",
        "\n",
        "select_movie = st.selectbox('Search A Movie', df['title'].values, index=0, key='select_movie', help=\"Select a movie to get recommendations.\")\n",
        "\n",
        "if st.button('More Like This'):\n",
        "    names, posters = recommend(select_movie)\n",
        "    poster_width = 140\n",
        "\n",
        "    col1, col2, col3, col4, col5 = st.columns(5)\n",
        "    for i, col in enumerate([col1, col2, col3, col4, col5]):\n",
        "        with col:\n",
        "            st.markdown(names[i], unsafe_allow_html=True)  # Render HTML\n",
        "            st.image(posters[i], width=poster_width)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4u8yq47_Mob1",
        "outputId": "da79caa5-765e-481c-f204-320354390725"
      },
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ngrok authtoken 2ksBfn6NmYPaEKotfiLq9l53VUa_7yi9ucgmy3k2CdEJUCEVz"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V02QdzEW3HaY",
        "outputId": "0779ba8a-4e85-4193-96d3-cf1504b78a4f"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py --server.port 8502 &>/dev/null &"
      ],
      "metadata": {
        "id": "ledXPNHP5QEd"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "public_url = ngrok.connect(8502, 'http')\n",
        "print('Public URL:', public_url)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D8wX5dmv5Sn7",
        "outputId": "6b428c9f-758e-4a7d-f696-b75eb25ab576"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Public URL: NgrokTunnel: \"https://20af-34-145-223-26.ngrok-free.app\" -> \"http://localhost:8502\"\n"
          ]
        }
      ]
    }
  ]
}