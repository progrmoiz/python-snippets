# File classtools.py (new)
"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provide an inheritable display overload method that shows
    instance with their class name and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance
    """
    def __gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return attrs

    def __repr__(self):
        return "[%s: %s]" % (self.__class__.__name__, self.__gatherAttrs())

if __name__ == "__main__":

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X,"\n",y)
