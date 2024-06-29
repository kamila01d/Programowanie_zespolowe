
from fastapi.requests import Request
from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, expect, sync_playwright


def search_komputronik(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        search = product.replace(" ", "%20")
        url = (
            "https://www.komputronik.pl/search/category/?query="
            + search
        )
        page.goto(url)
        page.wait_for_timeout(5000)
        page.wait_for_timeout(3000)
        list_ = page.locator('[class="tests-product-entry"]').all()
        items = []
        for locator in list_[1:]:
            data = locator.locator(
                '[class="product-image"]'
            ).inner_html()
            soup = BeautifulSoup(data, "html.parser")
            img_tag = soup.find("img")
            if img_tag:
                src = img_tag["data-original"]
            else:
                print("No img element found.")
            soup = BeautifulSoup(locator.inner_html(), "html.parser")
            a_tag = soup.find("a")
            name = a_tag.text
            if product.lower() in name.lower():
                href_value = a_tag["href"]
                prize = locator.locator(
                    '[class="text-3xl font-bold leading-8"]'
                ).first.text_content()
                price_str = prize.replace("\xa0", "")
                price_str = price_str.replace(",", ".")
                price_str = price_str.replace("zł", "").strip()
                price_float = float(price_str)
                items.append(
                    {
                        "name": name,
                        "link": href_value,
                        "price": price_float,
                        "src": src,
                    }
                )

        return items


def search_euro_agd(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        search = product.replace(" ", "%20")
        search_url = "https://www.euro.com.pl/search.bhtml?keyword="
        url = search_url + search
        base_url = "https://www.euro.com.pl/"
        page.set_default_timeout(40000)
        page.goto(url)
        page.wait_for_timeout(30000)

        # page.wait_for_timeout(20000)
        page.mouse.wheel(0, 5000)
        page.wait_for_timeout(3000)
        page.mouse.wheel(0, 5000)

        page.wait_for_timeout(3000)
        offers_list_div = page.locator(
            "body > ems-root > eui-root > eui-dropdown-host > div.content > ems-euro-mobile > ems-euro-mobile-product-listings > div > ems-euro-mobile-product-list-wrapper > ems-euro-mobile-product-list > div > div > section > ems-product-list-results > div > ems-euro-mobile-product-medium-box"
        ).all()
        page.wait_for_timeout(3000)
        items = []
        refs = []

        for i in offers_list_div:
            soup = BeautifulSoup(i.inner_html(), "html.parser")
            src_tag = soup.find(
                "img", class_="product-medium-box-content__photo"
            )
            src = src_tag["src"]

            a_tag = soup.find("a")
            href_value = a_tag["href"]
            price = i.locator('[class="parted-price"]').text_content()
            price_str = (
                price.replace("zł", "")
                .replace("\u0142", "")
                .replace(" ", "")
            )

            price_str = price_str[:-2] + "." + price_str[-2:]

            price_float = float(price_str)

            refs.append(url + href_value)
            items.append(
                {
                    "name": a_tag.text,
                    "link": base_url + href_value,
                    "price": price_float,
                    "src": src,
                }
            )
            page.wait_for_timeout(3000)

        return items


def search_morele_net(product_):
    search = product_.replace(" ", "+")
    url = "https://www.morele.net/wyszukiwarka/?q=" + search + "&d=1"

    response = Request.get(url)
    items = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find_all("div", class_="cat-product card")

        for product in products:
            src_tag = product.find("img")
            src = ""

            if src_tag:
                if src_tag.get("src"):
                    src = src_tag["src"]
                elif src_tag.get("data-src"):
                    src = src_tag["data-src"]
                else:
                    src = None

            info = product.find("a", class_="productLink")
            product_name = info.get("title")
            product_link = info.get("href")
            prize = product.find("div", class_="price-new")
            price_text = prize.get_text(strip=True)
            price_text = price_text.replace("zł", "").replace(
                "\xa0", ""
            )
            price_text = price_text.replace(",", ".")
            price_text = price_text.replace(" ", "")
            price_value = float(price_text)

            full_link = f"https://www.morele.net{product_link}"

            items.append(
                {
                    "name": product_name,
                    "link": full_link,
                    "price": price_value,
                    "src": src,
                }
            )

    else:
        print(
            f"Failed to retrieve the page. Status code: {response.status_code}"
        )

    return items
