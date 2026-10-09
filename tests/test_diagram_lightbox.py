"""Regressões do lightbox com eventos reais, sem renderizar o Quarto."""
import shutil
from pathlib import Path
from urllib.parse import quote

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=[(css, tag) for css in ("slides.css", "styles.css") for tag in ("img", "svg")])
def lightbox_page(request, tmp_path):
    playwright = pytest.importorskip("playwright.sync_api")
    css, tag = request.param
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400"><rect width="800" height="400" fill="navy"/></svg>'
    diagram = (f'<img id="diagram" width="300" src="data:image/svg+xml,{quote(svg)}">'
               if tag == "img" else svg.replace('<svg ', '<svg id="diagram" ', 1))
    fixture = tmp_path / "lightbox.html"
    fixture.write_text(
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8">'
        f'<link rel="stylesheet" href="{(ROOT / "assets/css" / css).as_uri()}">'
        '<div class="reveal"><div class="slides"><section><figure>'
        + diagram + '</figure></section></div></div>'
        f'<script src="{(ROOT / "assets/js/diagram-lightbox.js").as_uri()}"></script></html>'
    )
    with playwright.sync_playwright() as p:
        browser = p.chromium.launch(executable_path=shutil.which("chromium"))
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(fixture.as_uri())
        page.locator("#diagram").click()
        assert page.locator("#diagram-lightbox-modal").evaluate("el => el.classList.contains('active')")
        yield page
        assert not errors
        browser.close()


def test_pan_keeps_lightbox_open_after_mouse_release(lightbox_page):
    page = lightbox_page
    page.locator("#dl-zoom-in").click()
    before = page.locator("#dl-content").evaluate("el => el.style.transform")
    page.mouse.move(640, 360)
    page.mouse.down()
    page.mouse.move(800, 450, steps=12)
    moved = page.locator("#dl-content").evaluate("el => el.style.transform")
    assert moved != before
    page.mouse.up()
    assert page.locator("#diagram-lightbox-modal").evaluate("el => el.classList.contains('active')"), "Soltar o pan não deve fechar o lightbox"
    assert page.locator("#dl-content").evaluate("el => el.style.transform") == moved
    assert page.locator("#dl-content > svg, #dl-content > img").count() == 1
    page.mouse.move(900, 500)
    assert page.locator("#dl-content").evaluate("el => el.style.transform") == moved


@pytest.mark.parametrize("close_method", ["backdrop", "escape", "button"])
def test_explicit_close_still_works_after_pan(lightbox_page, close_method):
    page = lightbox_page
    page.mouse.move(640, 360)
    page.mouse.down()
    page.mouse.move(750, 400, steps=10)
    page.mouse.up()
    assert page.locator("#diagram-lightbox-modal").evaluate("el => el.classList.contains('active')")
    if close_method == "backdrop":
        page.mouse.click(10, 200)
    elif close_method == "escape":
        page.keyboard.press("Escape")
    else:
        page.locator("#dl-close").click()
    assert not page.locator("#diagram-lightbox-modal").evaluate("el => el.classList.contains('active')")


def test_zoom_and_reset_still_work_after_pan(lightbox_page):
    page = lightbox_page
    for x, y in [(800, 450), (600, 350)]:
        page.mouse.move(640, 360)
        page.mouse.down()
        page.mouse.move(x, y, steps=20)
        page.mouse.up()
        assert page.locator("#diagram-lightbox-modal").evaluate("el => el.classList.contains('active')")
    before = page.locator("#dl-content").evaluate("el => el.style.transform")
    page.locator("#dl-zoom-in").click()
    assert page.locator("#dl-content").evaluate("el => el.style.transform") != before
    page.locator("#dl-reset").click()
    assert page.locator("#dl-content").evaluate("el => el.style.transform") == "translate(0px, 0px) scale(1)"
