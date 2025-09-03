import os
import pytest

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    # Agar test fail hua toh screenshot save karo
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        test_name = request.node.name
        page.screenshot(path=f"screenshots/{test_name}.png")
        print(f"Screenshot taken for failed test: {test_name}") 





