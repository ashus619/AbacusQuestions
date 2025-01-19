{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO5nHaNYoBTZKsMpc2YqNzg",
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
        "<a href=\"https://colab.research.google.com/github/ashus619/AbacusQuestions/blob/main/Abacus_Questionnaire.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "xaVHvCbfeFNs"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oqWvYmLHNt2e",
        "outputId": "9331ecab-1d4d-4f8d-e38d-39e44f5bdea6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-01-19 06:54:58.614 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.710 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-01-19 06:54:58.712 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.716 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.718 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.720 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.723 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.725 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.726 Session state does not function when running a script without `streamlit run`\n",
            "2025-01-19 06:54:58.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.730 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.732 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.734 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.735 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.741 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.742 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.743 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.747 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.748 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.750 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.752 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.755 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.757 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.758 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.763 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.764 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.766 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.771 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.773 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.775 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.777 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.780 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.782 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-19 06:54:58.783 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "import streamlit as st\n",
        "\n",
        "# Function to generate a question\n",
        "def generate_question():\n",
        "    num1 = random.randint(1, 99)\n",
        "    num2 = random.randint(1, 99)\n",
        "    operation = random.choice([\"+\", \"-\"])\n",
        "    if operation == \"-\" and num1 < num2:\n",
        "        num1, num2 = num2, num1\n",
        "    correct_answer = eval(f\"{num1} {operation} {num2}\")\n",
        "    choices = [correct_answer]\n",
        "    while len(choices) < 4:\n",
        "        fake_answer = random.randint(correct_answer - 10, correct_answer + 10)\n",
        "        if fake_answer not in choices:\n",
        "            choices.append(fake_answer)\n",
        "    random.shuffle(choices)\n",
        "    return f\"What is {num1} {operation} {num2}?\", correct_answer, choices\n",
        "\n",
        "# Initialize session state\n",
        "if \"questions\" not in st.session_state:\n",
        "    st.session_state.questions = [generate_question() for _ in range(20)]\n",
        "if \"current_index\" not in st.session_state:\n",
        "    st.session_state.current_index = 0\n",
        "if \"score\" not in st.session_state:\n",
        "    st.session_state.score = 0\n",
        "\n",
        "# Display the current question\n",
        "if st.session_state.current_index < len(st.session_state.questions):\n",
        "    question, correct_answer, choices = st.session_state.questions[st.session_state.current_index]\n",
        "    st.write(f\"Question {st.session_state.current_index + 1}: {question}\")\n",
        "    user_answer = st.radio(\"Choose your answer:\", choices)\n",
        "\n",
        "    if st.button(\"Submit Answer\"):\n",
        "        # Check if the answer is correct\n",
        "        if user_answer == correct_answer:\n",
        "            st.session_state.score += 1\n",
        "            st.success(\"Correct!\")\n",
        "        else:\n",
        "            st.error(f\"Wrong! The correct answer was {correct_answer}\")\n",
        "\n",
        "        # Move to the next question\n",
        "        st.session_state.current_index += 1\n",
        "\n",
        "else:\n",
        "    # Quiz is complete\n",
        "    st.write(f\"Quiz completed! Your final score is {st.session_state.score}/20\")\n",
        "    st.stop()\n"
      ]
    }
  ]
}