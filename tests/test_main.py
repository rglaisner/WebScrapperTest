import unittest
from src.main import parse_books

class TestWebScraper(unittest.TestCase):

    def test_parse_books(self):
        # A sample of the HTML from books.toscrape.com
        html_content = """
        <ol class="row">
            <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                <article class="product_pod">
                    <div class="image_container">
                        <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
                    </div>
                    <p class="star-rating Three">
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                    </p>
                    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
                    <div class="product_price">
                        <p class="price_color">£51.77</p>
                        <p class="instock availability">
                            <i class="icon-ok"></i>
                            In stock
                        </p>
                        <form>
                            <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                        </form>
                    </div>
                </article>
            </li>
        </ol>
        """
        books = parse_books(html_content)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'A Light in the Attic')
        self.assertEqual(books[0]['price'], '£51.77')
        self.assertEqual(books[0]['rating'], 'Three')

if __name__ == '__main__':
    unittest.main()
