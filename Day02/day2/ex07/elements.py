# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 6

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-25"


from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='html', attr=attr, tag_type='double')


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='head', attr=attr, tag_type='double')


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='body', attr=attr, tag_type='double')


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='title', attr=attr, tag_type='double')


class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='meta', attr=attr, tag_type='simple')


class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='img', attr=attr, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='table', attr=attr, tag_type='double')


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='th', attr=attr, tag_type='double')


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='tr', attr=attr, tag_type='double')


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='td', attr=attr, tag_type='double')


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='ul', attr=attr, tag_type='double')


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='ol', attr=attr, tag_type='double')


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='li', attr=attr, tag_type='double')


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='h1', attr=attr, tag_type='double')


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='h2', attr=attr, tag_type='double')


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='p', attr=attr, tag_type='double')


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='div', attr=attr, tag_type='double')


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='span', attr=attr, tag_type='double')


class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='hr', attr=attr, tag_type='simple')


class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='br', attr=attr, tag_type='simple')


if __name__ == '__main__':
    try:
        print(Html("FAIL"))
    except Exception as e:
        print(e)

    print(Html([Head(), Body()]))

    print("\n")                 # DEBUG

    print(
        Html([
            Head(Title(Text('"Hello ground!"'))),
            Body([
                H1(Text('"Oh no, not again!"')),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ])
    )

    print("\n")                 # DEBUG

    print(
        Html([
            Head([
                Meta(attr={'charset': 'utf-8'}),
                Title(Text('"A title"'))]),
            Body([
                H1(Text('"A h1"')),
                Hr(),
                Br(),
                Span(Text('A span')),
                Div(
                    [Ul([Li(Text('A li in a ul'))])]),
                H2(Text('A h2')),
                P(Text('a p section\nla suite')),
                Table([
                    Tr(Th(Text('A th in a table'))),
                    Tr(Td(Text('A td')))
                ]),
                Ol([
                    Li(Text('Cest <')),
                    Li(Text('Bien >')),
                    Li(Text('Relou "'))
                ]),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ])
    )
