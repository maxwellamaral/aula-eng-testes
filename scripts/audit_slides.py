#!/usr/bin/env python3
"""
Auditoria visual automatizada para apresentações Reveal.js no Quarto.
Verifica o carregamento, resolução original, dimensões renderizadas, 
visibilidade e enquadramento de todas as imagens em todos os slides.
"""

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def audit_slides(
    slides_html_path: str | Path,
    screenshots_dir: str | Path = "scratch/slides_audit",
) -> bool:
    slides_path = Path(slides_html_path).resolve()
    screenshots_path = Path(screenshots_dir).resolve()

    if not slides_path.is_file():
        print(f"Erro: Arquivo não encontrado: {slides_path}")
        return False

    screenshots_path.mkdir(parents=True, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        
        file_url = slides_path.as_uri()
        print(f"Carregando apresentação: {file_url}")
        await page.goto(file_url, wait_until="networkidle")
        await asyncio.sleep(1)

        total_slides = await page.evaluate("Reveal.getTotalSlides()")
        print(f"Total de slides encontrados: {total_slides}\n")

        all_passed = True
        slides_with_images = 0

        for idx in range(total_slides):
            await page.evaluate(f"Reveal.slide({idx})")
            await asyncio.sleep(0.3)
            
            data = await page.evaluate("""
                () => {
                    const cur = Reveal.getCurrentSlide();
                    if (!cur) return null;
                    const h2 = cur.querySelector('h2');
                    const imgs = Array.from(cur.querySelectorAll('img')).map((img, i) => {
                        const rect = img.getBoundingClientRect();
                        const computed = window.getComputedStyle(img);
                        return {
                            imgIndex: i,
                            src: img.src,
                            complete: img.complete,
                            naturalWidth: img.naturalWidth,
                            naturalHeight: img.naturalHeight,
                            renderedWidth: rect.width,
                            renderedHeight: rect.height,
                            top: rect.top,
                            bottom: rect.bottom,
                            left: rect.left,
                            right: rect.right,
                            display: computed.display,
                            visibility: computed.visibility,
                            isVisible: rect.width > 0 && rect.height > 0 && computed.visibility !== 'hidden' && computed.display !== 'none',
                            isWithinViewport: rect.top >= 0 && rect.left >= 0 && rect.bottom <= window.innerHeight && rect.right <= window.innerWidth
                        };
                    });
                    return {
                        slideIndex: Reveal.getIndices().h + 1,
                        title: h2 ? h2.innerText : 'Slide',
                        imagesCount: imgs.length,
                        images: imgs
                    };
                }
            """)
            
            if data and data['imagesCount'] > 0:
                slides_with_images += 1
                print(f"==================================================")
                print(f"SLIDE {data['slideIndex']:02d} — {data['title']}")
                print(f"==================================================")
                slide_ok = True
                for img in data['images']:
                    filename = Path(img['src']).name
                    print(f"  Imagem: {filename}")
                    print(f"  - Carregada: {img['complete']}")
                    print(f"  - Resolução Original: {img['naturalWidth']}x{img['naturalHeight']} px")
                    print(f"  - Dimensões na Tela: {img['renderedWidth']:.1f}x{img['renderedHeight']:.1f} px")
                    print(f"  - Posição (Bounding Box): Top={img['top']:.1f}px, Left={img['left']:.1f}px")
                    print(f"  - Contida no viewport: {img['isWithinViewport']}")
                    
                    if not img['isVisible'] or not img['isWithinViewport'] or img['renderedHeight'] < 50 or img['renderedWidth'] < 50:
                        slide_ok = False
                        all_passed = False
                        print(f"  >>> ❌ [FALHA] Imagem {filename} não está visível, está pequena demais ou extrapola o viewport!")
                    else:
                        print(f"  >>> ✅ [OK] Imagem visível, dimensionada e contida no viewport.")
                
                # Salvar screenshot
                screenshot_path = screenshots_path / f"slide_{data['slideIndex']:02d}.png"
                await page.screenshot(path=str(screenshot_path))
                print(f"  Screenshot: {screenshot_path}\n")

        await browser.close()
        
        print("="*50)
        print("RESUMO DA AUDITORIA VISUAL")
        print("="*50)
        print(f"Slides com imagens: {slides_with_images}")
        print(f"Status geral: {'✅ APROVADO' if all_passed else '❌ REPROVADO'}")
        return all_passed

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "_site/docs/02-gestao-qualidade/slides.html"
    success = asyncio.run(audit_slides(target))
    sys.exit(0 if success else 1)
