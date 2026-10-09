"""Verifica os exemplos integrais e a janela, sem renderizar o projeto."""
import html
import re
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "docs/06-introducao-tdd"


def canonical_blocks():
    blocks = re.findall(
        r"```(?:\{\.(python|html)\}|[ \t]*(python|html))\n(.*?)\n```",
        (LESSON / "_content.qmd").read_text(),
        re.S,
    )
    return [(braced or plain, code) for braced, plain, code in blocks]


def test_examples_preserve_canonical_code():
    fragment = (LESSON / "_exemplos-codigo.html").read_text()
    examples = re.findall(r'<template id="codigo-(\d+)"[^>]*><pre><code>(.*?)</code></pre></template>', fragment, re.S)
    assert len(examples) == len(canonical_blocks()) == 9
    assert [html.unescape(re.sub(r"<[^>]+>", "", code)) for _, code in examples] == [code for _, code in canonical_blocks()]
    slides = (LESSON / "slides.qmd").read_text()
    assert "_exemplos-codigo.html" in slides
    targets = re.findall(r'data-code-example="(codigo-\d+)"', slides)
    assert targets
    assert set(targets) <= {f"codigo-{i}" for i in range(1, 10)}
    links = re.findall(r'<a\s+href="#(codigo-\d+)"[^>]*data-code-example="(codigo-\d+)"', slides)
    assert len(links) == len(targets)
    assert all(anchor == target for anchor, target in links)


def test_lesson_and_slides_reference_existing_images():
    for source in ("_content.qmd", "slides.qmd"):
        text = (LESSON / source).read_text()
        images = set(re.findall(r'''(?:\.\./\.\./|/)assets/images/06-introducao-tdd/[^)\s"'<>]+''', text))
        assert images, f"Nenhuma imagem encontrada em {source}"
        for image in images:
            path = ROOT / image.lstrip("/") if image.startswith("/") else LESSON / image
            assert path.is_file(), f"Imagem ausente em {source}: {image}"


def test_window_interactions(tmp_path):
    playwright = pytest.importorskip("playwright.sync_api")
    fragment = (LESSON / "_exemplos-codigo.html").read_text()
    fixture = tmp_path / "window.html"
    fixture.write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8">'
                       f'<link rel="stylesheet" href="{(ROOT / "assets/css/code-examples.css").as_uri()}">'
                       '<a id="trigger" href="#codigo-1" data-code-example="codigo-1">Ver código completo</a>'
                       + fragment + f'<script src="{(ROOT / "assets/js/code-examples.js").as_uri()}"></script></html>')
    with playwright.sync_playwright() as p:
        browser = p.chromium.launch(executable_path=shutil.which("chromium"))
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(fixture.as_uri())
        page.locator("#trigger").click()
        dialog = page.locator("#code-examples-dialog")
        assert dialog.is_visible()
        for i, (_, code) in enumerate(canonical_blocks(), 1):
            page.locator("#code-examples-select").select_option(f"codigo-{i}")
            assert page.locator("#code-examples-content code").text_content() == code
            tokens = page.locator("#code-examples-content code span")
            assert tokens.count() > 0
            colors = tokens.evaluate_all("els => [...new Set(els.map(el => getComputedStyle(el).color))]")
            assert colors != ["rgb(241, 245, 249)"]
            if i == 1:
                assert len(colors) >= 3
        assert page.locator("#code-examples-content").evaluate("el => el.scrollHeight > el.clientHeight") is False  # short final example
        page.locator("#code-examples-select").select_option("codigo-6")
        assert page.locator("#code-examples-content").evaluate("el => el.scrollHeight > el.clientHeight")
        width = dialog.bounding_box()["width"]
        page.get_by_role("button", name="Expandir janela", exact=True).click()
        assert dialog.bounding_box()["width"] > width
        size = page.locator("#code-examples-content").evaluate("el => parseFloat(getComputedStyle(el).fontSize)")
        page.get_by_role("button", name="Aumentar fonte", exact=True).click()
        assert page.locator("#code-examples-content").evaluate("el => parseFloat(getComputedStyle(el).fontSize)") > size
        page.keyboard.press("Escape")
        assert not dialog.is_visible()
        assert page.locator("#trigger").evaluate("el => document.activeElement === el")
        page.locator("#trigger").click()
        page.get_by_role("button", name="Fechar janela", exact=True).click()
        assert not dialog.is_visible()
        page.locator("#trigger").click()
        page.keyboard.press("Shift+Tab")
        assert dialog.evaluate("el => el.contains(document.activeElement)")
        page.mouse.click(1, 1)
        assert not dialog.is_visible()
        page.set_viewport_size({"width": 390, "height": 844})
        page.locator("#trigger").click()
        box = dialog.bounding_box()
        assert box["x"] >= 0 and box["x"] + box["width"] <= 390
        assert not errors
        browser.close()
