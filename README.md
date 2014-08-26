naacl-hlt-2015
==============

Website for the NAACL HLT 2015 Conference.

If you have questions, please ask Peter Ljunglöf (<peter.ljunglof@cse.gu.se>) who is responsible for these pages.

## Information for someone who wants to edit stuff

- The site is using Jekyll by Github Pages, so all you have to do is to commit your changes and Github takes care of publishing it. (But best is to install Jekyll at home and try out your changes by calling `jekyll serve --safe` before committing).

- Most pages are written in Markdown, please try to stick to that. Each file has to start with a header containing the page title, see the other files for inspiration.

- To create a news item, create a new file in the `_posts` directory, with the name `YYYY-MM-DD-title.md`. See the other posts for inspiration.

- The navigation menu is specified in the Yaml file `_data/navigation.yml`. The submenus should pop-up when you hover over them with the mouse, or when you click/touch the menu item. They should automatically disappear after a few seconds. If there is a problem on a browser, please contact Peter.

- The information in the footer is specified in the Yaml file `_config.yml`. The footer should stick to the bottom of the page. 

- The *important dates* are (unfortunately) spread in different files. If a date is changed, make sure to update all relevant files:

    - `call-for-XXX.md`
    - `dates.md`
    - `index.md`

- The banner logo is created in Inkscape (file `_extra/naacl-hlt-2015-banner-original.svg`. If you change it you have to convert it like this:

        cd _extra
        python cleannup_inkscape_svg.py < naacl-hlt-2015-banner-original.svg > ../img/naacl-hlt-2015-banner.svg
        cd ../img
        convert naacl-hlt-2015-banner.svg naacl-hlt-2015-banner.png

- The banner photograph is taken from [Wikimedia Commons](http://commons.wikimedia.org/wiki/File:City_Park_Panorama_2.png), ruthlessly cropped and colorized. The original photo is by Bryan Simmons and distributed under a Createive Commons license, [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/deed.en).
