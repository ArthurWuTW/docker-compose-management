from pathlib import Path
import flair
flair.cache_root = Path("/home/user/flair_cache")
_ = flair.models.TextClassifier.load('en-sentiment')