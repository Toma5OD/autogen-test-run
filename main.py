import autogen
from IPython.display import Image
Image(filename='coding/stock_price_ytd.png')

# Define the configuration for the LLM
gpt4_config = {
    "seed": 42,
    "temperature": 0,
    "config_list": autogen.config_list_from_json("config.json", filter_dict={"model": ["gpt-4"]}),
    "request_timeout": 120,
}
