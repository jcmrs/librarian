
from playwright.sync_api import sync_playwright
import markdownify

URL = "https://gemini.google.com/share/949e52dfd7e3"
OUTPUT_FILE = "conversation.md"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Navigating to {URL}...")
        page.goto(URL)

        # Just wait a fixed time for dynamic content to settle
        print("Waiting for page load...")
        page.wait_for_timeout(8000)

        # Check if we have user queries
        count = page.locator("user-query").count()
        print(f"Detected {count} user queries.")

        if count == 0:
            print("No user queries found. Trying to wait longer...")
            page.wait_for_timeout(5000)
            count = page.locator("user-query").count()
            print(f"Detected {count} user queries after wait.")

        # Extract Title
        title = "Gemini Conversation"
        if page.locator("h1.headline").count() > 0:
            title = page.locator("h1.headline").first.inner_text().strip()
        print(f"Title: {title}")

        # Extract Conversation
        elements = page.locator("user-query, response-container").all()
        print(f"Found {len(elements)} total conversation elements.")

        markdown_content = f"# {title}\n\n"

        for i, el in enumerate(elements):
            try:
                tag_name = el.evaluate("el => el.tagName.toLowerCase()")
            except Exception as e:
                print(f"Error evaluating element {i}: {e}")
                continue

            if tag_name == "user-query":
                # User Prompt
                # The text is usually in a div with class 'query-text'
                # Sometimes user-query contains nested elements, be careful
                if el.locator(".query-text").count() > 0:
                    html = el.locator(".query-text").first.inner_html()
                    text = markdownify.markdownify(html, heading_style="ATX").strip()
                    markdown_content += f"## User\n{text}\n\n"

            elif tag_name == "response-container":
                # Gemini Response
                if el.locator(".markdown").count() > 0:
                    html = el.locator(".markdown").first.inner_html()
                    text = markdownify.markdownify(html, heading_style="ATX").strip()
                    markdown_content += f"## Gemini\n{text}\n\n"

        # Save
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"Saved to {OUTPUT_FILE}")
        browser.close()

if __name__ == "__main__":
    run()
