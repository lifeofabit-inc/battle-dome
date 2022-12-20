import scrapy
import re


class HeroSpider(scrapy.Spider):
    name = "heroes"
    start_urls = ["https://knighthood.fandom.com/wiki/Heroes"]

    def parse(self, response):
        hero_table = response.css("table")[0]
        for hero in hero_table.css("tr")[2:]:
            wiki_link = hero.css("td a")[0].attrib["href"]
            hero_link = response.urljoin(wiki_link)

            try:
                hero_object = self.build_hero_object(hero, hero_link)
            except:
                print(f"ERROR: {hero.css('td a::text').get()}")

            yield response.follow(
                wiki_link,
                callback=self.parse_hero,
                cb_kwargs={"hero_object": hero_object},
            )

            # break

    def parse_hero(self, response, hero_object={}):
        hero_object = self.update_hero_object(response, hero_object)
        yield hero_object

    def build_hero_object(self, hero, hero_link):
        return {
            "name": hero.css("td a::text").get(),
            "link": hero_link,
            "button": hero.css("td:nth-child(1)").css("a img").attrib["data-src"],
            "rarity": hero.css("td:nth-child(2)").css("span::text").get().strip(),
            "alignment": hero.css("td:nth-child(3)::text").get().strip(),
            "class": hero.css("td:nth-child(4)::text").get().strip(),
            "strong_versus": hero.css("td:nth-child(5)::text").get().strip(),
            "max_star_bonus": re.sub(
                r"<[a-zA-Z/\s=\"-]+>", "", hero.css("td:nth-child(11)").get()
            ).strip(),
            # hero.css("td:nth-child(11)::text").get()
            # + hero.css("td:nth-child(11) a::text").get(),
            "base": {
                "charge": int(hero.css("td:nth-child(10)::text").get().strip()),
                "strong_versus": hero.css("td:nth-child(6)::text").get().strip(),
                "chance": hero.css("td:nth-child(7)").css("a::text").get(),
            },
            "rage": {
                "strong_versus": hero.css("td:nth-child(8)::text").get().strip(),
                "chance": hero.css("td:nth-child(9)").css("a::text").get(),
            },
        }

    def update_hero_object(self, response, hero_object):
        hero_object.update(
            {
                "image": response.css("figure a img").attrib["src"],
                # "max_star_bonus": response.css("aside")[0].css("div div::text").get()
                # + response.css("aside")[0].css("div div a::text").get(),
                # "max_star_bonus": response.css("aside")[0]
                # .css("div")[11]
                # .css("div::text")
                # .get()
                # + response.css("aside")[0].css("div")[11].css("div a::text").get(),
                "description": response.css("blockquote i::text").get()
                # TODO - Spotlight hero image
                # TODO - Detailed description
            }
        )

        hero_object["base"].update(
            {
                "name": response.css("table.article-table")
                .css("tr:nth-child(2) td i::text")
                .get(),
                "description": response.css("table.article-table")
                .css("tr:nth-child(2)")
                .css("td")[1]
                .css("td::text")
                .get()
                .strip(),
                "level_1": response.css("table.article-table")
                .css("tr:nth-child(2)")
                .css("td")[2]
                .css("td::text")
                .get()
                .strip(),
                "level_30": response.css("table.article-table")
                .css("tr:nth-child(2)")
                .css("td")[3]
                .css("td::text")
                .get()
                .strip(),
                "level_45_max": response.css("table.article-table")
                .css("tr:nth-child(2)")
                .css("td")[4]
                .css("td::text")
                .get()
                .strip(),
            }
        )

        hero_object["rage"].update(
            {
                "name": response.css("table.article-table")
                .css("tr:nth-child(3) td i::text")
                .get(),
                "description": response.css("table.article-table")
                .css("tr:nth-child(3)")
                .css("td")[1]
                .css("td::text")
                .get()
                .strip(),
                "level_1": response.css("table.article-table")
                .css("tr:nth-child(3)")
                .css("td")[2]
                .css("td::text")
                .get()
                .strip(),
                "level_30": response.css("table.article-table")
                .css("tr:nth-child(3)")
                .css("td")[3]
                .css("td::text")
                .get()
                .strip(),
                "level_45_max": response.css("table.article-table")
                .css("tr:nth-child(3)")
                .css("td")[4]
                .css("td::text")
                .get()
                .strip(),
            }
        )

        return hero_object
