# AIChatBot

Step 1: Install Ollama
First, download and install Ollama from the official website -https://ollama.com/download .

![image](https://github.com/user-attachments/assets/048c1e52-3e23-4f5d-83e7-bc421a575a15)

Once the download is complete, install the Ollama application like you would do for any other application.

Step 2: Download and run DeepSeek-R1
Let’s test the setup and download our model. Launch the terminal and type the following command.

ollama run deepseek-r1

Ollama offers a range of DeepSeek R1 models, spanning from 1.5B parameters to the full 671B parameter model. The 671B model is the original DeepSeek-R1, while the smaller models are distilled versions based on Qwen and Llama architectures. If your hardware cannot support the 671B model, you can easily run a smaller version by using the following command and replacing the X below with the parameter size you want (1.5b, 7b, 8b, 14b, 32b, 70b, 671b):

ollama run deepseek-r1:Xb

With this flexibility, you can use DeepSeek-R1's capabilities even if you don’t have a supercomputer.

Step 3: Running DeepSeek-R1 in the background
To run DeepSeek-R1 continuously and serve it via an API, start the Ollama server:

ollama serve

This will make the model available for integration with other applications.

Step 4: Accessing DeepSeek-R1 via Python
We can run Ollama in any integrated development environment (IDE) of choice. You can install the Ollama Python package using the following code:

pip install ollama

Once Ollama is installed, use the following script to interact with the model: Our App.py file.

Make UI as you want with HTML and CSS or refer what I've Made.

Thanks,
Gaurav Tiwari
