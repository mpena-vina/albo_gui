# albo_gui

To run this script, we need to have installed python 3 in a conda environment and the streamlit library
```
conda create --name env_name python=3
conda init
conda activate env_name
pip install streamlit
```

Once this is done, clone the repo
```
git clone https://github.com/mpena-vina/albo_gui.git
```

And run the script
```
streamlit run ./albo_gui/inference_result.py 
```
You can optionally indicate the port with:
```
streamlit run ./albo_gui/inference_result.py --server.port port_number
```
