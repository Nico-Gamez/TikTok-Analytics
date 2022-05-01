# TikTok Analytics
Project created to allow the **analysis of trending on the TikTok platform**, through graphs, datasets and relationships between variables.

TikTok-Api install (https://github.com/davidteather/TikTok-Api)
```
pip install TikTokApi
python -m playwright install
```

Python and Streamlit are used

**-** Create a virtual enviroment called *"tiktokanalytics"* using the command

```
.python -m venv tiktokanalytics
```

**-** Activate the virtual environment called *"tiktokanalytics"* using the command in CMD:
```
.\tiktokanalytics\Scripts\activate
```

**-** If you want install the enviroment on Jupyter you can do it with
```
python -m pip install ipykernel
```

**-** Install Streamlit via command
```
pip install streamlit
```
When opening the files and executing, the IDE console command that you have to use is
```
python tiktok.py name_hashtag  // Example: python tiktok.py food
```

Where *"name_hashtag"* is changed to the *initial hashtag* that you want to analyze. This is because an argument is requested

Subsequently by command execute
```
streamlit run app.py
```
![commands](https://user-images.githubusercontent.com/99749668/166136422-0c0311dd-a16d-42cc-a936-bdb4cbb5b210.png)


Then the program with the **user interface** will open in the browser.

![1](https://user-images.githubusercontent.com/99749668/166136413-31b704d5-f815-47eb-b812-74914d3e02d0.png)
![2](https://user-images.githubusercontent.com/99749668/166136415-d3bf1484-5081-4e69-ad44-5b44cf8a3a53.png)
![3](https://user-images.githubusercontent.com/99749668/166136416-09079460-04c6-4c58-a752-c0910dc05290.png)
![4](https://user-images.githubusercontent.com/99749668/166136418-0a0093d5-86d2-4aa3-a685-feb5a063f2c3.png)
