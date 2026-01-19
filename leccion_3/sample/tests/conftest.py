import sys
from pathlib import Path

# Add the sample directory to the path so imports work from any working directory
# NOTE: This is not how I typically do things.  I typically package my code and install it in editable mode for testing
# BUT, that's making things more difficult, this is hacky but does the job
sys.path.insert(0, str(Path(__file__).parent.parent))
