#! /usr/bin/env python

def print_template():
    title = 'Low-shot Visual Recognition by Shrinking and Hallucinating Features'
    authors = ['Bharath Hariharan', 'Ross Girshick']
    arxiv = '1606.02819'
    id = 'hariharan2016lowshot'
    year = '2016'
    month = 'Nov'
    authors_comma = ', '.join(authors)
    authors_latex = ' and '.join(authors)

    tpt = """
<div class="paper" id="{id}">
  <div class="wide">
    <a class="paper" onclick="_gaq.push(['_trackEvent', 'Pub', 'Download', '{id}']);" href="https://arxiv.org/pdf/{arxiv}">{title}</a><br />
    {authors_comma}<br />
    arXiv preprint {month}., {year} /
    <a shape="rect" href="javascript:togglebib('{id}')" class="togglebib">bibtex</a>
    <pre xml:space="preserve">
@article{{{id},
  Author    = {{{authors_latex}}},
  Title     = {{{title}}},
  Journal   = {{arXiv preprint arXiv:{arxiv}}},
  Year      = {{{year}}}}}
    </pre>
  </div>
</div>""".format(**locals())
    print(tpt)


if __name__ == '__main__':
    print_template()
