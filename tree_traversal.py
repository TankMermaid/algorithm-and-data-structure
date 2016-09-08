def in_order(root):
    """recursively left - mid - right"""
    if root is None:
        return []
    else:
        return in_order(root.left) + [root.key] + in_order(root.right)


def pre_order(root):
    """recursively mid - left - right"""
    if root is None:
        return []
    else:
        return [root.key] + pre_order(root.left) + pre_order(root.right)


def post_order(root):
    """recursively left - right - mid"""
    if root is None:
        return []
    else:
        return post_order(root.left) + post_order(root.right) + [root.key]
