from ex11 import Node, Diagnoser, Record, build_tree

BAD_CHILDS = 'There are childs even there shouldnt be.'


def test_remove_empty_true_1():
    # 3 level tree
    #   _x____
    #  /      \
    #  y     _y__
    # / \   /    \
    # a z None None
    # -------------
    #  y
    # / \
    # a z
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y1 = Node('y', none, none)
    x = Node('x', y1, y2)
    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == y2.data
    assert d.root.positive_child.data == y2.positive_child.data
    assert d.root.negative_child.data == y2.negative_child.data


def test_remove_empty_true_2():
    # 4 level tree - node with both child nones
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y1 = Node('y', Node('b', none, none), Node('d', none, none))
    x = Node('x', y1, y2)
    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == y2.data
    assert d.root.positive_child.data == y2.positive_child.data
    assert d.root.negative_child.data == y2.negative_child.data

    try:
        wrong_2nd_pospos = d.root.positive_child.positive_child.data
        wrong_2nd_posneg = d.root.positive_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except AttributeError:
        pass


def test_remove_empty_true_3():
    # 4 level tree - node with only neg child none
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y1 = Node('y', Node('b', none, none), Node('d', Node('e'), none))
    x = Node('x', y1, y2)

    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == x.data
    assert d.root.positive_child.data == 'e'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'

    try:
        wrong_2nd_pospos = d.root.positive_child.positive_child.data
        wrong_2nd_posneg = d.root.positive_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except AttributeError:
        pass


def test_remove_empty_true_4():
    # 4 level tree - node with only pos child none
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y1 = Node('y', Node('b', none, none), Node('d', none, Node('e')))
    x = Node('x', y1, y2)

    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == x.data
    assert d.root.positive_child.data == 'e'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'

    try:
        wrong_2nd_pospos = d.root.positive_child.positive_child.data
        wrong_2nd_posneg = d.root.positive_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except AttributeError:
        pass


def test_remove_empty_true_5():
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    e = Node('e')
    y1 = Node('y', Node('b', e, none), Node('d', none, none))
    x = Node('x', y1, y2)

    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == x.data
    assert d.root.positive_child.data == 'e'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'

    try:
        wrong_2nd_pospos = d.root.positive_child.positive_child.data
        wrong_2nd_posneg = d.root.positive_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except AttributeError:
        pass

def test_remove_empty_true_6():
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    e = Node('e')
    y1 = Node('y', Node('b', none, e), Node('d', none, none))
    x = Node('x', y1, y2)

    d = Diagnoser(x)
    d.minimize(True)

    assert d.root.data == x.data
    assert d.root.positive_child.data == 'e'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'

    try:
        wrong_2nd_pospos = d.root.positive_child.positive_child.data
        wrong_2nd_posneg = d.root.positive_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except AttributeError:
        pass

def test_remove_empty_true_7():
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    e = Node('e')
    y1 = Node('y', Node('b', none, none), Node('d', e, e))
    x = Node('x', y1, y2)

    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == x.data
    assert d.root.positive_child.data == 'e'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'


def test_remove_empty_true_8():
    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    e = Node('e')
    y1 = Node('y', Node('b', e, e), Node('d', none, none))
    x = Node('x', y1, y2)

    d = Diagnoser(x)

    d.minimize(True)
    assert d.root.data == x.data
    assert d.root.positive_child.data == 'e'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'


def test_remove_empty_true_9():
    # all diagnoses are none
    x = build_tree([Record(None, [])], ['a', 'b', 'c'])
    d = Diagnoser(x.root)
    d.minimize(True)

    assert d.root.data is None

    try:
        wrong_pos = d.root.positive_child
        wrong_neg = d.root.negative_child
        raise Exception(BAD_CHILDS)
    except:
        pass


def test_remove_empty_true_10():
    #   _x_________
    #  /           \
    #  y       ____z_
    # / \     /      \
    # a z    _y__    y
    #       /    \  / \
    #     None None a z
    # -------------------
    #  y
    # / \
    # a z

    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y3 = Node('y', none, none)
    y22 = Node('z', y2, y3)
    y1 = Node('y', z, a)
    x = Node('x', y22, y1)

    d = Diagnoser(x)
    d.minimize(True)

    assert d.root.data == 'y'
    assert d.root.positive_child.data == 'z'
    assert d.root.negative_child.data == 'a'


def test_remove_empty_true_11():
    # x
    # --
    # x

    x = Node('x')
    d = Diagnoser(x)
    d.minimize(True)

    assert d.root.data == 'x'


def test_remove_empty_true_12():
    #  x
    # / \
    # y y
    # ----
    # y

    x = Node('x', Node('y'), Node('y'))
    d = Diagnoser(x)
    d.minimize(True)

    assert d.root.data == 'y'

def test_remove_empty_true_13():
    #   _x_____________
    #  /               \
    #  y         ______z_
    # / \       /        \
    # a z      _y_       y
    #         /   \     / \
    #        _a   z__   a z
    #       /  \ /   \
    #     None a z None
    # ------------------------
    #  y
    # / \
    # a z

    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y3 = Node('y', Node('z', none, Node('z')), Node('a', Node('a'), none))
    y22 = Node('z', y2, y3)
    y1 = Node('y', z, a)
    x = Node('x', y22, y1)

    d = Diagnoser(x)
    d.minimize(True)

    assert d.root.data == 'y'
    assert d.root.positive_child.data == 'z'
    assert d.root.negative_child.data == 'a'


def test_remove_empty_true_14():
    #    _None__
    #   /       \
    # None    None
    # --------------
    # None

    x = Node(None, Node(None), Node(None))

    d = Diagnoser(x)
    d.minimize(True)

    assert d.root.data is None


def test_remove_empty_false_1():
    #   _x_
    #  /   \
    #  y   y
    # / \ / \
    # c d b b
    # ---------
    #    _x
    #  /  \
    #  y  b
    # / \
    # c d
    leaf_b = Node('b')
    leaf_c = Node('c')
    leaf_d = Node('d')
    y_pos = Node('y', leaf_b, leaf_b)
    y_neg = Node('y', leaf_d, leaf_c)
    root = Node('x', y_pos, y_neg)
    d = Diagnoser(root)
    d.minimize()

    assert d.root.data == 'x'
    assert d.root.positive_child.data == 'b'
    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'd'
    assert d.root.negative_child.negative_child.data == 'c'

    try:
        wrong1 = d.root.positive_child.data
        wrong2 = d.root.negative_child.data
        raise Exception(BAD_CHILDS)
    except:
        pass

def test_remove_empty_false_2():
    #   _x_
    #  /   \
    #  y   y
    # / \ / \
    # b b b c
    # ---------
    #  x_
    # /  \
    # b  y
    #   / \
    #   b c

    root4 = Node('x', Node('y', Node('c'), Node('b')),
                 Node('y', Node('b'), Node('b')))

    d = Diagnoser(root4)
    d.minimize()

    assert d.root.data == 'x'
    assert d.root.negative_child.data == 'b'
    assert d.root.positive_child.data == 'y'
    assert d.root.positive_child.positive_child.data == 'c'
    assert d.root.positive_child.negative_child.data == 'b'
    try:
        f1 = d.root.negative_child.positive_child
        f2 = d.root.negative_child.negative_child
        raise Exception(BAD_CHILDS)
    except:
        pass


def test_remove_empty_false_3():
    #   _x_
    #  /   \
    #  y   y
    # / \ / \
    # b b b b
    leaf_b = Node('b')
    y_pos = Node('y', leaf_b, leaf_b)
    root = Node('x', y_pos, y_pos)
    d = Diagnoser(root)
    d.minimize()

    assert d.root.data == 'b'
    try:
        f1 = d.root.positive_child
        f2 = d.root.negative_child
        raise Exception(BAD_CHILDS)
    except:
        pass

def test_remove_empty_false_4():
    #   _x_
    #  /   \
    #  y   y
    # / \ / \
    # b a b a
    # ---------
    #  y
    # / \
    # b a
    root3 = Node('x', Node('y', Node('a'), Node('b')),
                 Node('y', Node('a'), Node('b')))
    d = Diagnoser(root3)
    d.minimize()

    assert d.root.data == 'y'
    assert d.root.positive_child.data == 'a'
    assert d.root.negative_child.data == 'b'
    try:
        f1 = d.root.positive_child.positive_child.data
        f2 = d.root.positive_child.negative_child.data
        f3 = d.root.negative_child.positive_child.data
        f4 = d.root.negative_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except:
        pass

def test_remove_empty_false_5():
    #   _x_
    #  /   \
    #  y   y
    # / \ / \
    # a b b a
    # No change.
    root5 = Node('x', Node('y', Node('a'), Node('b')),
                 Node('y', Node('b'), Node('a')))
    d = Diagnoser(root5)
    d.minimize()

    assert d.root.data == 'x'
    assert d.root.positive_child.data == 'y'
    assert d.root.negative_child.data == 'y'
    assert d.root.positive_child.positive_child.data == 'a'
    assert d.root.positive_child.negative_child.data == 'b'
    assert d.root.negative_child.positive_child.data == 'b'
    assert d.root.negative_child.negative_child.data == 'a'


def test_remove_empty_false_6():
    #     ___x___
    #    /       \
    #   _y_     _y_
    #  /   \   /   \
    #  z   z   z   z
    # / \ / \ / \ / \
    # b a b a b a b a
    # -----------------
    #  z
    # / \
    # b a
    root6 = Node('x', Node('y', Node('z', Node('a'), Node('b')),
                           Node('z', Node('a'), Node('b'))),
                 Node('y', Node('z', Node('a'), Node('b')),
                      Node('z', Node('a'), Node('b'))))

    d = Diagnoser(root6)
    d.minimize()

    assert d.root.data == 'z'
    assert d.root.positive_child.data == 'a'
    assert d.root.negative_child.data == 'b'
    try:
        f1 = d.root.positive_child.positive_child.data
        f2 = d.root.positive_child.negative_child.data
        f3 = d.root.negative_child.positive_child.data
        f4 = d.root.negative_child.negative_child.data
        raise Exception(BAD_CHILDS)
    except:
        pass


def test_remove_empty_false_7():
    #   _x_________
    #  /           \
    #  y       ____z_
    # / \     /      \
    # a z    _y__    y
    #       /    \  / \
    #     None None a z
    # -------------------
    #   _x____
    #  /      \
    #  y     _z_
    # / \   /   \
    # a z None  y
    #          / \
    #          a z

    z = Node('z')
    a = Node('a')
    y2 = Node('y', z, a)
    none = Node(None)
    y3 = Node('y', none, none)
    y22 = Node('z', y2, y3)
    y1 = Node('y', z, a)
    x = Node('x', y22, y1)
    d = Diagnoser(x)
    d.minimize()

    assert d.root.data == 'x'
    assert d.root.positive_child.data == 'z'
    assert d.root.positive_child.positive_child.data == 'y'
    assert d.root.positive_child.negative_child.data is None

    assert d.root.negative_child.data == 'y'
    assert d.root.negative_child.positive_child.data == 'z'
    assert d.root.negative_child.negative_child.data == 'a'

    assert d.root.positive_child.positive_child.positive_child.data == 'z'
    assert d.root.positive_child.positive_child.negative_child.data == 'a'


def test_remove_empty_false_8():
    # x
    # --
    # x

    x = Node('x')
    d = Diagnoser(x)
    d.minimize()

    assert d.root.data == 'x'


def test_remove_empty_false_9():
    #  x
    # / \
    # y y
    # ----
    # y

    x = Node('x', Node('y'), Node('y'))
    d = Diagnoser(x)
    d.minimize()

    assert d.root.data == 'y'