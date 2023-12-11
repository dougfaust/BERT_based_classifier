# BERT classifier template script

PyTorch script to put a classifier layer on a masked language model.  Here using [BERT](https://huggingface.co/docs/transformers/model_doc/bert).

This has been used for contstrained topic modeling and sentiment on small blocks of text.  That is, this will truncate anything past the token limit.

## Installation

Using the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Data
Current settings (token length) are appropriate for data like [SMILE project](https://www.kaggle.com/datasets/ashkhagan/smile-twitter-emotion-dataset).  The script can be used on this data without modification, just download the SMILE dataset and update the path in the [config](config.py).

## Usage

Edit batch sizes as appropriate for your hardware.
Learning rates are informed by original [BERT paper](https://arxiv.org/abs/1810.04805).


```bash
python classifier_BERT.py
```

## License
if you find this and like it, take it.
