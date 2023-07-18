from finviz.main_func import (get_all_news, get_analyst_price_targets,
                              get_insider, get_news, get_stock)
from finviz.portfolio import Portfolio
from finviz.screener import Screener
import sys

if sys.version_info > (3, 8):
  from importlib import metadata
  __version__ = metadata.version("finviz")
else:
  import importlib_metadata;
  __version__ = importlib_metadata.version('finviz')