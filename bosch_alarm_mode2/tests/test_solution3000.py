from bosch_alarm_mode2.panel import Panel
import pytest
import asyncio

class TestSolution3000():
    @pytest.mark.asyncio
    async def test_connect(self, TestPanel):
        await TestPanel.connect(load_selector=Panel.LOAD_BASIC_INFO)
        assert TestPanel._connection
    
    @pytest.mark.asyncio
    async def test_get_status(self, TestPanel):
        await TestPanel.connect(load_selector=Panel.LOAD_ALL)
        assert len(TestPanel.points)>0
        TestPanel.print()
         
