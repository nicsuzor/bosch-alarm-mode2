# Requires pytest-asyncio: `pip install pytest-asyncio`

import os
import pytest

from ..panel import Panel

@pytest.fixture(scope='session')
def TestPanel():
    
    host = os.environ['BOSCH_HOST']
    port = os.environ['BOSCH_PORT']
    passcode = os.environ['BOSCH_PASSCODE']
    
    config = dict(host=host, port=port, passcode=passcode)
    return Panel(**config)