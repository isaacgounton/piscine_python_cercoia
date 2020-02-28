

from elements import *
from elem import Text


class Page:
    def __init__(self, elem):
        self.elem = elem
        self.__valide_instance_body_div = [
            H1, H2, Div, Table, Ul, Ol, Span, Text
        ]
        self.__valide_instance = [
            Html, Head, Body, Title, Meta, Img,
            Th, Tr, Td, Li, P, Hr, Br
        ] + self.__valide_instance_body_div

    def __str__(self):
        return (
            "<!DOCTYPE html>\n" if isinstance(self.elem, Html) else ""
        ) + str(self.elem)

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.__str__() + "\n")

    def is_valid(self):
        return self.__climb_tree(self.elem)

    def __climb_tree(self, elem):
        if isinstance(elem, Text):
            return True
        if not self.__is_valid_node(elem):
            return False

        for node in elem.content:
            if not self.__climb_tree(node):
                return False
        return True

    def __is_valid_node(self, node):
        for instance in self.__valide_instance:
            if isinstance(node, instance):
                if isinstance(node, Html):
                    return self.__is_valid_html(node)
                if isinstance(node, Head):
                    return self.__is_valid_head(node)
                if isinstance(node, Body):
                    return self.__is_valid_body_div(node)
                if isinstance(node, Div):
                    return self.__is_valid_body_div(node)
                if (isinstance(node, Title) or isinstance(node, H1) or isinstance(node, H2)
                        or isinstance(node, Li) or isinstance(node, Th) or isinstance(node, Td)):
                    return self.__is_valid_node_with_text(node)
                if isinstance(node, P):
                    return self.__is_valid_p(node)
                if isinstance(node, Span):
                    return self.__is_valid_span(node)
                if isinstance(node, Ul) or isinstance(node, Ol):
                    return self.__is_valid_list(node)
                if isinstance(node, Tr):
                    return self.__is_valid_tr(node)
                if isinstance(node, Table):
                    return self.__is_valid_table(node)
                if isinstance(node, Text):
                    return True
        return False

    def __is_valid_html(self, node):
        if len(node.content) != 2:
            return False
        if not isinstance(node.content[0], Head):
            return False
        if not isinstance(node.content[1], Body):
            return False
        return True

    def __is_valid_head(self, node):
        if len(node.content) != 1:
            return False
        return isinstance(node.content[0], Title)

    def __is_valid_body_div(self, node):
        if len(node.content) == 0:
            return True
        check = True
        for elem in node.content:
            if not check:
                return False
            for instance in self.__valide_instance_body_div:
                if isinstance(elem, instance):
                    check = True
                    break
                check = False
        return check

    def __is_valid_node_with_text(self, node):
        if len(node.content) == 0:
            return True
        if len(node.content) > 1:
            return False
        return isinstance(node.content[0], Text)

    def __is_valid_p(self, node):
        if len(node.content) == 0:
            return True
        for elem in node.content:
            if not isinstance(elem, Text):
                return False
        return True

    def __is_valid_span(self, node):
        if len(node.content) == 0:
            return True
        for elem in node.content:
            if not isinstance(elem, Text):
                if not isinstance(elem, P):
                    return False
        return True

    def __is_valid_list(self, node):
        if len(node.content) < 1:
            return False
        for elem in node.content:
            if not isinstance(elem, Li):
                return False
        return True

    def __is_valid_tr(self, node):
        if len(node.content) < 1:
            return False
        if isinstance(node.content[0], Th):
            for elem in node.content:
                if not isinstance(elem, Th):
                    return False
            return True
        if isinstance(node.content[0], Td):
            for elem in node.content:
                if not isinstance(elem, Td):
                    return False
            return True
        return False

    def __is_valid_table(self, node):
        if len(node.content) == 0:
            return True
        for elem in node.content:
            if not isinstance(elem, Tr):
                return False
        return True


if __name__ == '__main__':
    p = Page(
        Html([
            Head(Title(Text('"Hello test"'))),
            Body([
                H1(Text('"This is a test"')),
                Span(Text('This is span')),
                Div([
                    Ul([
                        Li(Text('This is a li in a ul'))
                    ])
                ]),
                H2(Text('h2 maintenant')),
                P(Text('a p section\nla suite')),  # pwet
                Table([
                    Tr(Th(Text('This is a th in a table'))),
                    Tr(Td(Text('this is a td')))
                ]),
                Ol([
                    Li(Text('<')),
                    Li(Text('>')),
                    Li(Text('"'))
                ])
            ])
        ])
    )
    print(p)
    print(p.is_valid())

    p = Page(
        Html([
            Head(Title(Text('"Hello test"'))),
            Body([
                H1(Text('"This is a test"')),
                Span(Text('This is span')),
                Div([
                    Ul([
                        Li(Text('This is a li in a ul'))
                    ])
                ]),
                H2(Text('h2 maintenant')),
                Table([
                    Tr(Th(Text('This is a th in a table'))),
                    Tr(Td(Text('this is a td')))
                ]),
                Ol([
                    Li(Text('<')),
                    Li(Text('>')),
                    Li(Text('"'))
                ])
            ])
        ])
    )
    print(p)
    print(p.is_valid())
    p.write_to_file('test.html')

    Page(
        Html([
            Head(Title(Text('title'))),
            Body(Div(Span(Text('span'))))
        ])
    )
    print(p)
    print(p.is_valid())

    p = Page(
        Html([
            Head(Title(Text('title'))),
            Body(Div(Span(Text('span'))))
        ])
    )
    print(p)
    print('body simple', p.is_valid())

    ph = Page(Html())
    print('juste html:', ph.is_valid())
    phhb = Page(Html([Head(), Body()]))
    print('html [head, body]:', phhb.is_valid())
    phhb = Page(Html([Body(), Head()]))
    print('html [body, head]:', phhb.is_valid())
    print('test head')
    ph = Page(Head())
    print('head:', ph.is_valid())
    ph = Page(Head(Title()))
    print('head(Title):', ph.is_valid())
    ph = Page(Head([Title(), Div()]))
    print('head([Title, Div]):', ph.is_valid())
    print('test body')
    pb = Page(Body())
    print('body', pb.is_valid())
    pb = Page(Body(Div()))
    print('body(div)', pb.is_valid())
    pb = Page(Body([Div(), Div()]))
    print('body([div, div])', pb.is_valid())
    pb = Page(Body([Div(), Title(), Div()]))
    print('body([div,title div])', pb.is_valid())
    print('title, h1')

    pt = Page(Title(Text('ok')))
    print('title(Text(ok))', pt.is_valid())
    pt = Page(Title([Text('uo'), Text('yo')]))
    print('title([Text(uo), Text(yo)])', pt.is_valid())
    pt = Page(Title(Text('ok')))
    print('title(Text(ok))', pt.is_valid())

    pt = Page(H1([Text('uo'), Text('yo')]))
    print('h1([Text(uo), Text(yo)])', pt.is_valid())
    pt = Page(H1(Text('ok')))
    print('h1(Text(ok))', pt.is_valid())
    pt = Page(H1([Text('uo'), Text('yo')]))
    print('h1([Text(uo), Text(yo)])', pt.is_valid())

    print('p')
    p = Page(P(Text('yo')))
    print('p(text(yo))', p.is_valid())
    p = Page(P([Text('yo'), Text('yo')]))
    print('p([text(yo), text(yo)])', p.is_valid())
    p = Page(P([Text('yo'), Div(), Text('yo')]))
    print('p([text(yo), div(), text(yo)])', p.is_valid())

    print('span')
    p = Page(Span(Text('ok')))
    print('span(text(yo)', p.is_valid())
    p = Page(Span([Text('ok'), P(Text('lol'))]))
    print('span(text(yo), p(lol))', p.is_valid())
    p = Page(Span([Text('ok'), Div(), P(Text('lol'))]))
    print('span(text(yo),div, p(lol))', p.is_valid())

    print('ul ol')
    p = Page(Ul())
    print('Page(Ul())', p.is_valid())
    p = Page(Ul(Li()))
    print('Page(Ul(Li()))', p.is_valid())
    p = Page(Ol(Li()))
    print('Page(Ol(Li()))', p.is_valid())
    p = Page(Ol([Li(), Li()]))
    print('Page(Ol(Li(), Li()))', p.is_valid())

    p = Page(Ol([Li(), Div(),  Li()]))
    print('Page(Ol(Li(),Div(), Li()))', p.is_valid())

    p = Page(Tr())
    print('p = Page(Tr())', p.is_valid())

    p = Page(Tr(Td()))
    print('p = Page(Tr(Td))', p.is_valid())
    p = Page(Tr([Td(), Th()]))
    print('p = Page(Tr(Td, Th))', p.is_valid())

    p = Page(Table(Td()))
    print('p = Page(Table(Td))', p.is_valid())
    p = Page(Table([Tr(), Tr()]))
    print('p = Page(Table(Tr, Tr))', p.is_valid())
