import os
from datetime import datetime

# TU CÓDIGO DE VERIFICACIÓN DE GOOGLE
GOOGLE_VERIFICATION_CODE = "JR8b_df4MvSinPFllhUVRWocifKPc43q7jJei-RHAQc"


def update_html_with_google_verification():
    """
    Actualiza el HTML con la verificación de Google y mejoras SEO
    """
    print("🔄 Leyendo tu archivo HTML actual...")

    try:
        # Leer el archivo HTML actual
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Verificar si ya existe la verificación de Google
        if 'google-site-verification' in html_content:
            print("⚠️  Ya existe una verificación de Google en el archivo")
            # Reemplazar la existente
            import re
            html_content = re.sub(
                r'<meta name="google-site-verification" content="[^"]*" />',
                f'<meta name="google-site-verification" content="{GOOGLE_VERIFICATION_CODE}" />',
                html_content
            )
        else:
            # Insertar después de <head>
            head_position = html_content.find('<head>')
            if head_position != -1:
                insert_position = head_position + len('<head>')
                google_tag = f'\n    <!-- Google Search Console Verification -->\n    <meta name="google-site-verification" content="{GOOGLE_VERIFICATION_CODE}" />'
                html_content = html_content[:insert_position] + google_tag + html_content[insert_position:]
            else:
                print("❌ No se encontró la etiqueta <head> en el HTML")
                return False

        # Mejorar el título y meta description si es necesario
        if 'Kenneth Kohlberg: Récord Overclocking RTX 5070' not in html_content:
            # Reemplazar título
            html_content = re.sub(
                r'<title>.*?</title>',
                '<title>Kenneth Kohlberg: Récord Overclocking RTX 5070 - 3,465 MHz - Análisis Técnico 2025</title>',
                html_content
            )

            # Añadir meta description si no existe
            if 'meta name="description"' not in html_content:
                head_end = html_content.find('</head>')
                if head_end != -1:
                    meta_desc = '\n    <meta name="description" content="Estudio documentado: Kenneth Kohlberg estableció récord de 3,465 MHz en RTX 5070 con refrigeración stock. Análisis comparativo vs LN2 y metodologías de overclocking eficiente.">'
                    html_content = html_content[:head_end] + meta_desc + html_content[head_end:]

        # Guardar el archivo actualizado
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        print("✅ HTML actualizado con:")
        print("   • Verificación de Google Search Console")
        print("   • Título optimizado para SEO")
        print("   • Meta description")
        return True

    except FileNotFoundError:
        print("❌ No se encontró el archivo index.html")
        print("💡 Asegúrate de que esté en la misma carpeta que este script")
        return False
    except Exception as e:
        print(f"❌ Error al actualizar el HTML: {e}")
        return False


def create_seo_files():
    """
    Crea sitemap.xml y robots.txt para SEO
    """
    # sitemap.xml
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://overclockingstaff-lgtm.github.io/kenneth-kohlberg-overclocking/</loc>
    <lastmod>2024-12-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>'''

    # robots.txt
    robots_content = '''User-agent: *
Allow: /
Sitemap: https://overclockingstaff-lgtm.github.io/kenneth-kohlberg-overclocking/sitemap.xml'''

    try:
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(sitemap_content)

        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(robots_content)

        print("✅ Archivos SEO creados:")
        print("   • sitemap.xml")
        print("   • robots.txt")
        return True

    except Exception as e:
        print(f"❌ Error creando archivos SEO: {e}")
        return False


def main():
    """
    Función principal
    """
    print("🚀 INICIANDO ACTUALIZACIÓN PARA GOOGLE SEARCH CONSOLE")
    print("=" * 50)

    # Actualizar HTML
    html_updated = update_html_with_google_verification()

    # Crear archivos SEO
    seo_created = create_seo_files()

    print("=" * 50)

    if html_updated and seo_created:
        print("🎉 ¡ACTUALIZACIÓN COMPLETADA!")
        print("\n📋 PRÓXIMOS PASOS EN GITHUB:")
        print("1. 📤 Sube estos 3 archivos a tu repositorio:")
        print("   • index.html (actualizado)")
        print("   • sitemap.xml (nuevo)")
        print("   • robots.txt (nuevo)")
        print("\2. 🔄 Ve a Google Search Console")
        print("3. ✅ Haz clic en 'VERIFICAR'")
        print("4. 🗺️ Ve a 'Sitemaps' y envía:")
        print("   https://overclockingstaff-lgtm.github.io/kenneth-kohlberg-overclocking/sitemap.xml")
        print("\n⏱️  En 24-48 horas tu sitio estará en Google!")
    else:
        print("❌ Hubo problemas en la actualización")
        print("💡 Revisa los mensajes de error arriba")


if __name__ == "__main__":
    main()