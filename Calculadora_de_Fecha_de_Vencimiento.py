{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNXyiTesVXVQ9xW6FS62vWO",
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
        "<a href=\"https://colab.research.google.com/github/alchemistcohen/CalculadoraFechaDeVencimiento.github.io/blob/main/Calculadora_de_Fecha_de_Vencimiento.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rp5u0Nk4DAHd",
        "outputId": "690f7cac-009f-4596-a51a-62628d4872f2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting gradio\n",
            "  Downloading gradio-5.12.0-py3-none-any.whl.metadata (16 kB)\n",
            "Collecting aiofiles<24.0,>=22.0 (from gradio)\n",
            "  Downloading aiofiles-23.2.1-py3-none-any.whl.metadata (9.7 kB)\n",
            "Requirement already satisfied: anyio<5.0,>=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.7.1)\n",
            "Collecting fastapi<1.0,>=0.115.2 (from gradio)\n",
            "  Downloading fastapi-0.115.6-py3-none-any.whl.metadata (27 kB)\n",
            "Collecting ffmpy (from gradio)\n",
            "  Downloading ffmpy-0.5.0-py3-none-any.whl.metadata (3.0 kB)\n",
            "Collecting gradio-client==1.5.4 (from gradio)\n",
            "  Downloading gradio_client-1.5.4-py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: httpx>=0.24.1 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.28.1)\n",
            "Requirement already satisfied: huggingface-hub>=0.25.1 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.27.1)\n",
            "Requirement already satisfied: jinja2<4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.1.5)\n",
            "Collecting markupsafe~=2.0 (from gradio)\n",
            "  Downloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)\n",
            "Requirement already satisfied: numpy<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (1.26.4)\n",
            "Requirement already satisfied: orjson~=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.10.13)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from gradio) (24.2)\n",
            "Requirement already satisfied: pandas<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.2.2)\n",
            "Requirement already satisfied: pillow<12.0,>=8.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (11.1.0)\n",
            "Requirement already satisfied: pydantic>=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.10.4)\n",
            "Collecting pydub (from gradio)\n",
            "  Downloading pydub-0.25.1-py2.py3-none-any.whl.metadata (1.4 kB)\n",
            "Collecting python-multipart>=0.0.18 (from gradio)\n",
            "  Downloading python_multipart-0.0.20-py3-none-any.whl.metadata (1.8 kB)\n",
            "Requirement already satisfied: pyyaml<7.0,>=5.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (6.0.2)\n",
            "Collecting ruff>=0.2.2 (from gradio)\n",
            "  Downloading ruff-0.9.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (25 kB)\n",
            "Collecting safehttpx<0.2.0,>=0.1.6 (from gradio)\n",
            "  Downloading safehttpx-0.1.6-py3-none-any.whl.metadata (4.2 kB)\n",
            "Collecting semantic-version~=2.0 (from gradio)\n",
            "  Downloading semantic_version-2.10.0-py2.py3-none-any.whl.metadata (9.7 kB)\n",
            "Collecting starlette<1.0,>=0.40.0 (from gradio)\n",
            "  Downloading starlette-0.45.2-py3-none-any.whl.metadata (6.3 kB)\n",
            "Collecting tomlkit<0.14.0,>=0.12.0 (from gradio)\n",
            "  Downloading tomlkit-0.13.2-py3-none-any.whl.metadata (2.7 kB)\n",
            "Requirement already satisfied: typer<1.0,>=0.12 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.15.1)\n",
            "Requirement already satisfied: typing-extensions~=4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (4.12.2)\n",
            "Collecting uvicorn>=0.14.0 (from gradio)\n",
            "  Downloading uvicorn-0.34.0-py3-none-any.whl.metadata (6.5 kB)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from gradio-client==1.5.4->gradio) (2024.10.0)\n",
            "Requirement already satisfied: websockets<15.0,>=10.0 in /usr/local/lib/python3.10/dist-packages (from gradio-client==1.5.4->gradio) (14.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (1.3.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (1.2.2)\n",
            "Collecting starlette<1.0,>=0.40.0 (from gradio)\n",
            "  Downloading starlette-0.41.3-py3-none-any.whl.metadata (6.0 kB)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (2024.12.14)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx>=0.24.1->gradio) (0.14.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.25.1->gradio) (3.16.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.25.1->gradio) (2.32.3)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.25.1->gradio) (4.67.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (2.27.2)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (13.9.4)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3.0,>=1.0->gradio) (1.17.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (2.18.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.25.1->gradio) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.25.1->gradio) (2.3.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio) (0.1.2)\n",
            "Downloading gradio-5.12.0-py3-none-any.whl (57.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.6/57.6 MB\u001b[0m \u001b[31m10.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gradio_client-1.5.4-py3-none-any.whl (321 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m321.4/321.4 kB\u001b[0m \u001b[31m12.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading aiofiles-23.2.1-py3-none-any.whl (15 kB)\n",
            "Downloading fastapi-0.115.6-py3-none-any.whl (94 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m94.8/94.8 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)\n",
            "Downloading python_multipart-0.0.20-py3-none-any.whl (24 kB)\n",
            "Downloading ruff-0.9.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.3/11.3 MB\u001b[0m \u001b[31m65.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading safehttpx-0.1.6-py3-none-any.whl (8.7 kB)\n",
            "Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)\n",
            "Downloading starlette-0.41.3-py3-none-any.whl (73 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.2/73.2 kB\u001b[0m \u001b[31m4.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tomlkit-0.13.2-py3-none-any.whl (37 kB)\n",
            "Downloading uvicorn-0.34.0-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.3/62.3 kB\u001b[0m \u001b[31m3.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading ffmpy-0.5.0-py3-none-any.whl (6.0 kB)\n",
            "Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)\n",
            "Installing collected packages: pydub, uvicorn, tomlkit, semantic-version, ruff, python-multipart, markupsafe, ffmpy, aiofiles, starlette, safehttpx, gradio-client, fastapi, gradio\n",
            "  Attempting uninstall: markupsafe\n",
            "    Found existing installation: MarkupSafe 3.0.2\n",
            "    Uninstalling MarkupSafe-3.0.2:\n",
            "      Successfully uninstalled MarkupSafe-3.0.2\n",
            "Successfully installed aiofiles-23.2.1 fastapi-0.115.6 ffmpy-0.5.0 gradio-5.12.0 gradio-client-1.5.4 markupsafe-2.1.5 pydub-0.25.1 python-multipart-0.0.20 ruff-0.9.1 safehttpx-0.1.6 semantic-version-2.10.0 starlette-0.41.3 tomlkit-0.13.2 uvicorn-0.34.0\n"
          ]
        }
      ],
      "source": [
        "pip install gradio\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import gradio as gr\n",
        "from datetime import datetime, timedelta"
      ],
      "metadata": {
        "id": "Q7fdSQjcDs6-"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Función para calcular la fecha de vencimiento y el lote juliano"
      ],
      "metadata": {
        "id": "q93XdAB_D3Xw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def calcular_vencimiento(fecha_elaboracion, vida_util):\n",
        "\n",
        "    fecha_elaboracion = datetime.strptime(fecha_elaboracion, '%d-%m-%Y')\n",
        "\n",
        "\n",
        "    fecha_vencimiento = fecha_elaboracion + timedelta(days=vida_util)\n",
        "\n",
        "\n",
        "    lote_juliano = fecha_elaboracion.timetuple().tm_yday\n",
        "\n",
        "\n",
        "    return fecha_vencimiento.strftime('%d-%m-%Y'), lote_juliano"
      ],
      "metadata": {
        "id": "hx4Kohb7Ho1c"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Función para calcular la fecha de elaboración a partir del lote juliano y la vida útil"
      ],
      "metadata": {
        "id": "zxXjanI0EfLW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def calcular_fecha_elaboracion(lote_juliano, vida_util):\n",
        "\n",
        "    year = datetime.now().year\n",
        "    primer_dia = datetime(year, 1, 1)\n",
        "\n",
        "\n",
        "    fecha_elaboracion = primer_dia + timedelta(days=lote_juliano - 1)\n",
        "\n",
        "\n",
        "    fecha_vencimiento = fecha_elaboracion + timedelta(days=vida_util)\n",
        "\n",
        "\n",
        "    return fecha_elaboracion.strftime('%d-%m-%Y'), fecha_vencimiento.strftime('%d-%m-%Y')\n"
      ],
      "metadata": {
        "id": "hSCMTpaiHx7H"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Gradio Interface"
      ],
      "metadata": {
        "id": "WtRKwfbcFI80"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def interfaz():\n",
        "    with gr.Blocks() as demo:\n",
        "        with gr.Tab(\"Calcular Fecha de Vencimiento y Lote Juliano\"):\n",
        "            fecha_elaboracion = gr.Textbox(label=\"Fecha de Elaboración (DD-MM-YYYY)\", placeholder=\"Ejemplo: 01-01-2024\")\n",
        "            vida_util = gr.Number(label=\"Días de Vida Útil\", value=30)\n",
        "\n",
        "            resultado_vencimiento = gr.Textbox(label=\"Fecha de Vencimiento\", interactive=False)\n",
        "            resultado_lote_juliano = gr.Textbox(label=\"Lote Juliano\", interactive=False)\n",
        "\n",
        "\n",
        "            btn_calcular = gr.Button(\"Calcular\")\n",
        "\n",
        "\n",
        "            btn_calcular.click(calcular_vencimiento, inputs=[fecha_elaboracion, vida_util], outputs=[resultado_vencimiento, resultado_lote_juliano])\n",
        "\n",
        "        with gr.Tab(\"Calcular Fecha de Elaboración desde Lote Juliano\"):\n",
        "            lote_juliano_input = gr.Number(label=\"Lote Juliano\")\n",
        "            vida_util_input = gr.Number(label=\"Días de Vida Útil\", value=30)\n",
        "\n",
        "            resultado_fecha_elaboracion = gr.Textbox(label=\"Fecha de Elaboración\", interactive=False)\n",
        "            resultado_fecha_vencimiento = gr.Textbox(label=\"Fecha de Vencimiento\", interactive=False)\n",
        "\n",
        "\n",
        "            btn_calcular_invertido = gr.Button(\"Calcular\")\n",
        "\n",
        "\n",
        "            btn_calcular_invertido.click(calcular_fecha_elaboracion, inputs=[lote_juliano_input, vida_util_input], outputs=[resultado_fecha_elaboracion, resultado_fecha_vencimiento])\n",
        "\n",
        "        demo.launch()\n",
        "\n",
        "\n",
        "interfaz()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 646
        },
        "id": "7Y4xpF66H7_2",
        "outputId": "f0d4366b-012b-4464-bada-f7b128676fca"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Running Gradio in a Colab notebook requires sharing enabled. Automatically setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).\n",
            "\n",
            "Colab notebook detected. To show errors in colab notebook, set debug=True in launch()\n",
            "* Running on public URL: https://020a296adfe1a7db34.gradio.live\n",
            "\n",
            "This share link expires in 72 hours. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div><iframe src=\"https://020a296adfe1a7db34.gradio.live\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install huggingface_hub gradio\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OIC6WLA0PKN3",
        "outputId": "4d728b08-89a2-4ac3-8b7c-99cc0f8c4dfc"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: huggingface_hub in /usr/local/lib/python3.10/dist-packages (0.27.1)\n",
            "Requirement already satisfied: gradio in /usr/local/lib/python3.10/dist-packages (5.12.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (3.16.1)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (2024.10.0)\n",
            "Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (24.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (6.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (2.32.3)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (4.67.1)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (4.12.2)\n",
            "Requirement already satisfied: aiofiles<24.0,>=22.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (23.2.1)\n",
            "Requirement already satisfied: anyio<5.0,>=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.7.1)\n",
            "Requirement already satisfied: fastapi<1.0,>=0.115.2 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.115.6)\n",
            "Requirement already satisfied: ffmpy in /usr/local/lib/python3.10/dist-packages (from gradio) (0.5.0)\n",
            "Requirement already satisfied: gradio-client==1.5.4 in /usr/local/lib/python3.10/dist-packages (from gradio) (1.5.4)\n",
            "Requirement already satisfied: httpx>=0.24.1 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.28.1)\n",
            "Requirement already satisfied: jinja2<4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.1.5)\n",
            "Requirement already satisfied: markupsafe~=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.1.5)\n",
            "Requirement already satisfied: numpy<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (1.26.4)\n",
            "Requirement already satisfied: orjson~=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.10.13)\n",
            "Requirement already satisfied: pandas<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.2.2)\n",
            "Requirement already satisfied: pillow<12.0,>=8.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (11.1.0)\n",
            "Requirement already satisfied: pydantic>=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.10.4)\n",
            "Requirement already satisfied: pydub in /usr/local/lib/python3.10/dist-packages (from gradio) (0.25.1)\n",
            "Requirement already satisfied: python-multipart>=0.0.18 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.0.20)\n",
            "Requirement already satisfied: ruff>=0.2.2 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.9.1)\n",
            "Requirement already satisfied: safehttpx<0.2.0,>=0.1.6 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.1.6)\n",
            "Requirement already satisfied: semantic-version~=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.10.0)\n",
            "Requirement already satisfied: starlette<1.0,>=0.40.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.41.3)\n",
            "Requirement already satisfied: tomlkit<0.14.0,>=0.12.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.13.2)\n",
            "Requirement already satisfied: typer<1.0,>=0.12 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.15.1)\n",
            "Requirement already satisfied: uvicorn>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.34.0)\n",
            "Requirement already satisfied: websockets<15.0,>=10.0 in /usr/local/lib/python3.10/dist-packages (from gradio-client==1.5.4->gradio) (14.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (1.3.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (1.2.2)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (2024.12.14)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx>=0.24.1->gradio) (0.14.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (2.27.2)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (13.9.4)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (2.3.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3.0,>=1.0->gradio) (1.17.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (2.18.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio) (0.1.2)\n"
          ]
        }
      ]
    }
  ]
}