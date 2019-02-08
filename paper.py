#! /usr/bin/env python


def print_template():

    #
    # Change these variables
    #
    title = "Exploring the Limits of Weakly Supervised Pretraining"
    authors = "Dhruv Mahajan, Ross Girshick, Vignesh Ramanathan, Kaiming He, Manohar Paluri, Yixuan Li, Ashwin Bharambe, Laurens van der Maaten"
    arxiv = "1805.00932"
    id = "mahajan2018weaklysup"
    year = "2018"
    #
    # End
    #

    authors = authors.split(", ")
    authors_comma = ", ".join(authors).replace(
        "Ross Girshick", "<strong>Ross Girshick</strong>"
    )
    replacements = (
        ("ä", '\\"{a}'),
        ("á", "\\'{a}"),
        ("ü", '\\"{u}')
    )
    authors_latex = " and ".join(authors)
    for (a, b) in replacements:
        authors_latex = authors_latex.replace(a, b)

    tpt = """
<!--------------------------------------------------------------------------->
<!--{id}-->
<!--------------------------------------------------------------------------->
<div class="paper" id="{id}">
  <div class="wide">
    <a class="paper" onclick="_gaq.push(['_trackEvent', 'Pub', 'Download', '{id}']);" href="https://arxiv.org/pdf/{arxiv}">{title}</a><br />
    {authors_comma}<br />
    arXiv preprint {year} /
    <a shape="rect" href="javascript:togglebib('{id}')" class="togglebib">bibtex</a>
    <pre xml:space="preserve">
@article{{{id},
  Author    = {{{authors_latex}}},
  Title     = {{{title}}},
  Journal   = {{arXiv preprint arXiv:{arxiv}}},
  Year      = {{{year}}}}}
    </pre>
  </div>
</div>
<!--------------------------------------------------------------------------->
""".format(
        **locals()
    )
    print(tpt)


if __name__ == "__main__":
    print_template()
