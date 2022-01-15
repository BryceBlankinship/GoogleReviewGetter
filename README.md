# GoogleReviewGetter
My first REST API. Using async and "normal" syncronous endpoints. I chose Python because of BeautifulSoup being such a good web scraping library, which is used to scrape the review results.

The API itself is built on FastAPI. I chose FastAPI because its insanely easy to use, and is the highest performing API framework for Python (benchmarks right behind NodeJS and Golang).

I created this for personal use, to be called from a website I made for a client (https://www.speedlinewash.com). The calls will be made from JS, but I wanted to make a REST API that could also be called from Golang for future projects, since getting these Google Reviews is actually pretty useful.

Everything will be open-source, I'll take suggestions but since my Github repos are part of my portfolio, I'd like to keep most of the code mine. If you'd like to support me, GET /index.html; I'm going to keep the API open to the public without keys or anything unless it becomes too expensive to run.

Furthermore, the code is NOT licensed, which gives me full legal autonomy on its use. You ARE allowed to copy, reproduce, and use code from this project in PERSONAL projects, you just have to provide a link back to this original repository. You are NOT allowed to use this for commercial use, which includes recreating the API to sell your own API keys, or selling the information that comes from this API. Web scraping for commercial use is illegal in many cases, it depends on the Terms of Service of the targeted site/company for scraping. I don't doubt that these "SaaS" companies offering Google Review embeds are doing just that, however there's also a reason they're all based overseas. I got tired of paying for this service, so just appreciate that I made a free version available to the internet!
